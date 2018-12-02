import asyncio
from asyncio import sleep
from typing import List

from cozmo.objects import EvtObjectTapped
from cozmo.objects import LightCubeIDs

from .cube import NoteCubes
from .cube_mat import CubeMat
from .song_robot import SongRobot
from .sound_effects import play_collect_point_sound


class OptionPrompter:
    """A class to help the user select an option from three different choices."""

    def __init__(self, song_robot: SongRobot):
        self._song_robot = song_robot

    async def get_option(self, prompt: str, options: List[str], response: List[str]) -> int:
        """Prompts the user to select from three different options by tapping a cube.

        1. Cozmo will prompt the user with ``prompt``.
        2. Cozmo will point to each cube saying the corresponding ``option``.
        3. The light chaser effect will start signaling the game is awaiting user input.
        4. Upon successful tap ``collect-point.wav`` is played and the cube flashes green.

        :param prompt: The prompt for Cozmo to say.
        :param options: A list of options associated with each cube.
        :param response: The list of responses based on the cube chosen.
        :return: :attr:`~cozmo.objects.LightCube.cube_id` of the tapped cube.
        """
        assert len(options) == 3

        await self._song_robot.say_text(prompt).wait_for_completed()
        sleep(1)
        for i, cube_id in enumerate(LightCubeIDs):
            prompt = options[i]

            if prompt != '':
                await self._song_robot.say_text(prompt).wait_for_completed()
                mat_position = CubeMat.cube_id_to_position(cube_id)
                action = await self._song_robot.tap_cube(mat_position)
                await action.wait_for_completed()

        note_cubes = NoteCubes.of(self._song_robot)
        note_cubes.start_light_chasers()

        # Try to make cozmo turn toward the cube that was tapped here?
        # Using the turn_to_cube method that they defined but did not use #
        event = await self._song_robot.world.wait_for(EvtObjectTapped)
        cube_id = event.obj.cube_id
        note_cubes.stop_light_chasers()
        play_collect_point_sound()

        print("The cube id is ", CubeMat.cube_id_to_position(cube_id))

        # Have cozmo turn towards the cube after the user taps the cube to select the number of players #
        action = await self._song_robot.tap_cube(cube_id)
        await action.wait_for_completed()

        await asyncio.sleep(1)

        if CubeMat.cube_id_to_position(cube_id) == 1:
            print("cube id is 1, 1 player")
            await self._song_robot.say_text(response[0]).wait_for_completed()
            # await self._song_robot.say_text(ONE_PLAYER).wait_for_completed()
        elif CubeMat.cube_id_to_position(cube_id) == 2:
            print("cube id is 2, 2 player")
            await self._song_robot.say_text(response[1]).wait_for_completed()
            # await self._song_robot.say_text(TWO_PLAYERS).wait_for_completed()
        elif CubeMat.cube_id_to_position(cube_id) == 3 and response.__len__() == 3:
            print("cube id is 3, 3 player")
            await self._song_robot.say_text(response[2]).wait_for_completed()
            # await self._song_robot.say_text(THREE_PLAYERS).wait_for_completed()

        await note_cubes.flash_single_cube_green(cube_id)
        await sleep(1)
        return CubeMat.cube_id_to_position(cube_id)

    # async def get_players_option(self, prompt: str, options: List[str]):
    #
    #     cube_id: int
    #     cube_id = self.get_option(prompt, options)
    #
    #     if CubeMat.cube_id_to_position(cube_id) == 1:
    #         print("cube id is 1, 1 player")
    #         await self._song_robot.say_text(ONE_PLAYER).wait_for_completed()
    #     elif CubeMat.cube_id_to_position(cube_id) == 2:
    #         print("cube id is 2, 2 player")
    #         await self._song_robot.say_text(TWO_PLAYERS).wait_for_completed()
    #     elif CubeMat.cube_id_to_position(cube_id) == 3:
    #         print("cube id is 3, 3 player")
    #         await self._song_robot.say_text(THREE_PLAYERS).wait_for_completed()
    #
    #     return CubeMat.cube_id_to_position