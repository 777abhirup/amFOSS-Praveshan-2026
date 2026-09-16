import os
import sys
import time
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1920
HEIGHT = 1080
NOTES_FILE = Path("notes.txt")
OUTPUT_FILE = Path("timeflow_wallpaper.png")


def get_font(size):
    """Return an available font."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]

    for font_path in font_paths:
        if Path(font_path).exists():
            return ImageFont.truetype(font_path, size)

    return ImageFont.load_default()


def read_notes():
    """Read the contents of notes.txt."""
    try:
        return NOTES_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "Create notes.txt to add your plan or schedule."


def generate_wallpaper(text):
    """Create the wallpaper image with notes and current time."""
    image = Image.new("RGB", (WIDTH, HEIGHT), (18, 18, 24))
    draw = ImageDraw.Draw(image)

    title_font = get_font(52)
    body_font = get_font(34)
    time_font = get_font(86)

    draw.text(
        (90, 70),
        "TIMEFLOW",
        font=title_font,
        fill=(235, 235, 245),
    )

    draw.text(
        (90, 170),
        "Your notes",
        font=body_font,
        fill=(150, 155, 170),
    )

    y = 245

    lines = text.splitlines()

    if not lines:
        lines = [""]

    for line in lines:
        draw.text(
            (90, y),
            line,
            font=body_font,
            fill=(225, 225, 235),
        )

        y += 52

        if y > HEIGHT - 180:
            break

    current_time = datetime.now().strftime("%H:%M:%S")

    draw.text(
        (WIDTH - 560, HEIGHT - 150),
        current_time,
        font=time_font,
        fill=(245, 245, 250),
    )

    image.save(OUTPUT_FILE)


def set_wallpaper():
    """Set the generated image as the desktop wallpaper."""
    wallpaper_path = OUTPUT_FILE.resolve()

    if sys.platform.startswith("linux"):
        path_uri = f"file://{wallpaper_path}"

        os.system(
            f"gsettings set org.gnome.desktop.background picture-uri "
            f"'{path_uri}' >/dev/null 2>&1"
        )

        os.system(
            f"gsettings set org.gnome.desktop.background picture-uri-dark "
            f"'{path_uri}' >/dev/null 2>&1"
        )

    elif sys.platform.startswith("win"):
        import ctypes

        ctypes.windll.user32.SystemParametersInfoW(
            20,
            0,
            str(wallpaper_path),
            3,
        )

    else:
        print("Unsupported operating system.")


def main():
    print(f"Watching: {NOTES_FILE.resolve()}")
    print("Press Ctrl+C to stop.")

    last_content = None
    last_time = None

    try:
        while True:
            content = read_notes()
            current_time = datetime.now().strftime("%H:%M:%S")

            # Update when the notes change or the clock changes.
            if content != last_content or current_time != last_time:
                generate_wallpaper(content)
                set_wallpaper()

                last_content = content
                last_time = current_time

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nTimeFlow stopped.")


if __name__ == "__main__":
    main()