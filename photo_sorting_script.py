import os
import shutil
import random
from PIL import Image
from PIL.ExifTags import TAGS

# pip install --upgrade Pillow
# Successfully installed Pillow-9.1.0
TARGET_PATCH = r'D:\'
file_extension = ['jpg', 'gif', 'bmp', 'png']
EXIT_PATCH = r'C:\Users\Root\PycharmProjects\foto_razbor'


def time_foto(target_patch, name):
    try:
        image = Image.open(os.sep.join([target_patch, name]))
        exifdata = image.getexif()
        for tag_id in exifdata:
            # получить имя тега вместо идентификатора
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # декодировать байты
            if isinstance(data, bytes):
                data = data.decode()
            if tag == 'DateTime':
                tmp = data.split()
                tmp = tmp[0].split(':')
            # tmp [год, месяц, день]
                return tmp
    except:
        return ['0', '0', '0']


def copy_file(target_patch, name, tmp):
    exit_patch = EXIT_PATCH
    if os.path.isdir(os.sep.join([exit_patch, tmp[0]])):
        exit_patch = os.sep.join([exit_patch, tmp[0]])
    else:
        os.mkdir(os.sep.join([exit_patch, tmp[0]]))
        exit_patch = os.sep.join([exit_patch, tmp[0]])

    if os.path.isdir(os.sep.join([exit_patch, tmp[1]])):
        exit_patch = os.sep.join([exit_patch, tmp[1]])
    else:
        exit_patch = os.sep.join([exit_patch, tmp[1]])
        os.mkdir(exit_patch)

    if os.path.isfile(os.sep.join([exit_patch, name])):
        tmp_patch = os.sep.join([target_patch, name])
        name = str(random.randint(1, 1000)) + name
        print(f'[!] There is such a file, rename it to {name}')
        shutil.copy(tmp_patch, os.sep.join([exit_patch, name]))
    else:
        shutil.copy(os.sep.join([target_patch, name]), os.sep.join([exit_patch, name]))

def list_file_dir(target_patch):
    list_file = os.listdir(target_patch)
    for name in list_file:
        if os.path.isfile(os.sep.join([target_patch, name])):
            rashirenie = name.split('.')[1]
            if rashirenie in file_extension:
                tmp = time_foto(target_patch, name)
                if tmp[0] != '0':
                    copy_file(target_patch, name, tmp)
                else:
                    print(f'[!] Not data for {name}')
            elif rashirenie == 'mp4':
                exit_patch = EXIT_PATCH
                exit_patch = os.sep.join([exit_patch, 'Video'])
                shutil.copy(os.sep.join([target_patch, name]), os.sep.join([exit_patch, name]))
        else:
            print(f'[*] Go to dir --> {name}')
            list_file_dir(os.sep.join([target_patch, name]))
os.mkdir(os.sep.join([EXIT_PATCH, 'Video']))
list_file_dir(TARGET_PATCH)

#from hachoir.parser import createParser
#from hachoir.metadata import extractMetadata
#from hachoir.core import config as HachoirConfig

#HachoirConfig.quiet = True
# pip install hachoir
#def creation_date(filename):
    #parser = createParser(filename)
    #metadata = extractMetadata(parser)
    #return metadata.get('creation_date')
#print(creation_date())
