from cli.cli import CLI
from cli.command import Command
import pytest
from unittest.mock import patch, call


@pytest.mark.parametrize(
    "k, v",
    [
        ("a", 1),
        ("b", 2.25),
        ("c", "three"),
    ],
)
@patch("builtins.print")
def test__get(mock_print, k, v):
    cli = CLI()
    cli.store[k] = v
    cli._get([k])
    mock_print.assert_called_once_with(v)


@patch("builtins.print")
def test__get_star(mock_print):
    cli = CLI()
    cli.store["a"] = "1"
    cli.store["b"] = "2.25"
    cli.store["c"] = "three"
    cli._get(["*"])
    assert mock_print.mock_calls == [call("a=1"), call("b=2.25"), call("c=three")]


@patch("builtins.print")
def test__get_none(mock_print):
    cli = CLI()
    cli._get(["a"])
    mock_print.assert_called_once_with(None)


def test__set():
    cli = CLI()
    cli._set(["a", "1"])
    assert cli.store["a"] == 1


def test__set_error():
    cli = CLI()
    with pytest.raises(ValueError):
        cli._set(["*", "1"])


def test_parse():
    cli = CLI()
    assert cli.parse("GET a") == (Command.GET, ["a"])
    assert cli.parse("SET a=1") == (Command.SET, ["a", "1"])
    assert cli.parse("EXIT") == (Command.EXIT, [])
    assert cli.parse("") == (Command.NOOP, [])
    assert cli.parse("  ") == (Command.NOOP, [])


@patch("builtins.print")
def test_perform(mock_print):
    cli = CLI()
    cli.perform(Command.SET, ["a", "1"])
    assert cli.store["a"] == 1
    cli.perform(Command.GET, ["a"])
    mock_print.assert_called_with(1)
    cli.perform(Command.GET, ["*"])
    mock_print.assert_called_with("a=1")
