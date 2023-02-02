from os import environ, path
from aiogram import Bot
from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
print(dotenv_path)

TGTOKEN = environ.get('TOKEN')
bot = Bot(token=TGTOKEN, parse_mode='HTML')
    
DBHOST = environ.get('DBHOST')
DBNAME = environ.get('DBNAME')
DBUSERNAME = environ.get('DBUSERNAME')
DBUSERPASSWORD = environ.get('DBUSERPASSWORD')
    
POSTGRES_URI = f'postgresql://{DBUSERNAME}:{DBUSERPASSWORD}@{DBHOST}/{DBNAME}'