from os import environ, path
from aiogram import Bot
from dotenv import load_dotenv

#Connecting the .env file
dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Getting a token from a bot
TGTOKEN = environ.get('TOKEN')
bot = Bot(token=TGTOKEN, parse_mode='HTML') #Create a bot object

#Connecting data from a database    
DBHOST = environ.get('DBHOST')
DBNAME = environ.get('DBNAME')
DBUSERNAME = environ.get('DBUSERNAME')
DBUSERPASSWORD = environ.get('DBUSERPASSWORD')

#Database connection url    
POSTGRES_URI = f'postgresql://{DBUSERNAME}:{DBUSERPASSWORD}@{DBHOST}/{DBNAME}'