from gino import Gino

from bot.misc import DBConfig

postgres_url = f'postgresql://{DBConfig.DBUSERNAME}:{DBConfig.DBUSERPASSWORD}@{DBConfig.DBHOST}/{DBConfig.DBNAME}'


