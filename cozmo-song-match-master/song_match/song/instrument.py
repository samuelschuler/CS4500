class Instrument:
    def __init__(self, instrument_type: str):
        # Piano instrument by default #
        self.instrument = instrument_type

    def get_instrument(self) -> str:
        return self.instrument
