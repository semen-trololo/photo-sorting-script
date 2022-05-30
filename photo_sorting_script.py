from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core import config as HachoirConfig
import os
import shutil
import random
target_patch = r'test'
check_patch = r''
file_extension_foto = ['jpg', 'gif', 'bmp', 'png']
file_extension_video = ['mp4', 'avi']
HachoirConfig.quiet = True
# pip install hachoir

def crate_patch(data_time):
    tmp_patch = os.sep.join([target_patch, str(data_time.year)])
    if os.path.isdir(tmp_patch):
        if os.path.isdir(os.sep.join([tmp_patch, str(data_time.month)])):
            tmp_patch = os.sep.join([tmp_patch, str(data_time.month)])
            return tmp_patch
        else:
            os.mkdir(os.sep.join([tmp_patch, str(data_time.month)]))
            tmp_patch = os.sep.join([tmp_patch, str(data_time.month)])
            return tmp_patch
    else:
        os.mkdir(tmp_patch)
        if os.path.isdir(os.sep.join([tmp_patch, str(data_time.month)])):
            tmp_patch = os.sep.join([tmp_patch, str(data_time.month)])
            return tmp_patch
        else:
            os.mkdir(os.sep.join([tmp_patch, str(data_time.month)]))
            tmp_patch = os.sep.join([tmp_patch, str(data_time.month)])
            return tmp_patch

def copy_file(patch, name):
    try:
        data_time = creation_date(patch)
        exit_patch = crate_patch(data_time)
        shutil.copy(patch, os.sep.join([exit_patch, name]))
    except:
        print('[!] Error ', patch)
        
def copy_file_video(patch, name):
    try:
        data_time = creation_date(patch)
        exit_patch = crate_patch(data_time)
        if os.path.isdir(os.sep.join([exit_patch, 'video'])):
            exit_patch = os.sep.join([exit_patch, 'video'])
            shutil.copy(patch, os.sep.join([exit_patch, name]))
        else:
            os.mkdir(os.sep.join([exit_patch, 'video']))
            exit_patch = os.sep.join([exit_patch, 'video'])
            shutil.copy(patch, os.sep.join([exit_patch, name]))
    except:
        print('[!] Error ', patch)

def creation_date(filename):
    parser = createParser(filename)
    metadata = extractMetadata(parser)
    return metadata.get('creation_date')

def list_file_dir(target_patch):
    list_file = os.listdir(target_patch)
    for name in list_file:
        if os.path.isfile(os.sep.join([target_patch, name])):
            if name.split('.')[1] in file_extension_foto:
                copy_file(os.sep.join([target_patch, name]), name)
            elif name.split('.')[1] in file_extension_video:
                copy_file_video(os.sep.join([target_patch, name]), name)
            else:
                print('[*] Unknow', name)
        else:
            print(f'[*] Go to dir --> {name}')
            list_file_dir(os.sep.join([target_patch, name]))
list_file_dir(check_patch)
#print(data_time.year)
#print(data_time.month)
#print(data_time.day)
#print(data_time.hour)
#print(data_time.minute)
