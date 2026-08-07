# RealFullInstaller

> **简体中文** | **English** — Dual-language documentation

---

[中文文档](#中文文档) | [English Documentation](#english-documentation)

---

<a id="中文文档"></a>

macOS / Linux 软件安装/搜索/卸载工具 | 基于 CustomTkinter
## 项目介绍
RealFullInstaller 是一款基于 Python + CustomTkinter 开发的图形化包管理工具，
支持在 macOS / Linux 上一键搜索、安装、卸载软件，自动适配 brew / apt 包管理器。
- 图形化界面，无需记忆命令
- 一键适配 brew (macOS) / apt (Linux)
- 支持软件搜索、安装、卸载
- 轻量简洁，开箱即用
## 依赖说明
本项目依赖：
- `customtkinter`
- `termcolor`
可使用 Release 中的一键安装脚本：
- **Windows**: `install_requirements.bat`
- **macOS / Linux**: `install_requirements.sh`
手动安装：
```bash
pip install customtkinter termcolor
```
## 平台说明
- **macOS / Linux**：可直接运行打包好的 DMG / ZIP
- **Windows**：无法运行 Unix 可执行文件，仅支持源码运行
## 下载使用（普通用户）
从 Releases 下载对应文件：
- `RealFullInstaller.dmg` (macOS)
- `RealFullInstaller.zip` (Linux)
- `main.py` (全平台源码)
- `install_requirements.bat` (Windows 一键安装依赖)
- `install_requirements.sh` (macOS/Linux 一键安装依赖)
## 源码运行（全平台）
1. 克隆仓库
```bash
git clone https://github.com/adksetup/real-full-installer.git
cd real-full-installer
```
2. 安装依赖
- Windows：双击运行 `install_requirements.bat`
- macOS / Linux：终端执行 `./install_requirements.sh`
- 或手动执行：`pip install customtkinter termcolor`
3. 运行程序
```bash
python main.py
```
## 版本信息
- 版本：v0.2
- 状态：正式版
- 支持平台：macOS / Linux
- Windows：仅支持源码运行
## 作者
AdkSetup

---

<a id="english-documentation"></a>

Cross-platform software installer / searcher / uninstaller for macOS & Linux, built on CustomTkinter.

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
## Author

AdkSetup

---

## License

This project is licensed under the [MIT License](./LICENSE).
