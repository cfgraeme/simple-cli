from collections import UserDict
from typing import Optional, Any


class CLIStore(UserDict):
    """Dict for CLI variables with special handling for * and type checking."""

    def __getitem__(self, key: str) -> Optional[Any]:
        """Get the value of a key."""
        if key == "*":
            raise ValueError("Cannot get a variable with reserved name *")
        if key in self.data:
            return self.data[key]
        else:
            return None

    def __setitem__(self, key: str, raw_value: str) -> None:
        """Set the value of a key."""
        if key == "*":
            raise ValueError("Cannot set a variable with reserved name *")
        value = CLIStore.parse_value(raw_value)
        if self.data.get(key) is None:
            self.data[key] = value
        elif (set_type := type(self.data[key])) != (new_type := type(value)):
            raise ValueError(
                f"Cannot set variable {key} to type {new_type}. "
                f"Variable is already type {set_type}"
            )
        else:
            self.data[key] = value

    @staticmethod
    def parse_value(value: Any) -> Any:
        """If possible, parse value to int or float. Otherwise, return value."""
        if type(value) == str:
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    pass
        return value
