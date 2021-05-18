import csv
import datetime
from datetime import date


class BirthdateWish:
    def __init__(self, fileEntry):
        self.birthdate = fileEntry.split(';')[0]
        self.email = fileEntry.split(';')[1]

    def __repr__(self):
        return f'Birthdate: {self.birthdate};Email: {self.email}'

    def __str__(self):
        return f'Birthdate: {self.birthdate};Email: {self.email}'

        # open the birthdate file


def readFile():
    with open('birthdates.csv', mode='r') as birthdatesFile:
        csvFile = csv.reader(birthdatesFile)

        possibleBirthdateWishes = []

        for line in csvFile:
            possibleBirthdateWishes.append(BirthdateWish(line[0]))

        return possibleBirthdateWishes


def getBirthDatesToday():

    def birthDateWish(birthDateWish):
        birthday = datetime.datetime(
            int(birthDateWish.birthdate.split('.')[2]),
            int(birthDateWish.birthdate.split('.')[1]),
            int(birthDateWish.birthdate.split('.')[0])
        ).date()

        today = date.today()

        if (birthday.day == today.day and birthday.month == today.month):
            return True

        return False

    birthDayWishesToday = filter(birthDateWish, readFile())
    return birthDayWishesToday
