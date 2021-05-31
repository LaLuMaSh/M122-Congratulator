import csv
import datetime
import logging
from datetime import date

from BirthdateWish import BirthdateWish


def read_file(config):
    with open(config["file-path"], mode='r') as birthdatesFile:
        csv_file = csv.reader(birthdatesFile)

        possible_birthdate_wishes = []
        for lines in csv_file:
            line = lines[0]

            if (len(lines) != 1):
                logging.error('error reading lines...')
                return []

            cells = line.split(';')
            if len(cells) != 3:
                logging.error('error reading line: ' + line)
                return []

            possible_birthdate_wishes.append(BirthdateWish(cells[0], cells[1], cells[2]))
        return possible_birthdate_wishes


def get_birth_dates_today(config):
    def birth_date_wish(birth_date_wish: BirthdateWish):
        split = birth_date_wish.birthdate.split('.')
        if len(split) != 3:
            logging.warning('error reading date from: ' + birth_date_wish.birthdate)
            return False

        birthday = datetime.datetime(
            int(split[2]),
            int(split[1]),
            int(split[0])
        ).date()

        today = date.today()

        if birthday.day == today.day and birthday.month == today.month:
            return True

        return False

    birth_day_wishes_today = filter(birth_date_wish, read_file(config))
    return birth_day_wishes_today
