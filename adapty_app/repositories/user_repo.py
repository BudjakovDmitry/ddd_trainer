from uuid import UUID

from adapty_app.domains.entities import User as UserEntity
from adapty_app.infrastructure.models.models import User


class UserRepository:
    @staticmethod
    def get_user_by_profile_id(profile_id: UUID) -> User:
        return User.objects.get(profile_id=profile_id)

    @staticmethod
    def save_user(user_data: UserEntity) -> User:
        user, created = User.objects.update_or_create(
            profile_id=user_data.profile_id, defaults=user_data.dict()
        )
        return user
