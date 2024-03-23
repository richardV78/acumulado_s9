class City:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
