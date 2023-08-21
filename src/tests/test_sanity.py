import pytest
from click.testing import CliRunner
from pathlib import Path
import os
from time import time
from typing import List

from src.search_cli import search_files


def tmp_files() -> List[str]:
    return ["one.txt", "two.txt", "word.doc"]


@pytest.fixture(name="tmp_test_dir")
def fixture_tmp_test_dir(tmp_path) -> str:
    test_dir_path = os.path.join(tmp_path, f"test_dir_{time()}")
    os.mkdir(test_dir_path)
    print(f"new directory generated {test_dir_path}")
    for f in tmp_files():
        file_path = os.path.join(test_dir_path, f)
        with open(file_path, "wb") as f:
            print(f"new file generated: {file_path}")
    yield test_dir_path


class TestSanity:
    def test_command(self, tmp_test_dir: str):
        runner = CliRunner()
        results = runner.invoke(
            search_files, ["--path", tmp_test_dir, "--ftype", "txt"]
        )
        assert results.exit_code == 0, "Failed to run command"
        txt_files = filter(lambda path: Path(path).suffix == "txt", tmp_files())
        for f in txt_files:
            assert f in results.output
