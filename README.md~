# pyshell
pyshell 调用命令，让你像执行bash一样方便

'''python
from pyshell import cmd
print cmd('ls -al')
print cmd("ls | grep 'LICENSE'")
print cmd("konsole --hold -e 'konsole --help'")
print cmd('ls $HOME')
print cmd('ls ~')

dd = cmd('ls ~').value().split('\n')
print dd
cmd("gnome-terminal -x bash -c 'python -h;read' ")
'''