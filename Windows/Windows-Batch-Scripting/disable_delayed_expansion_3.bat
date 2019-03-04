@echo off

for /r %~1 %%G in (*) do (
    set test=%%G
    echo "%test%"
    REM call :processFile
)

goto end

:processFile
    echo "test = %test%"
    echo/
    goto :eof

:end

pause