# VoDoc

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/OCR-Tesseract-5B7CFA?logo=tesseract&logoColor=white" alt="Tesseract OCR" />
</p>

VoDoc converts scanned PDFs and photos of documents into spoken audio, making reading more accessible for visually impaired users. It tries the PDF's embedded text first, then falls back to OCR when needed, and reads the cleaned text aloud using offline text-to-speech.

## Why VoDoc?

- Reads scanned documents and pages from images/PDFs
- Uses PDF text extraction first for speed and accuracy
- Falls back to Tesseract OCR for image-based or scanned content
- Cleans extracted text before speaking it aloud
- Works fully offline with no API keys required

## Features

- Hybrid extraction pipeline: embedded PDF text first, OCR fallback
- Tesseract-powered OCR for photos and scanned pages
- Language-aware OCR support, including Amharic via `--lang amh`
- Text cleanup for hyphenation, spacing, and noise reduction
- Offline speech synthesis with adjustable reading speed
- Audio export to a file in addition to live playback
- Clear reporting of extraction method and character count

## Demo

```bash
python -m src.cli sample.pdf --text-only
```

Example output:

```text
[extracted via text-layer: 339 characters]
Accessible Document Reader - sample document. This PDF has a real text layer, so the reader extracts it directly without needing OCR...
```

```bash
python -m src.cli sample-scanned.pdf --speak
```

```text
[extracted via ocr: 412 characters]
# 🔊 your computer reads the page aloud
```

```bash
python -m src.cli lecture-notes.pdf --save-audio lecture-notes.aiff --rate 190
```

```text
[extracted via ocr: 5210 characters]
Saved narration to lecture-notes.aiff
```

## Installation

### 1) System dependencies

On macOS:

```bash
brew install tesseract tesseract-lang poppler
```

On Ubuntu/Debian:

```bash
sudo apt install tesseract-ocr tesseract-ocr-eng poppler-utils
```

### 2) Python dependencies

```bash
pip install -r requirements.txt
```

## Usage

Print extracted text:

```bash
python -m src.cli document.pdf --text-only
```

Read aloud at the default speed:

```bash
python -m src.cli document.pdf --speak
```

Read more quickly:

```bash
python -m src.cli document.pdf --speak --rate 200
```

Save narration as audio:

```bash
python -m src.cli document.pdf --save-audio narration.aiff
```

OCR a photo of a page in Amharic:

```bash
python -m src.cli page.jpg --speak --lang amh
```

Try the included samples:

- `sample.pdf` — PDF with a text layer
- `sample-scanned.pdf` — scanned document that uses OCR fallback

## How it works

```text
PDF / image ──▶ reader.py ──▶ clean.py ──▶ speaker.py ──▶ 🔊 / audio file
                 │ text-layer     │ de-hyphenate   │ pyttsx3 (live)
                 │ first, OCR     │ normalize      │ `say` (file, macOS)
                 │ fallback       │ whitespace     │
```

Each module focuses on one responsibility, which keeps the project easy to test and extend. For a deeper walkthrough, see `CODE_WALKTHROUGH.md`.

## Project structure

```text
VoDoc/
├── src/
│   ├── cli.py        # command-line interface
│   ├── reader.py     # document loading and extraction pipeline
│   ├── ocr.py        # Tesseract wrapper
│   ├── clean.py      # text normalization for speech
│   └── speaker.py    # offline TTS + audio export
├── tests/
│   └── test_clean.py
├── sample.pdf
├── sample-scanned.pdf
├── CODE_WALKTHROUGH.md
├── requirements.txt
├── LICENSE
└── README.md
```

## Roadmap

- [ ] Amharic end-to-end OCR + spoken voice support
- [ ] Chapter chunking for long documents with a spoken table of contents
- [ ] Confidence-based re-OCR for low-quality scans
- [ ] Web UI for upload-and-listen workflows

## Tech stack

- Python
- Tesseract OCR
- pyttsx3
- pypdf
- pdf2image
- Pillow


