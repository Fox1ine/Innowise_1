import logging
from logging.handlers import RotatingFileHandler
import os


ENVIRONMENT = os.getenv('ENV', 'development')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEST_OUTPUT_PATH_DIR = os.path.join(BASE_DIR, r'tests\output_test')


if ENVIRONMENT != 'test':
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'inwise.log')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)



    OUTPUT_PATH_DIR = os.path.join(BASE_DIR, 'output')
    if not os.path.exists(OUTPUT_PATH_DIR):
        os.makedirs(OUTPUT_PATH_DIR)





    INITIAL_DATA_DIR = os.path.join(BASE_DIR, 'data')
    ROOMS_PATH = os.path.join(INITIAL_DATA_DIR, 'rooms.json')
    STUDENTS_PATH = os.path.join(INITIAL_DATA_DIR, 'students.json')
    TESTS_DIR = os.path.join(BASE_DIR, 'tests')


    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(filename=LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger(__name__)

DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '12345',
    'host': 'localhost',
    'port': '5438'
}
