@echo off

setlocal disabledelayedexpansion
REM setlocal enabledelayedexpansion

for /r %~1 %%G in (*) do (
    set test=%%G
    echo "%test%"
)

pause