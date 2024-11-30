from flask_pymongo import ObjectId

def user_serializer(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],  # Consider encrypting this field.
    }
