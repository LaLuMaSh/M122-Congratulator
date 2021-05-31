class BirthdateWish:
    def __init__(self, name, birthdate, email):
        self.name = name
        self.birthdate = birthdate
        self.email = email

    def __repr__(self):
        return f'Birthdate: {self.birthdate};Email: {self.email}'

    def __str__(self):
        return f'Birthdate: {self.birthdate};Email: {self.email}'