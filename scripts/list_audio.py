from pathlib import Path

AUDIO_EXTS = {".wav", ".mp3", ".flac", ".aiff", ".aif", ".m4a", ".ogg"}


folder = Path(".")  # carpeta actual
for p in folder.iterdir():
    if p.is_file() and p.suffix.lower() in AUDIO_EXTS:
        print(p.name)

