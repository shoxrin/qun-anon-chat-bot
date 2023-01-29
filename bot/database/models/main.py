from .UserModel import UserModel
from .GroupModel import GroupModel


def register_models() -> None:
    UserModel()
    GroupModel()
    

