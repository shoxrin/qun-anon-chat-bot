from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import UserModel