@echo off

set _tst=0

for /l %%G in (1,1,5) do (
    echo "%_tst%"
    set /a _tst+=1
)

pause