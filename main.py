import json
import logging
import sys
from datetime import datetime

import BirthdayMailManagement
from BirthdayFileManagement import get_birth_dates_today

def runApp() -> bool:
    if len(sys.argv) != 2:
        exit(1212)
        return False

    configPath = sys.argv[1]
    if configPath.startswith('json'):
        exit(213123)
        return False

    with open(configPath) as config_file:
        config = json.load(config_file)
    logging.basicConfig(filename=config['logfile'], level=logging.DEBUG)

    logging.info(datetime.now().strftime("%H:%M:%S") + " starting Congratulator...")
    to_congratulate = get_birth_dates_today(config)

    for cong in to_congratulate:
        BirthdayMailManagement.send_mail(config, cong)
    logging.info(datetime.now().strftime("%H:%M:%S") + " Congratulator: Done")
    return True

runApp()