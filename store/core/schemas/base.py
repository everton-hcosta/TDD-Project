import uuid
from datetime import datetime, timezone

from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixIn(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
