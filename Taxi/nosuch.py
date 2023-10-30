class InvalidTaxiName(Exception):
    def __init__(self, taxi_id) -> None:
        self.taxi_id = str(taxi_id)
        self.message = self.taxi_id + "bo'lgan driver yo'q"
        super().__init__(self.message)

