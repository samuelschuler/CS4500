from cozmo.anim import Triggers

from song_match.effect import Effect
from song_match.sound_effects import play_wrong_buzzer_sound

COZMO_WRONG = "Oops"


class WrongNoteEffect(Effect):
    """Played when either a player or Cozmo plays the wrong note."""

    async def play(self, cube_id: int, is_player: bool = True) -> None:
        """Play the wrong note effect.

        * Play ``wrong-buzzer.wav``
        * Animate Cozmo with :attr:`~cozmo.anim.Triggers.MemoryMatchPlayerLoseHand` or
          :attr:`~cozmo.anim.Triggers.MemoryMatchCozmoLoseHand` depending upon ``is_player``.
        * Flash the incorrect cube red.

        :param cube_id: :attr:`~cozmo.objects.LightCube.cube_id`
        :param is_player: Whether the player or Cozmo played the wrong note.
        :return: None
        """
        play_wrong_buzzer_sound()
        animation = Triggers.MemoryMatchPlayerLoseHand if is_player else Triggers.MemoryMatchCozmoLoseHand

        if not is_player:
            await self._song_robot.say_text(COZMO_WRONG).wait_for_completed()

        action = self._song_robot.play_anim_trigger(animation, in_parallel=True)
        await self._note_cubes.flash_single_cube_red(cube_id)
        await action.wait_for_completed()
