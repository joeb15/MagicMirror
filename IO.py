# -*- coding: utf-8 -*-

import os, codecs, time


def exists(file_name):
    return os.path.isfile(file_name) or os.path.isdir(file_name)


def create(file_name):
    write(file_name, "-")


def write(file_name, data):
    dirs = file_name.split("/")
    dir_name = ""
    for i in range(len(dirs) - 1):
        dir_name += dirs[i] + "/"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file = codecs.open(file_name, 'w+', encoding='utf8')
    file.truncate()
    file.write(data)
    file.write("\n::END::")
    file.close()


def delete(file_name):
    os.remove(file_name)


def read(file_name):
    if not exists(file_name):
        return ""
    file = codecs.open(file_name, 'r', encoding='utf8')
    temp = file.read()
    if temp.endswith("\n::END::"):
        return temp.split("\n::END::")[0]
    time.sleep(0.1)
    return read(file_name)
