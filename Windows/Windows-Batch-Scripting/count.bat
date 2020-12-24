@echo off
echo "Hi"

set index=1

:while

echo %index%
if %index% equ 10 goto :end
set /A index=index+1

goto :while


:end
echo "Ending"
PAUSE
