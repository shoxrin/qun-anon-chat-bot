from os import environ
from typing import Final

class TgKeys:
    TOKEN: Final = environ.get('TOKEN', '5513966790:AAHY7zpvASd6CArlWDSDpsI6Oy31YRIoUfY')
    
class DBConfig:
    DBHOST: Final = environ.get('DBHOST', '192.168.0.11')
    DBNAME: Final = environ.get('DBNAME', 'leskodchatbot')
    DBUSERNAME: Final = environ.get('DBUSERNAME', 'leskod')
    DBUSERPASSWORD: Final = environ.get('DBUSERPASSWORD', 'superpass')
    
    postgres_url = f'postgresql://{DBUSERNAME}:{DBUSERPASSWORD}@{DBHOST}/{DBNAME}'
