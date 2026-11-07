from typing import Protocol


class TokenProvider(Protocol):
    """ """

    def get_access_token(self) -> str: ...
