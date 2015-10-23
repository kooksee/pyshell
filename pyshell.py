#!/usr/bin/env python
# -*- coding:utf-8 -*-
from subprocess import Popen
from subprocess import PIPE


def py_ver():
    '''
    得到python的版本
    '''
    import sys
    return sys.version_info[0]
_ver = py_ver()

if _ver == 2:
    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)

elif _ver == 3:
    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)
else:
    raise ValueError(u'python 版本不正确')
del _ver

# 解析字符串中的环境变量


def parse_shell_token(t):
    import os
    # 将～等用用户的家目录进行替换
    t = os.path.expanduser(t)
    # path中可以使用环境变量,'$PATH'...
    t = os.path.expandvars(t)
    return t


class cmd(object):

    def __init__(self, *args, **kwargs):
        self.stdout = None
        self.cmd(*args, **kwargs)

    def cmd(self, cmd, env=None, stdout=PIPE):
        p = Popen(parse_shell_token(cmd), shell=True,
                  stdout=stdout, stdin=PIPE, stderr=PIPE, env=env)
        self.stdout, self.stderr = p.communicate(input=self.stdout)
        self.code = p.returncode
        return self

    def __repr__(self):
        return self.value()

    def __unicode__(self):
        return self.value()

    def __str__(self):
        return self.value()

    def __nonzero__(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self.value())

    def value(self):
        if not self.stdout:
            return ''
        return self.stdout.strip()

if __name__ == '__main__':
    # print cmd('ls -l')
    # print cmd("ls . | grep 'pyc'")
    # print cmd("konsole --hold -e 'konsole --help'")
    # print cmd('scrapy list')
    # print cmd('ls $HOME')
    # print cmd('ls ~')
   # import os
    #os.system('clear')

    print cmd('fromclip')
