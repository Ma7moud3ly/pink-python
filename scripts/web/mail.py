#!/usr/bin/python
import platform
print ('Content-type: text/html\n')
print ('<h1>Hello From Shared Hosting ^_^</h1>')
print ('<h2>My operating system is %s<h2>'%platform.system())
print ('<h2>My python version is %s<h2>'%platform.python_version())
