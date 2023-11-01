
class Place:
    def __init__(self, address, district, neighborhood):
        self.address = address
        self.district = district
        self.neighborhood = neighborhood

    def __str__(self):
        return f"{self.address}, {self.district}, {self.neighborhood}"
