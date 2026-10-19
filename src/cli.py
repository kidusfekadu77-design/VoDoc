"""Command-line interface: document -> text -> speech."""

from __future__ import annotations

import argparse

from .clean import clean_text
from .reader import read_document
from .speaker import save_audio, speak


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read a scanned document aloud (accessibility tool)."
    )
    parser.add_argument("input", help="PDF or image file to read")
    parser.add_argument("--lang", default="eng",
                        help="Tesseract language code (default: eng)")
    parser.add_argument("--speak", action="store_true",
                        help="Read the document aloud")
    parser.add_argument("--save-audio", metavar="FILE",
                        help="Save narration to an audio file instead")
    parser.add_argument("--rate", type=int, default=175,
                        help="Speech rate in words per minute (default: 175)")
    parser.add_argument("--text-only", action="store_true",
                        help="Print extracted text and exit")
    args = parser.parse_args()

    raw, method = read_document(args.input, args.lang)
    text = clean_text(raw)
    print(f"[extracted via {method}: {len(text)} characters]")

    if args.text_only or (not args.speak and not args.save_audio):
        print(text)
        return
    if args.speak:
        speak(text, args.rate)
    if args.save_audio:
        save_audio(text, args.save_audio, args.rate)
        print(f"Saved narration to {args.save_audio}")


if __name__ == "__main__":
    main()
