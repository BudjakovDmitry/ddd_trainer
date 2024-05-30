from uuid import UUID

from adapty_app.domains.entities import Device as DeviceEntity
from adapty_app.infrastructure.models.models import Device, User


class DeviceRepository:
    @staticmethod
    def get_device_by_device_id(device_id: UUID) -> Device:
        return Device.objects.get(device_id=device_id)

    @staticmethod
    def save_device(device_data: DeviceEntity, user: User) -> Device:
        device, created = Device.objects.update_or_create(
            device_id=device_data.device_id, user=user, defaults=device_data.dict()
        )
        return device
