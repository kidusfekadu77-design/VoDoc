"""Text cleanup: turn raw OCR output into something pleasant to hear."""

from __future__ import annotations

import re


def clean_text(raw: str) -> str:
    """Normalise OCR output for speech.

    - Joins words split by end-of-line hyphens ("docu-\\nment" -> "document")
    - Collapses newlines inside paragraphs to spaces
    - Collapses repeated whitespace
    """
    text = raw.replace("-\n", "")          # de-hyphenate
    text = text.replace("\n", " ")          # one flowing paragraph...
    text = re.sub(r"\s+", " ", text)        # ...without double spaces
    return text.strip()
