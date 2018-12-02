
"""ring_around_the_rosie.py: ring around song for song match"""

from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import PINK_LIGHT
from song_match.song import Song
from song_match.song.instrument import Instrument
from song_match.song.note import Note
from song_match.song.note import QUARTER_NOTE

MEDIUM = 6
LONG = 12


class RingAround(Song):
    """Ring around the rosie song """

    @property
    def _instrument(self) -> Instrument:
        return Instrument.get_instrument()

    @property
    def _notes(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()
        return [
            Note('D4', instrument),
            Note('B4', instrument),
            Note('E4', instrument)
        ]

    @property
    def _sequence(self) -> List[Note]:
        # Defining notes for it's raining song
        instrument = self.get_instrument().get_instrument_str()
        d_quarter = Note('D4', instrument, QUARTER_NOTE)
        b_quarter = Note('B4', instrument, QUARTER_NOTE)
        e_quarter = Note('E4', instrument, QUARTER_NOTE)
        return [
            d_quarter, d_quarter, b_quarter,
            e_quarter, d_quarter, b_quarter,
            b_quarter, d_quarter, d_quarter,
            b_quarter, e_quarter, d_quarter,
            b_quarter, d_quarter, b_quarter,
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