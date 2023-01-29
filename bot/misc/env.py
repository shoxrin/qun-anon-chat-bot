from os import environ
from typing import Final

class TgKeys:
    TOKEN: Final = environ.get('TOKEN', '5513966790:AAHY7zpvASd6CArlWDSDpsI6Oy31YRIoUfY')
    
class DBConfig:
    DBHOST: Final = environ.get('DBHOST', '127.0.0.1')
    DBNAME: Final = environ.get('DBNAME', 'leskod_chatbot')
    DBUSERNAME: Final = environ.get('DBUSERNAME', 'leskod_chatbot')
    DBUSERPASSWORD: Final = environ.get('DBUSERPASSWORD', 'superpass')
    
    postgres_url = f'postgresql://{DBUSERNAME}:{DBUSERPASSWORD}@{DBHOST}/{DBNAME}'
