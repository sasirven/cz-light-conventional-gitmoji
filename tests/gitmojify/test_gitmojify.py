"""
This module tests the `mojify` module in the `gitmojify` package.
"""

import re
from pathlib import Path
from typing import Optional
from unittest import mock

import pytest

from gitmojify import mojify
from shared.gitmojis import GitMojiConstant as mojisicon
from shared.spec import mojis


def test_grouped_gitmojis() -> None:
    """Verify gitmojis are grouped correctly."""
    grouped_gitmojis = mojify.grouped_gitmojis()
    assert isinstance(grouped_gitmojis, dict)
    assert len(grouped_gitmojis) == len(mojis)


@pytest.mark.parametrize(
    ["message_in", "message_out"],
    [
        (
            "feat: some new feature",
            f"feat: {mojisicon.GJ_FEAT.value} some new feature",
        ),
        (
            "docs(readme): add a section",
            f"docs(readme): {mojisicon.GJ_DOCS.value} add a section",
        ),
        (
            "refactor(FooClass)!: rename foo.bar -> foo.baz\n\n"
            "BREAKING CHANGE: this breaks stuff",
            f"refactor(FooClass)!: {mojisicon.GJ_REFACTOR.value} "
            f"rename foo.bar -> foo.baz\n\nBREAKING CHANGE: this breaks stuff",
        ),
        (
            "test(foo-tests): add some tests for foo\n\n"
            "Add new tests for foo.bar and foo.baz.",
            f"test(foo-tests): {mojisicon.GJ_TEST.value} "
            f"add some tests for foo\n\n"
            f"Add new tests for foo.bar and foo.baz.",
        ),
    ],
)
def test_gitmojify(message_in: str, message_out: str) -> None:
    """Verify the correct icon is prepended to the message."""
    assert mojify.gitmojify(message_in) == message_out


@pytest.fixture(name="message")
def fixture_message() -> str:
    """Return a commit message."""
    return "feat: some new feature"


@pytest.fixture(name="modified_message")
def fixture_modified_message(message: str) -> Optional[str]:
    """Return the modified commit message or None if not matched."""
    pattern = re.compile(r"([a-zA-Z]+)(\(\S+\))?!?:")
    match = pattern.match(message)
    if match:
        gtype = match.group(1)
        scope = match.group(2) if match.group(2) else ""
        return (
            f"{gtype}{scope}: {mojisicon.GJ_FEAT.value}{message[match.end():]}"
        )
    return None


def test_run_file(
    tmp_path: Path, message: str, modified_message: Optional[str]
) -> None:
    """Verify the commit message is modified."""
    filepath = tmp_path / "commit-msg"
    filepath.write_text(message)
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=mock.MagicMock(
            commit_msg_file=filepath.as_posix(), message=None
        ),
    ):
        mojify.run()

    if modified_message:
        assert filepath.read_text(encoding="utf-8") == modified_message
    else:
        assert False, "Message format is invalid"


def test_run_message(
    message: str,
    modified_message: Optional[str],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Verify the commit message is modified."""
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=mock.MagicMock(commit_msg_file=None, message=message),
    ):
        mojify.run()
    captured = capsys.readouterr()
    assert captured.out == modified_message
