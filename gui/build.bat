@echo off
@rem 先pip install  pyinstaller 安装；然后执行where  pyinstaller.exe 查询刚刚安装的；最后使用指定的pyinstaller版本
@rem 遇到 module 'enum' has no attribute 'IntFlag'错误，则执行 pip uninstall enum34
E:\workspace\workspace-js\ai-edu\SciTools2\venv\Scripts\pyinstaller.exe  -i icon.ico -D -w main.py  --hidden-import PyQt5.QtWebKit