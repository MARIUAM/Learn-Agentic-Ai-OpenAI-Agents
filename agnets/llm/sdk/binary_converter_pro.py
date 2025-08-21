4#!/usr/bin/env python3
"""
Binary Converter Pro
--------------------
A robust CLI + Interactive tool to convert between Text and Binary, with file I/O,
auto-detection, validation, history, and export.

Usage (CLI examples):
  # Text -> Binary
  python binary_converter_pro.py --mode t2b --text "Hello"

  # Binary -> Text
  python binary_converter_pro.py --mode b2t --binary "01001000 01100101 01101100 01101100 01101111"

  # Auto-detect based on input
  python binary_converter_pro.py --auto "01001000 01100101" 

  # Convert a file and save result
  python binary_converter_pro.py --mode t2b --infile notes.txt --outfile notes.bin.txt

  # Export history to JSON/CSV
  python binary_converter_pro.py --export history.json
  python binary_converter_pro.py --export history.csv

Run without arguments to open Interactive Menu.
"""

from __future__ import annotations
import argparse
import json
import csv
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional, Tuple, Iterable

NON_PRINTABLE_PLACEHOLDER = "�"  # used when decoding invalid UTF-8

# ---------------- Core conversion helpers ---------------- #

def text_to_binary(text: str, *, encoding: str = "utf-8") -> str:
    """
    Convert text to space-separated 8-bit binary bytes (UTF-8 by default).
    Multi-byte characters are represented by multiple 8-bit chunks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    b = text.encode(encoding, errors="replace")
    return " ".join(f"{byte:08b}" for byte in b)


def _sanitize_binary_str(binary: str) -> str:
    """
    Accept common separators (space, comma, underscore, dash, newline) and strip them.
    Return a continuous bits string like '01100001...'
    """
    allowed = set("01")
    bits = []
    for ch in binary:
        if ch in ("0", "1"):
            bits.append(ch)
        # ignore common separators silently
        elif ch in (" ", ",", "_", "-", "\n", "\t", "|", "/"):
            continue
        else:
            # invalid char, mark with special token so we can error nicely later
            bits.append("x")
    return "".join(bits)


def chunk_bits(bits: str, width: int = 8) -> List[str]:
    return [bits[i:i+width] for i in range(0, len(bits), width)]


def binary_to_text(binary: str, *, encoding: str = "utf-8") -> str:
    """
    Convert binary (8-bit groups) to text.
    Accepts inputs with spaces/commas/underscores/dashes/newlines or a continuous stream.
    Returns decoded text (UTF-8). Raises ValueError on invalid length or non-binary chars.
    """
    if not isinstance(binary, str):
        raise TypeError("binary must be a string")
    cleaned = _sanitize_binary_str(binary)
    if "x" in cleaned:
        raise ValueError("Invalid character found in binary input. Only 0/1 and separators are allowed.")
    if len(cleaned) == 0:
        return ""

    if len(cleaned) % 8 != 0:
        raise ValueError(f"Bit length must be a multiple of 8. Got {len(cleaned)} bits.")

    bytes_list = [int(b, 2) for b in chunk_bits(cleaned, 8)]
    try:
        return bytes(bytes_list).decode(encoding)
    except UnicodeDecodeError:
        # decode byte-by-byte with replacement to avoid crash
        return bytes(bytes_list).decode(encoding, errors="replace")


def looks_like_binary(s: str, *, threshold: float = 0.9) -> bool:
    """
    Heuristic: if >= threshold fraction of non-separator chars are 0/1, treat as binary.
    """
    if not s:
        return False
    total = sum(1 for ch in s if ch not in (" ", ",", "_", "-", "\n", "\t", "|", "/"))
    if total == 0:
        return False
    ones_zeros = sum(1 for ch in s if ch in ("0", "1"))
    return (ones_zeros / total) >= threshold


# ---------------- History & records ---------------- #

@dataclass
class Record:
    timestamp: str
    mode: str          # "t2b" or "b2t" or "auto"
    input_preview: str
    output_preview: str
    input_len: int
    output_len: int

class History:
    def __init__(self):
        self._items: List[Record] = []

    def add(self, mode: str, input_text: str, output_text: str):
        ts = datetime.now().isoformat(timespec="seconds")
        rec = Record(
            timestamp=ts,
            mode=mode,
            input_preview=(input_text[:80] + ("…" if len(input_text) > 80 else "")),
            output_preview=(output_text[:80] + ("…" if len(output_text) > 80 else "")),
            input_len=len(input_text),
            output_len=len(output_text),
        )
        self._items.append(rec)

    def to_json(self) -> str:
        return json.dumps([asdict(r) for r in self._items], ensure_ascii=False, indent=2)

    def export_json(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    def export_csv(self, path: str):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["timestamp","mode","input_preview","output_preview","input_len","output_len"])
            w.writeheader()
            for r in self._items:
                w.writerow(asdict(r))

    def __len__(self):
        return len(self._items)

    def tail(self, n: int = 10) -> List[Record]:
        return self._items[-n:]


HISTORY = History()


# ---------------- File processing ---------------- #

def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def convert_file(infile: str, outfile: str, mode: str) -> Tuple[int, int]:
    """
    Convert infile -> outfile according to mode ("t2b" or "b2t").
    Returns tuple of (input_chars, output_chars).
    """
    data = read_text_file(infile)
    if mode == "t2b":
        out = text_to_binary(data)
    elif mode == "b2t":
        out = binary_to_text(data)
    else:
        raise ValueError("mode must be 't2b' or 'b2t'")
    write_text_file(outfile, out)
    HISTORY.add(mode, data, out)
    return (len(data), len(out))


# ---------------- Interactive menu ---------------- #

def interactive_menu():
    print("=== Binary Converter Pro ===")
    print("1) Text → Binary")
    print("2) Binary → Text")
    print("3) Auto-detect (smart)")
    print("4) Convert a FILE")
    print("5) Show recent history")
    print("6) Export history (JSON/CSV)")
    print("0) Exit")

    while True:
        choice = input("\nApni choice select karo (0-6): ").strip()

        if choice == "1":
            text = input("\nText likho: ")
            out = text_to_binary(text)
            print("\nBinary:")
            print(out)
            HISTORY.add("t2b", text, out)

        elif choice == "2":
            binary = input("\nBinary likho (8-bit, spaces optional; commas/dashes allowed):\n")
            try:
                out = binary_to_text(binary)
                print("\nText:")
                print(out)
                HISTORY.add("b2t", binary, out)
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            data = input("\nApna input do (Text ya Binary):\n")
            if looks_like_binary(data):
                mode = "b2t"
                try:
                    out = binary_to_text(data)
                except ValueError as e:
                    print(f"❌ Error: {e}")
                    continue
                print("\nDetected: Binary → Text")
                print(out)
            else:
                mode = "t2b"
                out = text_to_binary(data)
                print("\nDetected: Text → Binary")
                print(out)
            HISTORY.add("auto", data, out)

        elif choice == "4":
            print("\nFile Convert:")
            mode = input("Mode choose karo ('t2b' ya 'b2t'): ").strip().lower()
            infile = input("Input file path: ").strip().strip('"')
            outfile = input("Output file path: ").strip().strip('"')
            try:
                in_len, out_len = convert_file(infile, outfile, mode)
                print(f"✅ Done! {in_len} chars → {out_len} chars\nSaved to: {outfile}")
            except FileNotFoundError:
                print("❌ File nahi mili. Sahi path do.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "5":
            print("\n--- Recent History ---")
            for r in HISTORY.tail(10):
                print(f"[{r.timestamp}] {r.mode.upper()} | in:{r.input_len} out:{r.output_len}")
                print(f"  IN : {r.input_preview}")
                print(f"  OUT: {r.output_preview}")
            if len(HISTORY) == 0:
                print("(empty)")

        elif choice == "6":
            path = input("File name do (history.json ya history.csv): ").strip()
            if path.lower().endswith(".json"):
                HISTORY.export_json(path)
                print(f"✅ Exported JSON → {path}")
            elif path.lower().endswith(".csv"):
                HISTORY.export_csv(path)
                print(f"✅ Exported CSV → {path}")
            else:
                print("❌ Extension invalid. .json ya .csv use karo.")

        elif choice == "0":
            print("Bye! 👋")
            break
        else:
            print("❌ Galat option. 0-6 try karo.")


# ---------------- CLI ---------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Binary Converter Pro - Text/Binary converter with file support.")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--mode", choices=["t2b", "b2t"], help="Conversion mode")
    g.add_argument("--auto", metavar="INPUT", help="Auto-detect and convert this input (text or binary)")
    p.add_argument("--text", help="Text input for t2b (ignored if --binary provided)")
    p.add_argument("--binary", help="Binary input for b2t (ignored if --text provided)")
    p.add_argument("--infile", help="Read input from file (text)")
    p.add_argument("--outfile", help="Write output to file")
    p.add_argument("--export", help="Export history to JSON/CSV")
    p.add_argument("--print", action="store_true", help="Print the result to stdout")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Export-only shortcut
    if args.export:
        if args.export.lower().endswith(".json"):
            HISTORY.export_json(args.export)
            print(f"✅ Exported JSON → {args.export}")
            return 0
        elif args.export.lower().endswith(".csv"):
            HISTORY.export_csv(args.export)
            print(f"✅ Exported CSV → {args.export}")
            return 0
        else:
            print("❌ --export requires .json or .csv")
            return 1

    # If no args: interactive menu
    if not any([args.mode, args.auto, args.text, args.binary, args.infile, args.outfile]):
        interactive_menu()
        return 0

    # Auto-detect path
    if args.auto is not None:
        data = args.auto
        if looks_like_binary(data):
            mode = "b2t"
            try:
                out = binary_to_text(data)
            except ValueError as e:
                print(f"❌ Error: {e}")
                return 1
        else:
            mode = "t2b"
            out = text_to_binary(data)
        HISTORY.add("auto", data, out)
        if args.outfile:
            write_text_file(args.outfile, out)
            print(f"✅ Saved → {args.outfile}")
        if args.print or not args.outfile:
            print(out)
        return 0

    # Mode-based path
    if not args.mode:
        print("❌ Specify --mode t2b|b2t or use --auto.")
        return 1

    # Decide input source
    data = None
    if args.infile:
        try:
            data = read_text_file(args.infile)
        except FileNotFoundError:
            print("❌ Input file nahi mili.")
            return 1
    elif args.text and args.mode == "t2b":
        data = args.text
    elif args.binary and args.mode == "b2t":
        data = args.binary
    else:
        # Fallback: read from stdin
        try:
            data = sys.stdin.read()
        except Exception as e:
            print(f"❌ Could not read stdin: {e}")
            return 1

    # Perform conversion
    try:
        if args.mode == "t2b":
            out = text_to_binary(data)
        else:
            out = binary_to_text(data)
    except ValueError as e:
        print(f"❌ Error: {e}")
        return 1

    HISTORY.add(args.mode, data, out)

    # Output destination
    if args.outfile:
        write_text_file(args.outfile, out)
        print(f"✅ Saved → {args.outfile}")
    if args.print or not args.outfile:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
