import enum
from dataclasses import dataclass
from uuid import UUID


class UserRole(str, enum.Enum):
    PROFESSOR = "professor"
    COORDENADOR = "coordenador"


@dataclass(frozen=True)
class UserIdentity:
    id: UUID
    email: str
    role: UserRole
