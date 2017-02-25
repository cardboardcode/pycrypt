@echo off

cd ..

for /L %%a in (1,1,5) do (                                                        
call encode.cmd < input.txt
call decode.cmd < output.txt                                                                 
)

cd debug

