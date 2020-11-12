
# This code is based on: https://github.com/nutonomy/second.pytorch.git
# 
# MIT License
# Copyright (c) 2018 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime
import os
import shutil

def create_folder(prefix, add_time=True, add_str=None, delete=False):
    additional_str = ''
    if delete is True:
        if os.path.exists(prefix):
            shutil.rmtree(prefix)
        os.makedirs(prefix)
    folder = prefix
    if add_time is True:
        # additional_str has a form such as '170903_220351'
        additional_str += datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        if add_str is not None:
            folder += '/' + additional_str + '_' + add_str
        else:
            folder += '/' + additional_str
    if delete is True:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    os.makedirs(folder)
    return folder