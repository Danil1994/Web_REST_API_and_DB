from peewee import SqliteDatabase
from config import Settings

database = SqliteDatabase(Settings.DATA_BASE)
