import shutil
import os
import glob
import json
import time
from random import randint
from functools import partial
from multiprocessing import Pool


from_dir_ = '/home/user/Projects/tasks_05/from/'
to_dir_ = '/home/user/Projects/tasks_05/to/'


def coping(to_dir, file_path):
    global from_dir_
    global to_dir_
    if not os.path.exists(to_dir_):
        os.makedirs(to_dir_)
    if os.path.isfile(file_path):
        new_name = to_dir + file_path.replace(from_dir_, '')
        shutil.copy(file_path, new_name)
        print('Coping from {0} to {1}'.format(file_path, new_name))
    """
    elif os.path.isdir(file_path):
        dirs_name = to_dir + file_path.replace(from_dir_, '')
        print('\n' + file_path, dirs_name)
        os.makedirs(dirs_name)
        start(file_path + '/', to_dir)
    else:
        print('Not file and not directory!')
    """
    time.sleep(randint(1, 5))


def files(path='/home/user/from/'):
    return glob.glob(path + '*')


def settings(file='number_of_processes.json'):
    with open(file) as f:
        number = json.load(f)
        return number['number']


def start(from_dir, to_dir):
    names = files(from_dir)
    pool = Pool(settings())
    pool.map(partial(coping, to_dir), names)
    pool.close()
    pool.join()


if __name__ == '__main__':
    start(from_dir_, to_dir_)
