import random

PIANO = "piano"
CLARINET = "clarinet"
SAXAPHONE = "saxaphone"
PIANO_INDEX = 1
CLARINET_INDEX = 2
SAXAPHONE_INDEX = 3


class Instrument:
    def __init__(self):
        self.instrument_dictionary = {
            PIANO_INDEX: PIANO,
            CLARINET_INDEX: CLARINET,
            SAXAPHONE_INDEX: SAXAPHONE
        }

        self.instrument = self.get_random_instrument()

    def get_instrument_str(self) -> str:
        return self.instrument

    def set_instrument(self) -> None:
        self.instrument = self.get_random_instrument()

    def get_random_instrument(self) -> str:
        random_instrument_index = random.randint(PIANO_INDEX, SAXAPHONE_INDEX)

        return self.instrument_dictionary[random_instrument_index]
