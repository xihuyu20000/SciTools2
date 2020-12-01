@echo off
@rem C:\Users\Administrator\.virtualenvs\ToolWindow\Scripts\python.exe  cx_setup.py build
pyinstaller.exe  -i icon.ico -D -w gui/main.py  --hidden-import PyQt5.QtWebKit