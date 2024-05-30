from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, field_validator

from adapty_app.domains.entities.enums import Gender


class User(BaseModel):
    profile_id: UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    email:  Optional[EmailStr] = None

    @field_validator('gender')
    def platform_validator(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if v not in (p.value for p in Gender):
            raise ValueError(f"Invalid gender value {v}")
        return v

    @field_validator('first_name', 'last_name')
    def string_max_length_validator(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        MAX_LEN = 25
        if len(v) > MAX_LEN:
            raise ValueError(f"Length is more that {MAX_LEN} characters")
        return v
