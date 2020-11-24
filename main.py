import os
from os import listdir
from os.path import isfile, join


def get_blur_ave(dir_path):

    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    for file in onlyfiles:
        file_path = os.join(dir_path,file)
        print(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    apero_path = '/Users/cody/Downloads/apero'
    get_blur_ave(apero_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
