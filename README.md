# Taskbar Color Picker / 任务栏取色器

一个轻量、无界面、只在任务栏显示的极简屏幕取色工具

<img width="274" height="47" alt="ScreenShot_2026-02-24_125803_403" src="https://github.com/user-attachments/assets/8c8a3593-cc1b-42d6-b280-a51767c876ea" />

## ⭐ 简介 | Overview

-  打开即运行，无窗口、无广告、无多余操作
-  随时鼠标中键一键取色，无需按多余按钮
-  颜色值自动复制到剪贴板
-  任务栏实时显示颜色代码

## ⭐ 运行环境 | Environment

- **操作系统**：Windows 10/11
- **架构**：x86 /x64 通用
- **py依赖库**：ctypes、threading、time、 pystray、pyperclip、PIL


## ⭐ 使用方法 | How to use

1. **双击运行**
2. **观察任务栏**：
   - 出现多个空白图标代表启动成功
     
     <img width="199" height="40" alt="ScreenShot_2026-02-24_132324_456" src="https://github.com/user-attachments/assets/38eea9ba-b652-4cbc-96d2-5999e8bf8b9b" />

   - 如果没显示，请到右下角隐藏托盘区找到图标，拖到任务栏显示
     
     <img width="201" height="169" alt="a6ad476b24f29d15fe57a09fdf01bb10" src="https://github.com/user-attachments/assets/dd36ee28-db33-4f0d-8ebb-7bc0969c8b83" />

3. **将鼠标移动到想要取色的位置**：
4. **按一下鼠标中键**
5. **颜色值会自动显示在任务栏，并复制到剪贴板**


## ⭐ 如何关闭 | How to close

本软件无关闭按钮，属于常驻型小工具。如需退出：

1. **打开 任务管理器**：
2. **找到TaskbarColorPicker.exe进程**
3. **结束进程**


## ⭐ 打包命令| Build Command

#### 使用构建脚本打包
双击运行Build.bat

#### 使用构建命令打包
```bash
pyinstaller --onefile --noconsole ^--name TaskbarColorPicker ^--icon=icon.png ^--add-data "*.png;." ^--exclude-module PyQt5 ^--exclude-module PyQt5.QtCore ^--exclude-module PyQt5.QtGui ^--exclude-module PyQt5.QtWidgets ^--exclude-module numpy ^--exclude-module setuptools ^--exclude-module gi ^--exclude-module clr ^--exclude-module clr_loader ^--exclude-module pycparser ^--exclude-module psutil ^--exclude-module charset_normalizer ^--exclude-module jaraco ^--exclude-module more_itertools ^--exclude-module typing_extensions ^--exclude-module packaging ^--exclude-module importlib_resources ^--exclude-module backports ^--exclude-module importlib_metadata ^--exclude-module zipp ^--exclude-module tomli ^--exclude-module wheel ^01.py
```

## ⭐ 发行版说明 | Release Notes
本项目提供 已编译 exe 版本，无需 Python 环境，下载即可使用。
##### 下载应用最新版本
- [Windows 版](https://github.com/HLBQ/color-picker/releases/tag/v1.0)


## ⭐ 许可证 | License
本项目基于 [MIT License](LICENSE.txt) 开源。
自由使用、修改、分发。


*如果这个项目对你有帮助，请给个Star⭐支持一下！*



