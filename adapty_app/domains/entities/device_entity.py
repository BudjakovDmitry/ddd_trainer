from uuid import UUID

from pydantic import BaseModel, field_validator

from adapty_app.domains.entities.enums import Platform


class Device(BaseModel):
    device_id: UUID
    app_version: str
    platform: str
    timezone: str

    @field_validator('platform')
    def platform_validator(cls, v: str) -> str:
        if v not in (p.value for p in Platform):
            raise ValueError(f"Invalid platform value {v}")
        return v
