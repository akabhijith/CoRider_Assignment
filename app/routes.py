from flask import Blueprint, request, jsonify
from services.user_services import UserService
from app.models import user_serializer

def init_routes(app):
    @app.route('/users', methods=['GET'])
    def get_users():
        users = UserService.get_users()
        return jsonify([user_serializer(user) for user in users])

    @app.route('/users/<id>', methods=['GET'])
    def get_user(id):
        user = UserService.get_user_by_id(id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user_serializer(user))

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user_id = UserService.create_user(data)
        return jsonify({"id": str(user_id)}), 201

    @app.route('/users/<id>', methods=['PUT'])
    def update_user(id):
        data = request.get_json()
        result = UserService.update_user(id, data)
        if result.modified_count == 0:
            return jsonify({"error": "Update failed"}), 400
        return jsonify({"message": "User updated"})

    @app.route('/users/<id>', methods=['DELETE'])
    def delete_user(id):
        result = UserService.delete_user(id)
        if result.deleted_count == 0:
            return jsonify({"error": "Delete failed"}), 400
        return jsonify({"message": "User deleted"})
