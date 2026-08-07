# RealFullInstaller

Cross-platform software installer / searcher / uninstaller for macOS & Linux, built on CustomTkinter.

> [中文文档](./README.md)

## Overview

RealFullInstaller is a graphical package management tool built with Python + CustomTkinter. It lets you search, install, and uninstall software on macOS / Linux with a single click, automatically adapting to the **brew** (macOS) and **apt** (Linux) package managers.

- Graphical UI — no commands to memorize
- One-click support for **brew (macOS)** and **apt (Linux)**
- Search, install, and uninstall software
- Lightweight, clean, ready to use out of the box

## Dependencies

This project depends on:
- `customtkinter`
- `termcolor`

You can use the one-click dependency installers shipped in Releases:
- **Windows**: `install_requirements.bat`
- **macOS / Linux**: `install_requirements.sh`

Or install manually:
```bash
pip install customtkinter termcolor
```

## Platform Notes

- **macOS / Linux**: Run the packaged DMG / ZIP directly
- **Windows**: Cannot run Unix executables — source code only

## Download & Use (Regular Users)

Download the appropriate file from [Releases](../../releases):
- `RealFullInstaller.dmg` (macOS)
- `RealFullInstaller.zip` (Linux)
- `main.py` (source for all platforms)
- `install_requirements.bat` (Windows one-click dependency installer)
- `install_requirements.sh` (macOS / Linux one-click dependency installer)

## Run from Source (All Platforms)

1. Clone the repository
```bash
git clone https://github.com/adksetup/real-full-installer.git
cd real-full-installer
```

2. Install dependencies
- **Windows**: Double-click `install_requirements.bat`
- **macOS / Linux**: Run `./install_requirements.sh` in a terminal
- Or manually: `pip install customtkinter termcolor`

3. Run the program
```bash
python main.py
```

## Version Info

- Version: v0.2
- Status: Stable
- Supported platforms: macOS / Linux
- Windows: Source code only

## License

Released under the [MIT License](./LICENSE).

## Author

AdkSetup
