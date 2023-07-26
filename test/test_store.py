from cli.store import CLIStore
import pytest


def test_cli_store_num_parse():
    store = CLIStore()
    store["a"] = "1"
    store["b"] = "2.25"
    store["c"] = "three"
    assert store["a"] == 1
    assert store["b"] == 2.25
    assert store["c"] == "three"
    assert store["d"] is None


def test_cli_store_get_error_star():
    store = CLIStore()
    store["a"] = "1"
    with pytest.raises(ValueError):
        store["*"]


def test_cli_store_set_error_star():
    store = CLIStore()
    with pytest.raises(ValueError):
        store["*"] = "1"


@pytest.mark.parametrize(
    "k, v",
    [
        ("a", "three"),
        ("a", "2.25"),
        ("b", "1"),
        ("b", "three"),
        ("c", "1"),
        ("c", "2.25"),
    ],
)
def test_cli_store_set_error_type(k, v):
    store = CLIStore()
    store["a"] = "1"
    store["b"] = "2.25"
    store["c"] = "three"
    with pytest.raises(ValueError):
        store[k] = v


@pytest.mark.parametrize(
    "k, v, expected",
    [
        ("a", "3", 3),
        ("a", "2", 2),
        ("b", "1.11", 1.11),
        ("b", "3.14", 3.14),
        ("c", "one", "one"),
        ("c", "two", "two"),
    ],
)
def test_cli_store_set_success(k, v, expected):
    store = CLIStore()
    store["a"] = "1"
    store["b"] = "2.25"
    store["c"] = "three"
    store[k] = v
    assert store[k] == expected
