from typing import Protocol


class MalProgressRepository(Protocol):
    """ """

    def get_progress(self, mal_id: int) -> int | None: ...

    def update_progress(self, mal_id: int, episode_number: int) -> None: ...
