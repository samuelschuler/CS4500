import unittest
from unittest.mock import patch

from song_match.config import init_mixer
from song_match.exceptions import InvalidNoteInstrument
from song_match.song import Note
from song_match.song.instrument import PIANO
from song_match.song.instrument import CLARINET
from song_match.song.instrument import SAXAPHONE


class TestNote(unittest.TestCase):

    @patch('song_match.config.init')
    def test_raises_invalid_note_exception(self, init):
        init_mixer()

        # The Piano has the pitches 1-5 for the note A.#
        with self.assertRaises(InvalidNoteInstrument):
            Note('A6', PIANO)

        # The Piano has the pitches 1-5 for the note B.#
        with self.assertRaises(InvalidNoteInstrument):
            Note('B6', PIANO)

        # The Piano has the pitches 1-5 for the note E.#
        with self.assertRaises(InvalidNoteInstrument):
            Note('E6', PIANO)

        # The Piano has the pitches 1-5 for the note F.#
        with self.assertRaises(InvalidNoteInstrument):
            Note('F6', PIANO)

        # The Piano has the pitches 1-5 for the note G.#
        with self.assertRaises(InvalidNoteInstrument):
            Note('G6', PIANO)

        # The Clarinet does have a C7 note, but the Piano and Saxaphone do not. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C7', PIANO)

        # The Clarinet has the pitches 3-6 for the A note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('A1', CLARINET)

        # The Clarinet has the pitches 3-6 for the A note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('A2', CLARINET)

        # The Clarinet does have a C7 note, but it does not have a
        # A7, B7, D7, E7, F7, or G7 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('A7', CLARINET)

        # The Clarinet has the pitches 3-6 for the B note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('B1', CLARINET)

        # The Clarinet has the pitches 3-6 for the B note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('B2', CLARINET)

        # The Clarinet does have a C7 note, but it does not have a
        # A7, B7, D7, E7, F7, or G7 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('B7', CLARINET)

        # The Clarinet has the pitches 4-6 for the C note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C1', CLARINET)

        # The Clarinet has the pitches 4-6 for the C note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C2', CLARINET)

        # The Clarinet does not have a C3 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C3', CLARINET)

        # The Clarinet has the pitches 3-6 for the D note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('D1', CLARINET)

        # The Clarinet has the pitches 3-6 for the D note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('D2', CLARINET)

        # The Clarinet does have a C7 note, but it does not have a
        # A7, B7, D7, E7, F7, or G7 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('D7', CLARINET)

        # The Clarinet has the pitches 3-6 for the E note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('E1', CLARINET)

        # The Clarinet has the pitches 3-6 for the E note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('E2', CLARINET)

        # The Clarinet does have a C7 note, but it does not have a
        # A7, B7, D7, E7, F7, or G7 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('E7', CLARINET)

        # The Clarinet has the pitches 3-6 for the F note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('F1', CLARINET)

        # The Clarinet has the pitches 3-6 for the F note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('F2', CLARINET)

        # The Clarinet does have a C7 note, but it does not have a
        # A7, B7, D7, E7, F7, or G7 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('F7', CLARINET)

        # The Clarinet has the pitches 3-6 for the G note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('G1', CLARINET)

        # The Clarinet has the pitches 3-6 for the G note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('G2', CLARINET)

        # The Clarinet does have a C7 note, but it does not have a
        # A7, B7, D7, E7, F7, or G7 note. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('G7', CLARINET)

        # The Saxaphone has the pitches 4-6 for the note C. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C3', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for the note A. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('A6', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for the note B. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('B6', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for the note G. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('G6', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for note A. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('A1', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for note A. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('A2', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for note B. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('B1', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for note B. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('B2', SAXAPHONE)

        # The Saxaphone has the pitches 4-6 for note C. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C1', SAXAPHONE)

        # The Saxaphone has the pitches 4-6 for note C. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C2', SAXAPHONE)

        # The Saxaphone has the pitches 3-6 for note D. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('D1', SAXAPHONE)

        # The Saxaphone has the pitches 3-6 for note D. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('D2', SAXAPHONE)

        # The Saxaphone has the pitches 3-6 for note E. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('E1', SAXAPHONE)

        # The Saxaphone has the pitches 3-6 for note E. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('E2', SAXAPHONE)

        # The Saxaphone has the pitches 3-6 for note F. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('F1', SAXAPHONE)

        # The Saxaphone has the pitches 3-6 for note F. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('F2', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for note G. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('G1', SAXAPHONE)

        # The Saxaphone has the pitches 3-5 for note G. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('G2', SAXAPHONE)

        # The Clarinet does have a C7 note, but the Piano and Saxaphone do not. #
        with self.assertRaises(InvalidNoteInstrument):
            Note('C7', SAXAPHONE)

        assert init.called


if __name__ == '__main__':
    unittest.main()
