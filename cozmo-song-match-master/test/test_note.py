import unittest
from unittest.mock import patch

from song_match.config import init_mixer
from song_match.exceptions import InvalidNote
from song_match.song import Note
from song_match.song.instrument import PIANO
from song_match.song.instrument import CLARINET
from song_match.song.instrument import SAXAPHONE


class TestNote(unittest.TestCase):

    @patch('song_match.config.init')
    def test_raises_invalid_note_exception(self, init):
        init_mixer()
        with self.assertRaises(InvalidNote):
            Note('c4', PIANO)

        with self.assertRaises(InvalidNote):
            Note('c4', CLARINET)

        with self.assertRaises(InvalidNote):
            Note('c4', SAXAPHONE)

        with self.assertRaises(InvalidNote):
            Note('J6', PIANO)

        with self.assertRaises(InvalidNote):
            Note('J6', CLARINET)

        with self.assertRaises(InvalidNote):
            Note('J6', SAXAPHONE)

        with self.assertRaises(InvalidNote):
            Note('Ab4', PIANO)

        with self.assertRaises(InvalidNote):
            Note('Ab4', CLARINET)

        with self.assertRaises(InvalidNote):
            Note('Ab4', SAXAPHONE)

        with self.assertRaises(InvalidNote):
            Note('C10', PIANO)

        with self.assertRaises(InvalidNote):
            Note('C10', CLARINET)

        with self.assertRaises(InvalidNote):
            Note('C10', SAXAPHONE)

        assert init.called


if __name__ == '__main__':
    unittest.main()
