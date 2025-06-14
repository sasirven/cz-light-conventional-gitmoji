"""Conftest to store global fixtures for the tests."""

from typing import Any

import pytest
from _pytest.fixtures import SubRequest
from commitizen import defaults
from commitizen.config.base_config import BaseConfig

from cz_light_gitmoji.main import CommitizenGitmojiCz
from shared.gitmojis import GitMojiConstant as Mojis


@pytest.fixture
def config() -> BaseConfig:
    """Return a BaseConfig instance with the default settings."""
    config_ = BaseConfig()
    config_.settings.update({"name": defaults.name})
    return config_


@pytest.fixture
def cz_gitmoji(config: BaseConfig) -> CommitizenGitmojiCz:
    """
    Return a CommitizenGitmojiCz instance.

    :param config: BaseConfig instance from the config fixture
    :type config: BaseConfig.
    """
    return CommitizenGitmojiCz(config)


@pytest.fixture(
    params=[
        # answers, expected
        (
            {
                "prefix": "docs",
                "scope": "models",
                "subject": f"{mojis.GJ_DOCS.value} person was undocumented",
                "body": (
                    "When no plant of the field was yet in "
                    "the image of God he created them; "
                    "male and female he created them."
                ),
                "is_breaking_change": False,
                "footer": "",
            },
            f"docs(models): {mojis.GJ_DOCS.value} person was undocumented\n\n"
            f"When no plant of the field was yet in the image of God "
            f"he created them; male and female he created them.",
        ),
        (
            {
                "prefix": "refactor",
                "scope": "dto",
                "subject": f"{mojis.GJ_REFACTOR.value} bla bla",
                "body": "The woman said to him, Where are you?",
                "is_breaking_change": True,
                "footer": "BREAKING CHANGE: this breaks stuff",
            },
            f"refactor(dto)!: {mojis.GJ_REFACTOR.value} bla bla\n\n"
            f"The woman said to him, Where are you?"
            f"\n\nBREAKING CHANGE: this breaks stuff",
        ),
        (
            {
                "prefix": "test",
                "scope": "controllers",
                "subject": f"{mojis.GJ_TEST.value} xpto",
                "body": (
                    "So out of the heavens and the earth and the woman, "
                    "and between your offspring and hers; "
                    "he will strike his heel."
                ),
                "is_breaking_change": True,
                "footer": "",
            },
            f"test(controllers)!: {mojis.GJ_TEST.value} xpto\n\n"
            f"So out of the heavens and the earth and the woman, "
            f"and between your offspring and hers; he will strike his heel.",
        ),
        (
            {
                "prefix": "build",
                "scope": "docker",
                "subject": f"{mojis.GJ_BUILD.value} xpto",
                "body": (
                    "He drove out the man; and at the east of the garden "
                    "at the time of the evening breeze, "
                    "and the man and put him in the garden of Eden, "
                    "to till the ground the LORD God walking in "
                    "the image of God he created them; "
                    "male and female he created them."
                ),
                "is_breaking_change": False,
                "footer": "Ref: #1111, #1112, #1113",
            },
            f"build(docker): {mojis.GJ_BUILD.value} xpto\n\n"
            f"He drove out the man; and at the east of the garden at "
            f"the time of the evening breeze, and the man and put him in "
            f"the garden of Eden, to till the ground the LORD God walking in "
            f"the image of God he created them; "
            f"male and female he created them.\n\nRef: #1111, #1112, #1113",
        ),
    ]
)
def messages(request: SubRequest) -> tuple[dict[str, Any], str]:
    """
    Return a tuple with answers and the expected commit message.

    :param request: pytest fixture request object
    :return: tuple with answers and expected commit message
    """
    return request.param
