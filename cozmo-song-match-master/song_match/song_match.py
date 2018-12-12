"""Module containing :class:`~song_match.song_match.SongMatch`."""

from asyncio import sleep
from sys import exit
import random
from typing import Callable, List

from cozmo.anim import AnimationTrigger
from cozmo.objects import EvtObjectTapped
from cozmo.objects import LightCube
from cozmo.robot import Robot

from .config import init_mixer
from .cube import NoteCube
from .cube import NoteCubes
from .cube_mat import CubeMat
from .effect import EffectFactory
from .game_constants import MAX_STRIKES
from .game_constants import COZMO_WELCOME_MESSAGE
from .game_constants import STARTING_POSITION, TUTORIAL_STARTING_POSITION
from .game_constants import COZMO_SPEECH_DURATION, COZMO_VOICE_PITCH
from .game_constants import MODE_PROMPT, TUTORIAL_MODE, EAR_TRAINING_MODE, SONGMATCH_MODE
from .game_constants import TUTORIAL_MODE_SELECTED, EAR_TRAINING_SELECTED, SONGMATCH_SELECTED
from .game_constants import TIME_IN_BETWEEN_PLAYERS_AND_COZMO
from .game_constants import ONE_PLAYER, TWO_PLAYERS, THREE_PLAYERS
from .game_constants import COZMO_NEXT_ROUND, COZMO_GAME_START, COZMO_TURN, COZMO_TRY_AGAIN, COZMO_DEMONSTRATE
from .game_constants import COZMO_PLAY_AGAIN, PLAY_AGAIN_YES, PLAY_AGAIN_NO, COZMO_END_GAME, COZMO_NEW_GAME, COZMO_GOOD_JOB
from .option_prompter import OptionPrompter
from .player import Player
from .song import MaryHadALittleLamb
from .song import RainRainGoAway
from .song import HotCrossBuns
from .song import ItsRaining
from .song import RingAround
from .song import RandomSong
from .song import Note
from .song import Song
from .song import Instrument
from .song_robot import SongRobot
from song_match.cube.lights import WHITE_LIGHT


class SongMatch:
    """Main game class."""

    def __init__(self, song: Song = None, num_players: int = None):
        # Set the song to Mary Had  A Little Lamb if no other song was provided.
        self._song = MaryHadALittleLamb() if song is None else song
        self._num_players = num_players
        self._num_games = 0  # Start number of games as 0
        self._game_started = False  # Game has not yet started
        self._mode = SONGMATCH_MODE  # Default to the songmatch game until the user picks an option

        self._song_robot = None
        self._note_cubes = None
        self._effect_factory = None
        self._players = None

        self._prevent_tap = True  # Flag to prevent player from interrupting game by tapping cubes
        self._played_final_round = False  # Keep track of whether the final round has been played

        # Keep track of the songs played. This dictionary represents all the songs that can be played;
        # when the player completes a round, the song completed will be removed from the dictionary.
        self._songs_played = {
            'hcb': HotCrossBuns(),
            'mhall': MaryHadALittleLamb(),
            'rrga': RainRainGoAway(),
            'ir': ItsRaining(),
            'ra': RingAround()
        }

        # This dictionary represents the game mode options the user may select, and will be used as cube pagination
        # with the option_prompter.
        self._mode_options = {
            1: TUTORIAL_MODE,
            2: SONGMATCH_MODE,
            3: EAR_TRAINING_MODE
        }

        self._game_over = False  # Game has not yet started, so game over is false
        self._keep_playing = True  # Default keep playing the game to true

        # Init py_mixer
        init_mixer()

    async def play(self, robot: Robot) -> None:
        """Play the Song Match game.

        Pass this function into :func:`cozmo.run_program`.

        :param robot: Cozmo Robot instance.
        :type robot: :class:`~cozmo.robot.Robot`
        :return: None
        """

        # While the user wishes to keep playing
        while self._keep_playing is True:
            # Set up the song_robot, note_cubes, and effect_factory objects
            self._song_robot = SongRobot(robot, self._song)
            self._note_cubes = NoteCubes.of(self._song_robot)
            self._effect_factory = EffectFactory(self._song_robot)
            await self.__setup()

            # If the tutorial mode was selected, begin the tutorial mode game loop.
            if self._mode is TUTORIAL_MODE:
                await self.__init_tutorial_loop()

            # Otherwise, init the main game loop.
            await self.__init_game_loop()

            # Ask the user if they wish to play again.
            play_again = await self.__get_play_again_option(self._song_robot)

            # Set the user response.
            self._keep_playing = self.__get_play_again(play_again)

            # If the user wishes to keep playing, reset the game.
            if self._keep_playing is True:
                self.reset_game()

        exit(0)

    async def __setup(self) -> None:
        await self._song_robot.world.wait_until_num_objects_visible(3, object_type=LightCube)
        CubeMat.order_cubes_by_position(self._song_robot)
        self._song_robot.world.add_event_handler(EvtObjectTapped, self.__tap_handler)
        self._note_cubes.turn_on_lights()

        # Have Cozmo introduce the game #
        if self._num_games is 0:
            await self._song_robot.say_text(COZMO_WELCOME_MESSAGE, COZMO_SPEECH_DURATION).wait_for_completed()

        self._mode = await self.__setup_mode(self._song_robot)
        if self._mode is EAR_TRAINING_MODE:
            self._song = RandomSong()
            self._song_robot._song = self._song

        if self._mode is not TUTORIAL_MODE:
            self._players = await self.__setup_players(self._song_robot)

    async def __setup_mode(self, song_robot: SongRobot) -> str:
        options = [TUTORIAL_MODE, SONGMATCH_MODE, EAR_TRAINING_MODE]
        option_prompter = OptionPrompter(song_robot)
        mode = await option_prompter.get_option(MODE_PROMPT, options,
                                                [TUTORIAL_MODE_SELECTED, SONGMATCH_SELECTED, EAR_TRAINING_SELECTED])
        return self._mode_options[mode]

    async def __setup_players(self, song_robot: SongRobot) -> List[Player]:
        num_players = self._num_players
        if num_players is None:
            num_players = await self.__get_number_of_players(song_robot)
        return self.__get_players(num_players)

    def reset_game(self):
        self._game_over = False
        self._players = None
        self._played_final_round = False
        self.get_new_song()
        self._song_robot = None
        self._note_cubes = None
        self._effect_factory = None
        self._num_games += 1
        self._game_started = False

    def get_new_song(self):
        song_choices = [MaryHadALittleLamb(), HotCrossBuns(), RainRainGoAway(), RingAround(), ItsRaining()]
        current_song = self._song

        # Delete the song that was previously played from the dictionary.
        del self._songs_played[self._song.get_id()]

        if len(self._songs_played) is 0:
            exit(0)

        while self._song is current_song:
            new_song = random.choice(song_choices)

            if new_song.get_id() in self._songs_played:
                self._song = new_song

    @staticmethod
    async def __get_number_of_players(song_robot: SongRobot) -> int:
        prompt = 'How many players?'
        options = ['One?', 'Two?', 'Three?']
        option_prompter = OptionPrompter(song_robot)
        return await option_prompter.get_option(prompt, options, [ONE_PLAYER, TWO_PLAYERS, THREE_PLAYERS])

    @staticmethod
    def __get_players(num_players: int) -> List[Player]:
        return [Player(i) for i in range(1, num_players + 1)]

    @staticmethod
    async def __get_play_again_option(song_robot: SongRobot) -> int:
        options = [PLAY_AGAIN_YES, PLAY_AGAIN_NO, '']
        option_prompter = OptionPrompter(song_robot)
        await song_robot.turn_back_to_center()
        return await option_prompter.get_option(COZMO_PLAY_AGAIN, options, [COZMO_NEW_GAME, COZMO_END_GAME])

    @staticmethod
    def __get_play_again(play_again: int) -> bool:
        if play_again == 1:
            return True
        else:
            return False

    async def __tap_handler(self, evt, obj=None, tap_count=None, **kwargs) -> None:
        if self._prevent_tap:
            return
        cube = evt.obj
        note_cube = NoteCube(cube, self._song)
        await note_cube.blink_and_play_note()

    async def __init_game_loop(self) -> None:
        current_position = STARTING_POSITION
        # Have Cozmo 'announce' when the game is starting #
        await self._song_robot.say_text(COZMO_GAME_START, COZMO_SPEECH_DURATION).wait_for_completed()

        while self._song.is_not_finished(current_position) and self._game_over is False:
            if self._game_started is True:
                await self._song_robot.say_text(COZMO_NEXT_ROUND, COZMO_SPEECH_DURATION).wait_for_completed()
                await sleep(1)

            await self.__play_round_transition_effect()

            notes = self._song.get_sequence_slice(current_position)
            await self.__play_notes(notes)

            await self.__wait_for_players_to_match_notes(current_position)

            await sleep(TIME_IN_BETWEEN_PLAYERS_AND_COZMO)

            if self._game_over is False:
                await self.__wait_for_cozmo_to_match_notes(current_position)

            await self.__check_for_game_over()

            current_position = self.__update_position(current_position)

            self._game_started = True

        await self.__play_end_game_results()

    async def __init_tutorial_loop(self) -> None:
        current_position = TUTORIAL_STARTING_POSITION

        while self._song.is_not_finished(current_position):
            await self.__play_round_transition_effect()

            notes = self._song.get_sequence_slice(current_position)
            await self.__play_notes(notes)

            user_wrong = await self.__tutorial_wait_for_player_to_match_notes(current_position)

            await sleep(TIME_IN_BETWEEN_PLAYERS_AND_COZMO)

            if user_wrong is True:
                await self.__tutorial_wait_for_cozmo_to_match_notes(current_position)

            current_position = self.__update_position(current_position)

        # Have Cozmo congratulate the user for completing the tutorial
        await self._song_robot.say_text(COZMO_GOOD_JOB, COZMO_SPEECH_DURATION, COZMO_VOICE_PITCH, True).\
            wait_for_completed()

    async def __tutorial_wait_for_player_to_match_notes(self, current_position: int) -> bool:
        await self._song_robot.say_text('Your turn', COZMO_SPEECH_DURATION).wait_for_completed()
        num_notes_played = 0
        attempts = 0
        notes = self._song.get_sequence_slice(current_position)
        notes_to_play = notes.__len__() - 1
        wrong_note = False
        while attempts < 3 and num_notes_played != current_position:
            correct_note = notes[num_notes_played]
            cube_id = self._song.get_cube_id(correct_note)
            note_cube = NoteCube.of(self._song_robot, cube_id)
            await note_cube.flash(WHITE_LIGHT, 5)

            event = await self.__lift_tap_guard(lambda: self._song_robot.world.wait_for(EvtObjectTapped))
            tapped_cube = NoteCube(event.obj, self._song)

            if tapped_cube.note != correct_note:
                attempts += 1
                await self.__play_wrong_note_effect(tapped_cube.cube_id)

                if attempts < 3:
                    await self._song_robot.say_text(COZMO_TRY_AGAIN, COZMO_SPEECH_DURATION).wait_for_completed()

                wrong_note = True
            else:
                wrong_note = False
                await self.__play_correct_sequence_effect(current_position, False)
                num_notes_played += 1

        return wrong_note

    async def __wait_for_players_to_match_notes(self, current_position: int) -> None:
        for i, player in enumerate(self._players):
            if player.num_wrong < MAX_STRIKES:
                await self.__player_turn_prompt(player)
                await self.__wait_for_player_to_match_notes(current_position, i)
        await self.__check_for_game_over()

    async def __wait_for_player_to_match_notes(self, current_position: int, player_index: int) -> None:
        num_notes_played = 0
        notes = self._song.get_sequence_slice(current_position)
        while num_notes_played != current_position:
            event = await self.__lift_tap_guard(lambda: self._song_robot.world.wait_for(EvtObjectTapped))
            tapped_cube = NoteCube(event.obj, self._song)
            correct_note = notes[num_notes_played]

            if tapped_cube.note != correct_note:
                self._players[player_index].num_wrong += 1

                await self.__play_wrong_note_effect(tapped_cube.cube_id)

                if self._players[player_index].num_wrong == MAX_STRIKES:
                    await self._song_robot.say_text(str(self._players[player_index]) + ' you are out!',
                                                    COZMO_SPEECH_DURATION).wait_for_completed()

                return

            num_notes_played += 1

        await self.__play_correct_sequence_effect(current_position)

    async def __lift_tap_guard(self, callable_function: Callable):
        self._prevent_tap = False
        result = await callable_function()
        self._prevent_tap = True
        return result

    # Have cozmo say which player's turn it is #
    async def __player_turn_prompt(self, player: Player) -> None:
        player.id_to_str()

        if len(self._players) > 1:
            prompt = player.players_turn()
            await self._song_robot.say_text(prompt, COZMO_SPEECH_DURATION).wait_for_completed()
        else:
            prompt = player.players_turn()
            await self._song_robot.say_text(prompt, COZMO_SPEECH_DURATION).wait_for_completed()

    async def __wait_for_cozmo_to_match_notes(self, current_position: int) -> None:
        if self._song_robot.num_wrong < MAX_STRIKES:
            # Have Cozmo say that its his turn #
            await self._song_robot.say_text(COZMO_TURN, COZMO_SPEECH_DURATION).wait_for_completed()

            notes = self._song.get_sequence_slice(current_position)
            played_correct_sequence, note = await self._song_robot.play_notes(notes, with_error=True)
            if played_correct_sequence:
                await self.__play_correct_sequence_effect(current_position, is_player=False)
            else:
                self._song_robot.num_wrong += 1
                wrong_cube_id = self._song.get_cube_id(note)
                await self.__play_wrong_note_effect(wrong_cube_id, is_player=False)

    async def __tutorial_wait_for_cozmo_to_match_notes(self, current_position: int) -> None:
        await self._song_robot.say_text(COZMO_DEMONSTRATE, COZMO_SPEECH_DURATION).wait_for_completed()

        notes = self._song.get_sequence_slice(current_position)
        await self._song_robot.play_notes(notes, with_error=False)

    async def __check_for_game_over(self) -> None:
        all_players = self._players + [self._song_robot]
        out_of_game_players = self.__get_out_of_game_players(all_players)
        num_of_players_out_of_game = len(out_of_game_players)
        if num_of_players_out_of_game >= len(self._players) and self._game_over is False:
            # await self.__play_end_game_results()
            self._game_over = True

    @staticmethod
    def __get_out_of_game_players(all_players: list) -> list:
        return [player for player in all_players if player.num_wrong == MAX_STRIKES]

    async def __play_end_game_results(self) -> None:
        winners = await self.__get_winners()
        animation = await self.__play_game_over_effect(winners, did_cozmo_win=self._song_robot.did_win)
        await self.__play_notes(self._song.get_sequence())
        await animation.wait_for_completed()
        sleep(1)
        # exit(0)

    async def __get_winners(self) -> List[Player]:
        return [player for player in self._players if player.did_win]

    async def __play_wrong_note_effect(self, cube_id: int, is_player=True) -> None:
        effect = self._effect_factory.create('WrongNote')
        await effect.play(cube_id, is_player=is_player)

    async def __play_correct_sequence_effect(self, current_position: int, is_player=True) -> None:
        is_sequence_long = self._song.is_sequence_long(current_position)
        effect = self._effect_factory.create('CorrectSequence')
        await effect.play(is_sequence_long=is_sequence_long, is_player=is_player)

    async def __play_round_transition_effect(self) -> None:
        effect = self._effect_factory.create('RoundTransition')
        await effect.play()

    async def __play_game_over_effect(self, winners: List[Player], did_cozmo_win: bool) -> AnimationTrigger:
        effect = self._effect_factory.create('GameOver')
        return await effect.play(winners, did_cozmo_win=did_cozmo_win)

    async def __play_notes(self, notes: List[Note]) -> None:
        for note in notes:
            await self.__play_note(note)
            await sleep(note.duration)

    async def __play_note(self, note: Note) -> None:
        cube_id = self._song.get_cube_id(note)
        note_cube = NoteCube.of(self._song_robot, cube_id)
        await note_cube.blink_and_play_note()

    def __update_position(self, current_position: int) -> int:
        current_position = self.__increment_current_position(current_position)
        return self.__round_current_position(current_position)

    def __increment_current_position(self, current_position: int) -> int:
        medium, long = self._song.get_difficulty_markers()
        if current_position < medium:
            current_position += 1
        elif current_position < long:
            current_position += 2
        else:
            current_position += 3
        return current_position

    def __round_current_position(self, current_position) -> int:
        song_length = self._song.length
        if current_position >= song_length and not self._played_final_round:
            self._played_final_round = True
            return song_length
        elif self._played_final_round:
            return song_length + 1  # The main loop only exits when current position is greater than song length
        else:
            return current_position
