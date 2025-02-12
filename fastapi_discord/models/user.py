from typing import Any, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    global_name: str
    discriminator: str
    avatar: Optional[str]
    avatar_url: Optional[str] = "https://cdn.discordapp.com/embed/avatars/1.png"
    locale: str
    email: Optional[str] = None
    bot: Optional[bool] = None
    mfa_enabled: bool
    flags: int
    premium_type: Optional[int]
    public_flags: int

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.avatar:
            self.avatar_url = f"https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.png"
        else:
            self.avatar_url = "https://cdn.discordapp.com/embed/avatars/1.png"
