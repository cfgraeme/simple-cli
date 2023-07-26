from cli.store import CLIStore
from cli.command import Command


class CLI:
    """Class for parsing CLI input and performing commands."""

    def __init__(self):
        """Initialize CLI with a CLIStore and a map of commands to functions."""
        self.store = CLIStore()
        self._command_map = {
            Command.GET: self._get,
            Command.SET: self._set,
            Command.EXIT: exit,
            Command.NOOP: lambda _: None,
        }

    def _get(self, args: list[str]):
        """Get a variable from the CLI store, formatted for CLI output."""
        if args[0] == "*":
            for key, value in self.store.items():
                print(f"{key}={value}")
        else:
            print(self.store[args[0]])

    def _set(self, args: list[str]):
        """Set a variable in the CLI store."""
        self.store[args[0]] = args[1]

    def perform(self, command: Command, args: list[str]):
        """Retrieve the function from the command map and perform it."""
        if command:
            self._command_map[command](args)

    def parse(self, line: str) -> tuple[Command, list[str]]:
        """Parse the command line input into a command and args."""

        raw = line.strip().split()
        if not raw:
            return Command.NOOP, []
        if len(raw) > 1:
            raw_command, arg = raw
        else:
            raw_command, arg = raw[0], None

        command = Command(raw_command)
        if not command or command not in self._command_map:
            raise ValueError(
                f"Invalid command {command}. "
                f"Accepted commands: {self._command_map.keys()}"
            )
        if not arg:
            args = []
        elif (arg_len := len(args := arg.split("="))) != command.arg_reqs():
            raise ValueError(
                f"Invalid number of arguments for command {command}. "
                f"Required: {command.arg_reqs()}. Received: {arg_len}"
            )

        return command, args

    def run(self):
        """Run the CLI."""
        while True:
            try:
                # Get command line input
                line = input("> ")
                # Parse the input
                command, args = self.parse(line)
                # Perform the command
                self.perform(command, args)
            except ValueError as e:
                print(e)
