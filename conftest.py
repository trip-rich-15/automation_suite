import pytest


def pytest_bdd_apply_tag(tag, function):
    # Scenarios tagged with @known_bug_<ID> are marked as expected failures.
    # strict=True makes the test fail if it passes, so a fixed bug is not missed.
    if tag.startswith("known_bug_"):
        bug_id = tag.removeprefix("known_bug_")
        pytest.mark.xfail(reason=f"Known defect {bug_id}", strict=True)(function)
        return True
    return None
