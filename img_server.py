#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Date     : 2021-03-31
# @Author   : pt
# -*- coding:utf-8 -*-
import os
from subprocess import Popen

path = os.path.split(os.path.realpath(__file__))[0]

p = Popen("img_server.bat", cwd=r"{}\img_server".format(path), shell=True)
stdout, stderr = p.communicate()
print("img_server msg：{},{}".format(stdout, stderr))
