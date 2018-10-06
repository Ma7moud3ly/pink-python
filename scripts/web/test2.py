#!/home/<user_name_on_host>/.local/bin/python3
print ("Content-type: text/html\n")
import os,platform
print ('<h1>Hello From Shared Hosting ^_^</h1>')
print ('<h2>My operating system is %s<h2>'%platform.system())
print ('<h2>My python version is %s<h2>'%platform.python_version())
