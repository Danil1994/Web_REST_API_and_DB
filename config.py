from os import environ as env
from dotenv import load_dotenv

# Загрузка переменных среды из файла .env без этого не работает
load_dotenv()


class Settings:
    PATH_FILE = env.get('LOCAL_PATH_FILE')
    DATA_BASE = env.get('LOCAL_DATA_BASE')


class Config:
    DEBUG = True
    DEVELOPMENT = True
    DB_HOST = Settings.DATA_BASE


class ProductionConfig(Config):
    DEBUG = False
