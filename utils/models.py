from __future__ import annotations

import time
from dataclasses import dataclass

from utils.shortcuts import get_expiry

"""careful moving the order of the below dataclasses as it will break the corresponding calls to them"""


@dataclass
class BlacklistedUser:
    id: int
    reason: str
    bot: bool
    tickets: bool
    tags: bool
    expires: int = 9999999999

    def fix_db_types(self):
        self.bot = bool(self.bot)
        self.tickets = bool(self.tickets)
        self.tags = bool(self.tags)
        self.expires = int(self.expires)
        return self

    def is_expired(self):
        if self.expires == 9999999999:
            return False
        return int(time.time()) > self.expires

    @property
    def get_expiry(self):
        return get_expiry(self.expires)


@dataclass
class Tag:
    name: str
    content: str
    owner: int
    created_at: int
    views: int = 0


@dataclass
class Alias:
    tag_id: str
    alias: str


@dataclass
class FlagQuizUser:
    user_id: int
    tries: int
    correct: int
    completed: int
