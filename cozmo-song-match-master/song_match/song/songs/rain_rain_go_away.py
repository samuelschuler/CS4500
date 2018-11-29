"""Module containing :class:`~song_match.song.songs.rain_rain_go_away.RainRainGoAway`."""

from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import PINK_LIGHT
from song_match.song import Song
from song_match.song.instrument import Instrument
from song_match.song.note import HALF_NOTE
from song_match.song.note import Note
from song_match.song.note import QUARTER_NOTE

MEDIUM = 8
LONG = 16


class RainRainGoAway(Song):
    """Rain Rain Go Away"""

    @property
    def _notes(self) -> List[Note]:
<<<<<<< HEAD
=======
        instrument = self.get_instrument().get_instrument_str()
>>>>>>> 5ceb25a5b2c8c0f6cc9063e9a9ef8290a3de6889
        return [
            Note('E5', instrument),
            Note('G5', instrument),
            Note('A5', instrument)
        ]

    @property
    def _sequence(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()
        print("returning note sequence: instrument is", instrument)
        g_quarter = Note('G5', instrument, QUARTER_NOTE)
        e_quarter = Note('E5', instrument, QUARTER_NOTE)
        a_quarter = Note('A5', instrument, QUARTER_NOTE)
        g_half = Note('G5', instrument, HALF_NOTE)
        e_half = Note('E5', instrument, HALF_NOTE)
        return [g_half, e_half,
                g_quarter, g_quarter, e_half,
                g_quarter, g_quarter, e_quarter, a_quarter, g_quarter, g_quarter, e_half,
                g_quarter, e_half,
                g_quarter, g_quarter, e_half,
                g_quarter, g_quarter, e_quarter, a_quarter, g_quarter, g_quarter, e_half]

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
