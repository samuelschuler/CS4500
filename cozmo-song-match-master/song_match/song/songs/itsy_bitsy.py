"""Module containing :class:`~song_match.song.songs.mary_had_a_little_lamb.MaryHadALittleLamb`."""

from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import PINK_LIGHT
from song_match.song import Song
from song_match.song.note import Note
from song_match.song.note import HALF_NOTE
from song_match.song.note import EIGHTH_NOTE
from song_match.song.note import QUARTER_NOTE
from song_match.song.note import DOTTED_QUARTER_NOTE
from song_match.song.note import DOTTED_HALF_NOTE

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
        instrument = self.get_instrument().get_instrument_str()
        return [
            Note('D4', instrument),
            Note('G5', instrument),
            Note('C4', instrument),
            Note('D4', instrument),
            Note('A4', instrument),
            Note('E4', instrument)
        ]

    @property
    def _sequence(self) -> List[Note]:
        # G  C C  C D  E E #
        # E  D  C  D E C #

        instrument = self.get_instrument().get_instrument_str()
        e_half = Note('E4', instrument, HALF_NOTE)
        c_half = Note('C4', instrument, HALF_NOTE)

        g_quarter = Note('G5', instrument, QUARTER_NOTE)
        d_quarter = Note('D4', instrument, QUARTER_NOTE)
        e_quarter = Note('E4', instrument, QUARTER_NOTE)
        a_quarter = Note('A4', instrument, QUARTER_NOTE)
        c_quarter = Note('C4', instrument, QUARTER_NOTE)

        e_dotted_quarter = Note('E4', instrument, DOTTED_QUARTER_NOTE)
        c_dotted_half = Note('C4', instrument, DOTTED_HALF_NOTE)

        g_eighth = Note('G5', instrument, EIGHTH_NOTE)
        c_eighth = Note('C4', instrument, EIGHTH_NOTE)
        d_eighth = Note('D4', instrument, EIGHTH_NOTE)
        e_eighth = Note('E4', instrument, EIGHTH_NOTE)
        c_eighth = Note('C4', instrument, EIGHTH_NOTE)

        return [
            g_eighth, c_quarter, c_eighth, c_quarter, d_eighth, e_dotted_quarter, e_quarter,
            e_eighth, d_quarter, c_eighth, d_quarter, e_eighth, c_dotted_half
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
