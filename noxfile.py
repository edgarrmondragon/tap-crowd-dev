"""Nox configuration."""

from __future__ import annotations

import os
import sys
from textwrap import dedent

import nox

try:
    from nox_poetry import Session, session
except ImportError:
    message = f"""\
    Nox failed to import the 'nox-poetry' package.
    Please install it using the following command:
    {sys.executable} -m pip install nox-poetry"""
    raise SystemExit(dedent(message)) from None

package = "tap-crowd-dev"
src_dir = "tap_crowd_dev"
tests_dir = "tests"

python_versions = ["3.11", "3.10", "3.9", "3.8", "3.7"]
main_python_version = "3.10"
locations = src_dir, tests_dir, "noxfile.py"
nox.options.sessions = ("tests",)


@session(python=python_versions)
def tests(session: Session) -> None:
    """Execute pytest tests."""
    deps = ["pytest", "pytest-durations"]
    if "GITHUB_ACTIONS" in os.environ:
        deps.append("pytest-github-actions-annotate-failures")

    session.install(".")
    session.install(*deps)
    session.run("pytest", *session.posargs)
