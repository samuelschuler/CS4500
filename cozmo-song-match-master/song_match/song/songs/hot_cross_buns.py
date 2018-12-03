"""Module containing :class:`~song_match.song.songs.hot_cross_buns.HotCrossBuns`."""

from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import PINK_LIGHT
from song_match.song import Song
from song_match.song.instrument import Instrument
from song_match.song.note import EIGHTH_NOTE
from song_match.song.note import HALF_NOTE
from song_match.song.note import Note
from song_match.song.note import QUARTER_NOTE

MEDIUM = 5
LONG = 11


class HotCrossBuns(Song):
    """Hot Cross Buns"""

    @property
    def _song_id(self) -> str:
        return 'hcb'

    @property
    def _notes(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()
        return [
            Note('G3', instrument),
            Note('A3', instrument),
            Note('B3', instrument)
        ]

    @property
    def _sequence(self) -> List[Note]:
        # Defining the notes for hot cross buns
        instrument = self.get_instrument().get_instrument_str()
        a_eighth = Note('A3', instrument, EIGHTH_NOTE)
        g_eighth = Note('G3', instrument, EIGHTH_NOTE)
        b_quarter = Note('B3', instrument, QUARTER_NOTE)
        a_quarter = Note('A3', instrument, QUARTER_NOTE)
        g_half = Note('G3', instrument, HALF_NOTE)

        return [
            b_quarter, a_quarter, g_half,
            b_quarter, a_quarter, g_half,
            g_eighth, g_eighth, g_eighth, g_eighth,
            a_eighth, a_eighth, a_eighth, a_eighth,
            b_quarter, a_quarter, g_half,

        ]

    @property
    def _cube_lights(self) -> List[Light]:
        return [
            PINK_LIGHT,
            BLUE_LIGHT,
            CYAN_LIGHT
        ]

    @property
    def _difficulty_markers(self) -> List[int]:
        return [
            MEDIUM,
            LONG
        ]
