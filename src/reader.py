"""Document loading: PDFs (text layer first, OCR fallback) and images."""

from __future__ import annotations

from pathlib import Path

from PIL import Image
from pypdf import PdfReader

from .ocr import ocr_image

SUPPORTED_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp"}


def load_pdf_text_layer(path: Path) -> str | None:
    """Extract text from a PDF's embedded text layer.

    Returns the text if the PDF has a usable text layer, otherwise None so
    the caller can fall back to OCR.
    """
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(pages).strip()
    # A scanned PDF may technically "extract" a few stray characters; require
    # a meaningful amount of text before trusting the text layer.
    if len(text) < 100:
        return None
    return text


def rasterise_pdf(path: Path, dpi: int = 300) -> list[Image.Image]:
    """Render each PDF page to a PIL image for OCR."""
    from pdf2image import convert_from_path

    return convert_from_path(str(path), dpi=dpi)


def read_document(path: str | Path, ocr_lang: str = "eng") -> tuple[str, str]:
    """Read a document file and return (text, method_used).

    method_used is "text-layer" or "ocr" — useful to report to the user.
    Raises FileNotFoundError for missing files, ValueError for bad types.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No such file: {path}")

    ext = path.suffix.lower()
    if ext == ".pdf":
        text = load_pdf_text_layer(path)
        if text is not None:
            return text, "text-layer"
        images = rasterise_pdf(path)
        return "\n\n".join(ocr_image(img, ocr_lang) for img in images), "ocr"
    if ext in SUPPORTED_IMAGE_EXTS:
        return ocr_image(Image.open(path), ocr_lang), "ocr"
    raise ValueError(f"Unsupported file type: {ext} (try .pdf, .png, .jpg)")
