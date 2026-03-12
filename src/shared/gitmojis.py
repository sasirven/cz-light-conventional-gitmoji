"""Contains the Gitmoji constants."""

from enum import Enum

__all__ = ["GitMojiConstant"]


class GitMojiConstant(Enum):
    """Enum class for Gitmojis."""

    GJ_FIX = "🐛"
    GJ_REVERT = "⏪️"
    GJ_FEAT = "✨"
    GJ_DOCS = "📝"
    GJ_STYLE = "🎨"
    GJ_REFACTOR = "♻️"
    GJ_PERF = "⚡️"
    GJ_TEST = "✅"
    GJ_BUILD = "👷"
    GJ_CI = "💚"
    GJ_DUMP = "🔥"
    GJ_HOTFIX = "🚑️"
    GJ_INIT = "🎉"
    GJ_BUMP = "🔖"
    GJ_DEP_DROP = "⬇️"
    GJ_DEP_BUMP = "⬆️"
    GJ_DEP_ADD = "➕"
    GJ_DEP_RM = "➖"
    GJ_CONFIG = "🔧"
    GJ_LANG = "🌐"
    GJ_MERGE = "🔀"
    GJ_LOGS_ADD = "🔊"
    GJ_LOGS_RM = "🔇"
    GJ_IGNORE = "🙈"
    GJ_CHORE = "🧹"
