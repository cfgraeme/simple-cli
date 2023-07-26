from enum import Enum


class Command(Enum):
    """Enum for commands."""

    GET = "GET"
    SET = "SET"
    EXIT = "EXIT"
    NOOP = "NOOP"

    def arg_reqs(self) -> int:
        """Return the number of arguments required for this command."""
        arg_req_map = {
            Command.GET: 1,
            Command.SET: 2,
            Command.EXIT: 0,
            Command.NOOP: 0,
        }
        return arg_req_map[self]
