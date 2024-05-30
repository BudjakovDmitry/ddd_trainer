from django.db import transaction

from adapty_app.repositories import DeviceRepository, UserRepository


class UserService:
    @staticmethod
    @transaction.atomic
    def create_or_update_user(user_data, device_data):
        user = UserRepository.save_user(user_data)
        DeviceRepository.save_device(device_data, user)
