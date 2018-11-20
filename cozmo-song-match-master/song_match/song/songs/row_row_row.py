
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
        return [
            Note('saxophone_C4'),
            Note('saxophone_D4'),
            Note('saxophone_E4'),
            Note('saxophone_F4'),
            Note('saxophone_G4')
        ]

    @property
    def _sequence(self) -> List[Note]:
        c_quarter = Note('saxophone_C4', QUARTER_NOTE)
        d_quarter = Note('saxophone_D4', QUARTER_NOTE)
        e_quarter = Note('saxophone_E4', QUARTER_NOTE)
        f_quarter = Note('saxophone_F4', QUARTER_NOTE)
        g_quarter = Note('saxophone_G4', QUARTER_NOTE)

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
