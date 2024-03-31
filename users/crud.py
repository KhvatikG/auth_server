from users.schemas import CreateUser


def create_user(user_: CreateUser) -> dict:
    user = user_.model_dump()
    return {
        "succes": True,
        "user": user,
    }
