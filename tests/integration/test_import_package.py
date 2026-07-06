"""Import smoke tests for the package."""

import repo_guard


def test_package_exposes_version() -> None:
    """The package exposes a stable version string."""
    assert repo_guard.__version__ == "0.1.0"
