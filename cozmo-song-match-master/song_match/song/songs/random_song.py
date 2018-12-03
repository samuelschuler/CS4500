"""Module containing :class:`~song_match.song.songs.mary_had_a_little_lamb.MaryHadALittleLamb`."""
import random

from typing import List

from cozmo.lights import Light

from song_match.cube.lights import BLUE_LIGHT
from song_match.cube.lights import CYAN_LIGHT
from song_match.cube.lights import PINK_LIGHT
from song_match.song import Song
from song_match.song.instrument import Instrument
from song_match.song.note import HALF_NOTE
from song_match.song.note import QUARTER_NOTE
from song_match.song.note import EIGHTH_NOTE
from song_match.song.note import WHOLE_NOTE
from song_match.song.note import Note

MEDIUM = 8
LONG = 16

RANDOM_SEQUENCE_MIN_BOUND = 5
RANDOM_SEQUENCE_MAX_BOUND = 10


class RandomSong(Song):

    def random_note(self) -> str:
        random_note_sequence = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        random_note_numbers = "45"
        random_note_pitch = random.choice(random_note_sequence)
        random_note_num = random.choice(random_note_numbers)
        note = random_note_pitch + random_note_num
        return note

    @property
    def _song_id(self) -> str:
        return 'random'

    @property
    def _notes(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()

        if not self.is_notes_set:
            while self.random_note_one == self.random_note_two or self.random_note_one == self.random_note_three \
                    or self.random_note_two == self.random_note_three:
                    self.random_note_one = self.random_note()
                    self.random_note_two = self.random_note()
                    self.random_note_three = self.random_note()

            self.is_notes_set = True

        return [
            Note(self.random_note_one, instrument),
            Note(self.random_note_two, instrument),
            Note(self.random_note_three, instrument)
        ]

    def random_note_length(self):
        return random.choice([WHOLE_NOTE, HALF_NOTE, QUARTER_NOTE, EIGHTH_NOTE])

    @property
    def _sequence(self) -> List[Note]:
        instrument = self.get_instrument().get_instrument_str()

        first_note = Note(self.get_note_at_pos(0), instrument, self.random_note_length())
        second_note = Note(self.get_note_at_pos(1), instrument, self.random_note_length())
        third_note = Note(self.get_note_at_pos(2), instrument, self.random_note_length())

        if not self.is_seq_set:
            self.is_seq_set = True
            choice_sequence = [first_note, second_note, third_note]

            # Determine a random length for the sequence in the range 5-10
            sequence_len = random.randint(RANDOM_SEQUENCE_MIN_BOUND, RANDOM_SEQUENCE_MAX_BOUND)

            for x in range(0, sequence_len):
                self.seq.append(random.choice(choice_sequence))

        print("\tRandomSong(): The first note is ", first_note, "\n\tThe second note is ", second_note,
              "\n\tThe third note is ", third_note, "\n\tThe sequence length is ", self.seq.__len__())

        return self.seq

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
