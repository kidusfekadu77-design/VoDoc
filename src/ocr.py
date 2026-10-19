"""OCR wrapper around Tesseract."""

from __future__ import annotations

from PIL import Image

import pytesseract


def ocr_image(image: Image.Image, lang: str = "eng") -> str:
    """Run Tesseract OCR on a PIL image.

    lang: Tesseract language code, e.g. "eng". Tesseract ships many more
    ("amh" for Amharic included) — see the roadmap in README.md.
    """
    if image.mode != "L":
        image = image.convert("L")  # grayscale improves OCR accuracy
    return pytesseract.image_to_string(image, lang=lang)
