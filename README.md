Vodoc
[!Python](https://www.python.org/)
[!License: MIT](LICENSE)
[!OCR](https://github.com/tesseract-ocr/tesseract)
Turn scanned documents into narrated audio — an accessibility tool for visually impaired readers.
VoDoc takes a PDF or a photo of a page, extracts the text (fast text-layer parsing first, Tesseract OCR fallback for scanned pages), cleans it up, and reads it aloud — or saves the narration as an audio file. It grew out of volunteer work with the Ethiopian National Association for the Blind, where I saw how much of daily life is gated behind documents some people can't read.

Demo
$ python -m src.cli sample.pdf --text-only
[extracted via text-layer: 339 characters]
Accessible Document Reader - sample document. This PDF has a real text
layer, so the reader extracts it directly without needing OCR...

$ python -m src.cli sample-scanned.pdf --speak
[extracted via ocr: 412 characters]
# 🔊 your computer reads the page aloud

$ python -m src.cli lecture-notes.pdf --save-audio lecture-notes.aiff --rate 190
[extracted via ocr: 5210 characters]
Saved narration to lecture-notes.aiff
Features
Hybrid text extraction — tries the PDF's embedded text layer first (fast, exact); falls back to OCR automatically for scanned pages
OCR via Tesseract — handles photos and scans; language-configurable (--lang amh for Amharic, and 100+ more)
Text cleanup — de-hyphenates line breaks, collapses whitespace, strips noise
Offline text-to-speech — no API keys, no network, no cost; adjustable reading rate
Audio export — save narration to a file instead of playing it
Transparent pipeline — every run reports which extraction method was used and how much text was found
Installation
1. System dependencies (outside Python — pip can't install these):
# macOS
brew install tesseract tesseract-lang poppler

# Ubuntu / Debian
sudo apt install tesseract-ocr tesseract-ocr-eng poppler-utils
Tool
Job
Tesseract
Reads text out of images (the OCR engine)
poppler
Renders PDF pages into images for OCR
2. Python packages:
pip install -r requirements.txt
Usage
# Print extracted text
python -m src.cli document.pdf --text-only

# Read aloud (default 175 words/min)
python -m src.cli document.pdf --speak

# Read aloud faster
python -m src.cli document.pdf --speak --rate 200

# Save narration to audio (AIFF on macOS, MP3 elsewhere)
python -m src.cli document.pdf --save-audio narration.aiff

# OCR a photo of a page, in Amharic
python -m src.cli page.jpg --speak --lang amh
Try it with the included samples: sample.pdf (text layer) and sample-scanned.pdf (OCR path).
How it works
PDF / image ──▶  reader.py  ──▶  clean.py  ──▶  speaker.py  ──▶  🔊 / audio file
                  │ text-layer     │ de-hyphenate   │ pyttsx3 (live)
                  │ first, OCR     │ normalise      │ `say` (file, macOS)
                  │ fallback       │ whitespace     │
Each module does one job and knows nothing about the others — the pattern
that makes the code easy to test and extend. See
CODE_WALKTHROUGH.md for a full file-by-file breakdown
and a guide to rebuilding it from scratch.
Project structure
vodoc/
├── src/
│   ├── cli.py        # command-line interface (argparse)
│   ├── reader.py     # document loading: text layer → OCR fallback
│   ├── ocr.py        # Tesseract wrapper
│   ├── clean.py      # text normalisation for speech
│   └── speaker.py    # offline TTS + audio export
├── tests/
│   └── test_clean.py
├── sample.pdf            # text-layer sample
├── sample-scanned.pdf    # OCR-path sample
└── CODE_WALKTHROUGH.md   # deep-dive documentation
Roadmap
[ ] Amharic end-to-end: amh OCR + Amharic TTS voice
[ ] Chapter chunking for long documents with a spoken table of contents
[ ] Confidence-based re-OCR: flag low-confidence words for review
[ ] Web UI (upload → listen) for non-technical users
Tech stack
Python · Tesseract OCR · pyttsx3 · pypdf · pdf2image · Pillow
License
MIT — see LICENSE.
