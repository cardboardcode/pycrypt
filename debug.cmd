@echo off

cd debug
echo ------------------DEBUG START----------------
call debugtest > report.txt || echo debug launch failed. 
echo ------------------DEBUG END------------------
call reportc || echo Unable to check the report

call average || echo Unable to average report

cd ..

exit /b