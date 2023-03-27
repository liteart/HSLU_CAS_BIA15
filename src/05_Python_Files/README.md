  
 
# 05_Python_Files

## Introduction 👋

Python file I/O (a.k.a File handling) is one of the essential topics for programmers and automation testers. It is required to work with files for either writing to a file or read data from it.

Also, if you are not already aware, I/O operations are the costliest operations where a program can stumble. Hence, you should be quite careful while implementing file handling for reporting or any other purpose. Optimizing a single file operation can help you produce a high-performing application or a robust solution for automated software testing.

In Python, file processing takes place in the following order.

* Open a file that returns a filehandle.
* Use the handle to perform read or write action.
* Close the filehandle.

Before you do a read or write operation to a file in Python, you need to open it first. And as the read/write transaction completes, you should close it to free the resources tied with the file.
