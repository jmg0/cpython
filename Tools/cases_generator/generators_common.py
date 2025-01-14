from pathlib import Path
from typing import TextIO

ROOT = Path(__file__).parent.parent.parent
DEFAULT_INPUT = (ROOT / "Python/bytecodes.c").absolute()


def root_relative_path(filename: str) -> str:
    return Path(filename).relative_to(ROOT).as_posix()


def write_header(generator: str, source: str, outfile: TextIO) -> None:
    outfile.write(
        f"""// This file is generated by {root_relative_path(generator)}
// from:
//   {source}
// Do not edit!
"""
    )
