@echo off
echo Building ROKAnswerBot Executable...
echo.

REM Install dependencies
pip install -r requirements.txt

REM Run the build script
python build_exe.py

echo.
echo Build process completed!
pause
