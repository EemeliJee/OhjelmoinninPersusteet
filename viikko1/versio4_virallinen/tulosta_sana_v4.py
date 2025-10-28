
"""
Käyttö:
    python tulosta_sana_v4.py --tiedosto sana.txt

Paluuarvot:
    0  onnistui
    1  tiedostoa ei löytynyt tai virhe argumenteissa
    2  tiedoston sisältö virheellinen
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path


def read_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read one word from the file and print it."
    )
    parser.add_argument(
        "-t",
        "--file",
        type=Path,
        default=Path("sana.txt"),
        help="File path(default: sana.txt)",
    )
    return parser.parse_args()


def read_one_word(path:Path) -> str:

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    text = path.read_text(encoding="utf-8").strip()
    pattern = re.compile(r"^[\w-]+$", flags=re.UNICODE)

    if not text or not pattern.match(text):
        raise ValueError(
            "The file must include only one word without spaces or symbols."
        )

    return text


def main() -> int:
    args = read_arguments()
    try:
        word = read_one_word(args.file)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# from __future__ import annotations
# import argparse
# import re
# import sys
# from pathlib import Path

# def read_arguments() -> argparse.Namespace:
#     parser = argparse.ArgumentParser(description="Read one word from a file and print it.")
#     parser.add_argument("-t","--file",type=Path,default=Path("sana.txt"), help="File path (default: sana.txt)",)

# def read_one_word(path: Path) -> str:
#     if not path.exists():
#         raise FileNotFoundError(f"File not found: {path}")

#     text = path.read_text(encodinf="uft-8").strip()
#     pattern = re.compile(r"^[\w-]+$", flags=re.UNICODE)

#     if not text or not pattern.match(text):
#         raise ValueError("The file must containt only one word without spaces or symbols.")
#     return text

# def main() -> int:
#       args = read_arguments()
#       try:
#           word = read_one_word(args.file)
#       except FileNotFoundError as e:
#           print(f"Error: {e}", file=sys.stderr)
#           return 1
#       except ValueError as e:
#           print(f"Virhe: {e}", file=sys.stderr)
#           return 2

#       print(word)
#       return 0

# if __name__ == "__main__":
#       sys.exit(main())
