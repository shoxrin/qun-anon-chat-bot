from os import environ
from typing import Final

class TgKeys:
    TOKEN: Final = environ.get('TOKEN', '5513966790:AAHY7zpvASd6CArlWDSDpsI6Oy31YRIoUfY')
    
class DBConfig:
    DBHOST: Final = environ.get('DBHOST', 'default')
    DBNAME: Final = environ.get('DBNAME', 'default')
    DBUSERNAME: Final = environ.get('DBUSERNAME', 'default')
    DBUSERPASSWORD: Final = environ.get('DBUSERPASSWORD', 'default')
    
    postgres_url = f'postgresql://{DBUSERNAME}:{DBUSERPASSWORD}@{DBHOST}/{DBNAME}'
