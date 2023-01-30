from .UserModel import UserModel
from .GroupModel import GroupModel
from .UserChatModel import UserChatModel


def register_models() -> None:
    UserModel()
    GroupModel()
    UserChatModel()
    

