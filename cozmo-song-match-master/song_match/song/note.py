"""Module containing :class:`~song_match.song.note.Note`."""

from pygame.mixer import Sound

from song_match.sound_effects import get_note_sound_path

EIGHTH_NOTE = .2  #: Time for eighth note.
QUARTER_NOTE = EIGHTH_NOTE * 2  #: Time for quarter note.
HALF_NOTE = QUARTER_NOTE * 2  #: Time for half note.
WHOLE_NOTE = HALF_NOTE * 2  #: Time for whole note.
#: Time for a dotted quarter. A quarter note plus one-half of an eighth note, or 3 eighth notes
DOTTED_QUARTER_NOTE = EIGHTH_NOTE * 3
#: Time for a dotted half. 3 quarter notes
DOTTED_HALF_NOTE = QUARTER_NOTE * 3


class Note:
    """Represents a musical note."""

    # Defining a note
    # Default value (if not provided) for duration is a QUARTER_NOTE
    def __init__(self, note: str, instrument: str, duration: int = QUARTER_NOTE):
        self.duration = duration
        self.note = note
        self.instrument = instrument

        # Add a instrument member variable, such as self.instrument,
        # so we can invoke get_note_sound_path(note) and that function will know
        # whether the instrument is piano, flute, or guitar
        # self.instrument = instrument   <--- where instrument will be provided as a string argument when
        #                                       invoking Note()
        # ex Note() call: Note('A3', EIGHTH_NOTE, guitar)

        # This calls the constructor method for the Sound class, where the __sound is
        # a member variable of the Note class.
        # get_piano_note_sound_path() is in sound_effects.py
        # We will need to change this and allow it to choose flute, piano, or guitar
        self.__sound = Sound(get_note_sound_path(note, instrument))

    def play(self) -> None:
        """Play the note.

        :return: None
        """
        self.__sound.play()

    def to_str(self) -> str:
        return self.note

    def __eq__(self, other):
        return isinstance(other, Note) and self.note == other.note

    def __repr__(self):
        return "<Note '{}'>".format(self.note)

    def __str__(self):
        return "<Note '{}'>".format(self.note)
