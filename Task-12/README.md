# Task 12 — TimeFlow Wallpaper Sync

## Objective
TimeFlow reads a text file and turns its contents into a desktop wallpaper. The wallpaper also shows a live clock with seconds and is regenerated continuously so edits to the notes file appear on the desktop.

## Files
- `timeflow.py` — application source code
- `requirements.txt` — Python dependency

## Setup
```bash
python3 -m pip install -r requirements.txt
```

## Usage
Create a text file named `notes.txt`, then run:
```bash
python3 timeflow.py notes.txt
```

Press `Ctrl+C` to stop the program.

The program targets GNOME on Linux and also contains basic Windows wallpaper support. The generated image is saved as `timeflow_wallpaper.png`.

## Concepts learned
- Reading and monitoring text files
- Image generation with Pillow
- Dynamic time using `datetime`
- Continuous loops and timed updates
- Setting desktop wallpaper through system APIs

## Required demonstration
Run the application and capture screenshots showing the initial wallpaper, changing clock, and wallpaper after editing `notes.txt`.
