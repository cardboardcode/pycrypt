@echo off

cd ..

for /L %%a in (1,1,10) do (                                                        
call encode.cmd < input.txt
timeout /t 1 
call decode.cmd < output.txt                                                                 
)
