## User Guide

#### Setting up

> 1. Click on the green button on the top right of the list of files on this page to download. Choose a suitable directory or folder to unzip all of the content.
  2. Open up your command prompt by pressing **Windows Key** + **R**. Type **cmd** into the Run window which opens up.
  3. **cd** to the directory where you have unzipped all the file content.
  4. You are now ready to use pycrypt, a simple python-based cryptographer which you will be able to customize on your own as you learn more about python. 

#### Usage

> 1. Create a .txt file which you would like encrypt in the directory **bench**.
	> **Take note** When naming your file, remember to add a '**0**' behind your intented filename. eg. **message0**, **newfile0**, **secret0**
	> '**0**' indicates that the file is **not** encrypted yet.
	> '**8**' indicates that the file is **encrypted** already.

##### Encoding
> 2. Continuing from setting up, type the following command into the command prompt terminal
 > **encode**
 > The terminal will say **Enter name of your .txt file**
 > **filename0** (eg. type "message0")
 > Your file is now being encoded based on the default parser library. The number at the end of your .txt file has been changed to from **0** to **8**. 

##### Decoding
> 3. Follow the steps below to decode it.
 > **decode**
 > The terminal will say **Enter name of your .txt file**
 > **filename8** (eg. type "message8")
 > Your file is now being encoded based on the default parser library. The number at the end of your .txt file has been changed to from **8** to **0**. 

> 4. Customize your own parser library and create your own secret language that no one will be able to crack. Have fun.  


#### Others

> There are other files hanging around so feel free to explore what they do. Go crazy.

Purpose: 

I have started this project in order to sustain and improve my understanding of the Python programming language as well as the Object-Oriented Programming (OOP) principles.

OOP Principles:

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction

Coding Practices:
http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html