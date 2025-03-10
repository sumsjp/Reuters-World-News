REM @echo off

REM 自動切換到 bat 檔案自身所在的目錄
cd /d "%~dp0"

REM 啟動虛擬環境
call ..\Scripts\activate.bat

REM 執行 Python 腳本
git pull
python update_youtube.py
git add ..
git commit -am update
git push

REM 停用虛擬環境（可選）
call ..\Scripts\deactivate.bat
