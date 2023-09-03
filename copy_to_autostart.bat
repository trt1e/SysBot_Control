@echo off
setlocal

:: Set the source file
set "source_file=main_frame.py"

:: Use environment variable to locate the Startup folder
for /f "tokens=*" %%a in ('echo %APPDATA%') do (
    set "destination_folder=%%a\Microsoft\Windows\Start Menu\Programs\Startup"
)

:: Copy the source file to the destination folder
copy "%~dp0%source_file%" "%destination_folder%"

:: Exit the batch file
exit /b
