from bson import ObjectId
from app import mongo

class UserService:
    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data).inserted_id

    @staticmethod
    def get_users():
        return mongo.db.users.find()

    @staticmethod
    def get_user_by_id(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def update_user(user_id, data):
        return mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete_user(user_id):
        return mongo.db.users.delete_one({"_id": ObjectId(user_id)})
