# RealFullInstaller
macOS / Linux 软件安装/搜索/卸载工具 | 基于 CustomTkinter

> [English Documentation](./README.en.md) | 中文文档

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

## 开源协议
本项目基于 [MIT License](./LICENSE) 开源。

## 作者
AdkSetup
