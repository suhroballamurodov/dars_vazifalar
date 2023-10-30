class Place:

    def __init__(self, tuman, mahalla):
        self.tuman = tuman
        self.mahalla = mahalla

    def __str__(self):
        return f"Address: {self.tuman}, {self.mahalla}"