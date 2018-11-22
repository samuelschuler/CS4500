
from typing import List

from cozmo.lights import Light


from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import GREEN_LIGHT
from song_match.song import Song
from song_match.song.note import EIGHTH_NOTE
from song_match.song.note import HALF_NOTE
from song_match.song.note import Note
from song_match.song.note import QUARTER_NOTE

MEDIUM = 4
LONG = 12


class RowRowRow(Song):
    """Row row row your boat"""

    @property
    def _notes(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()
        return [
            Note('C4', instrument),
            Note('D4', instrument),
            Note('E4', instrument),
            Note('F4', instrument),
            Note('G4', instrument)
        ]

    @property
    def _sequence(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()
        c_quarter = Note('C4', instrument, QUARTER_NOTE)
        d_quarter = Note('D4', instrument, QUARTER_NOTE)
        e_quarter = Note('E4', instrument, QUARTER_NOTE)
        f_quarter = Note('F4', instrument, QUARTER_NOTE)
        g_quarter = Note('G4', instrument, QUARTER_NOTE)

        return [
            c_quarter, c_quarter, c_quarter, d_quarter,
            e_quarter, e_quarter, d_quarter, e_quarter,
            f_quarter, g_quarter, c_quarter, c_quarter,
            c_quarter, g_quarter, g_quarter, g_quarter,
            e_quarter, e_quarter, e_quarter, c_quarter,
            c_quarter, c_quarter, c_quarter, g_quarter,
            f_quarter, e_quarter, d_quarter, c_quarter,
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
