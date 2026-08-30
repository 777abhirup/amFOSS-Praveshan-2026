import os
import sys
import time
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

try:
    import ctypes
except ImportError:
    ctypes = None

WIDTH, HEIGHT = 1920, 1080
OUTPUT = Path("timeflow_wallpaper.png")


def get_font(size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def read_notes(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "Create notes.txt to add your plan or schedule."


def generate_wallpaper(text, output=OUTPUT):
    image = Image.new("RGB", (WIDTH, HEIGHT), (18, 18, 24))
    draw = ImageDraw.Draw(image)
    title_font = get_font(52)
    body_font = get_font(34)
    time_font = get_font(86)

    draw.text((90, 70), "TIMEFLOW", font=title_font, fill=(235, 235, 245))
    draw.text((90, 170), "Your notes", font=body_font, fill=(150, 155, 170))

    y = 245
    for line in text.splitlines() or [""]:
        draw.text((90, y), line, font=body_font, fill=(225, 225, 235))
        y += 52
        if y > HEIGHT - 180:
            break

    now = datetime.now().strftime("%H:%M:%S")
    draw.text((WIDTH - 560, HEIGHT - 150), now, font=time_font, fill=(245, 245, 250))
    image.save(output)
    return output


def set_wallpaper(path):
    path = str(Path(path).resolve())
    if sys.platform.startswith("linux"):
        # GNOME is the primary target. Other desktop environments can use the generated PNG manually.
        os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}' >/dev/null 2>&1")
        os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{path}' >/dev/null 2>&1")
    elif sys.platform.startswith("win") and ctypes:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)


def main():
    notes = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("notes.txt")
    print(f"Watching {notes.resolve()}")
    print("Press Ctrl+C to stop.")
    last_content = None
    while True:
        content = read_notes(notes)
        # Regenerate every second so the displayed clock includes seconds.
        if content != last_content:
            last_content = content
        generate_wallpaper(content)
        set_wallpaper(OUTPUT)
        time.sleep(1)


if __name__ == "__main__":
    main()
