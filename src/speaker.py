"""Offline text-to-speech via pyttsx3."""

from __future__ import annotations

import pyttsx3


def _engine(rate: int = 175):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)  # words per minute
    return engine


def speak(text: str, rate: int = 175) -> None:
    """Read text aloud through the system speakers."""
    engine = _engine(rate)
    engine.say(text)
    engine.runAndWait()


def save_audio(text: str, output_path: str, rate: int = 175) -> None:
    """Render text to an audio file instead of speaking it."""
    engine = _engine(rate)
    engine.save_to_file(text, output_path)
    engine.runAndWait()
