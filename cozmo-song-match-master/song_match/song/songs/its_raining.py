


from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import GREEN_LIGHT
from song_match.song import Song
from song_match.song.instrument import Instrument
from song_match.song.note import HALF_NOTE
from song_match.song.note import Note
from song_match.song.note import QUARTER_NOTE

MEDIUM = 8
LONG = 16


class ItsRaining(Song):
    """It's raining, it's pouring """

    @property
    def _instrument(self) -> Instrument:
        return Instrument.get_instrument()

    @property
    def _notes(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()
        return [
            Note('E4', instrument),
            Note('G4', instrument),
            Note('A4', instrument)
        ]

    @property
    def _sequence(self) -> List[Note]:
        # Defining notes for it's raining song
        instrument = self.get_instrument().get_instrument_str()
        a_quarter = Note('C4', instrument, QUARTER_NOTE)
        g_quarter = Note('D4', instrument, QUARTER_NOTE)
        e_quarter = Note('E4', instrument, QUARTER_NOTE)
        g_half = Note('D4', instrument, HALF_NOTE)
        e_half = Note('E4', instrument, HALF_NOTE)
        return [
            e_quarter, g_half, e_quarter, a_quarter, g_half,
            e_quarter, e_quarter, g_half, e_quarter, a_quarter,
            g_half, e_half, e_quarter, g_quarter, g_quarter,
            e_quarter, e_quarter, g_quarter, g_quarter, e_quarter,
            e_quarter, g_quarter, g_quarter, e_quarter, e_quarter,
            e_quarter, a_quarter, g_half, e_quarter
        ]

    @property
    def _cube_lights(self) -> List[Light]:
        return [
            GREEN_LIGHT,
            BLUE_LIGHT,
            CYAN_LIGHT
        ]

    @property
    def _difficulty_markers(self) -> List[int]:
        return [
            MEDIUM,
            LONG
        ]