import multiprocessing
import os
from time import sleep

global_list = list()


def add_data():
    for i in range(3):
        global_list.append(i)
        print('add:', i)
        sleep(0.5)
    print('Adding finished:', global_list)


def read_data():
    while True:
        print('read: ', global_list)
        sleep(0.5)


add_process = multiprocessing.Process(target=add_data)
read_process = multiprocessing.Process(target=read_data)

if __name__ == '__main__':
    add_process.start()
    add_process.join()
    print('main:', global_list)
    # read_process.daemon = True
    read_process.start()
    sleep(2)
    read_process.terminate()
    print('main process ends...')
