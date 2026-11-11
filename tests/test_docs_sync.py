"""Docs must match the code: platform table and counts are generated."""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "gen_platform_docs.py"

pytestmark = pytest.mark.skipif(
    not SCRIPT.exists() or not (ROOT / "README.md").exists(),
    reason="repository docs/scripts are not available (e.g. installed package)",
)


@pytest.fixture(scope="module")
def gen():
    spec = importlib.util.spec_from_file_location("gen_platform_docs", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_platform_meta_covers_every_predefined_platform(gen):
    gen.check_meta()  # raises SystemExit with details when out of sync


def test_readme_table_and_counts_are_up_to_date(gen):
    stale = gen.run(check=True)
    assert stale == [], (
        f"Stale files: {stale}. Run `python scripts/gen_platform_docs.py` and commit the result."
    )


def test_count_label_rounds_down_to_five(gen):
    assert gen.count_label(69) == "65+"
    assert gen.count_label(70) == "70+"
    assert gen.count_label(74) == "70+"
