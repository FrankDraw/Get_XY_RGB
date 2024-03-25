@ECHO OFF
CHCP 65001 >nul
CD /D %~dp0
COLOR 0A
TITLE "Auto CMD ^for pyinstaller ver:1.0 2024-03-14"
REM MODE CON: COLS=85 LINES=30

ECHO.
ECHO ********************************************************************************************************
ECHO [Current Path]:
ECHO  %CD%
ECHO ********************************************************************************************************
ECHO.


:: Code Begin.
set PyFile="Get_XY_RGB_v3.0.py"
set IconFile=get_xy_rgb_favicon64.ico

ECHO.
ECHO  Python File Name: %PyFile%
ECHO  Icon   File Name: %IconFile%
ECHO.
ECHO Press any key to start the convert.
PAUSE >NUL

pyinstaller -F -i ./%IconFile% %PyFile%

:: Code End.

cmd.exe /k
pause
