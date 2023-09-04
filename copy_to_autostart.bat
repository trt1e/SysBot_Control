@echo off
setlocal

set "source_file=main_frame.py"

for /f "tokens=*" %%a in ('echo %APPDATA%') do (
    set "destination_folder=%%a\Microsoft\Windows\Start Menu\Programs\Startup"
)

copy "%~dp0%source_file%" "%destination_folder%"

exit /b
