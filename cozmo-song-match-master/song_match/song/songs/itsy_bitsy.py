"""Module containing :class:`~song_match.song.songs.mary_had_a_little_lamb.MaryHadALittleLamb`."""

from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import PINK_LIGHT
from song_match.song import Song
#from song_match.song.note import HALF_NOTE
from song_match.song.note import Note
from song_match.song.note import QUARTER_NOTE

MEDIUM = 8
LONG = 16


""" D G G G 
    A B B B
    A G A B G
    B B C D D
    C B C D B """


class ItsyBitsy(Song):
    """Itsy Bitsy Spider"""

    @property
    def _notes(self) -> List[Note]:
        return [
            Note('C4'),
            Note('D4'),
            Note('E4')
        ]

    @property
    def _sequence(self) -> List[Note]:
        g_quarter = Note('G4', QUARTER_NOTE)
        d_quarter = Note('D4', QUARTER_NOTE)
        b_quarter = Note('E4', QUARTER_NOTE)
        a_quarter = Note('A4', QUARTER_NOTE)
        c_quarter = Note('C4', QUARTER_NOTE)

        return [
            d_quarter, g_quarter, g_quarter, g_quarter, a_quarter,
            b_quarter, b_quarter, b_quarter, a_quarter, g_quarter,
            a_quarter, b_quarter, g_quarter, b_quarter, b_quarter,
            c_quarter, d_quarter, d_quarter, c_quarter, b_quarter,
            c_quarter, b_quarter, c_quarter,  d_quarter, b_quarter,
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
