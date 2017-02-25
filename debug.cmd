@echo off

cd debug
echo ------------------DEBUG START----------------
call debugtest > report.txt || echo debug launch failed. 
echo ------------------DEBUG END------------------
exit /b