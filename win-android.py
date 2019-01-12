import os
from PIL import Image
import sys

filename = sys.argv[-1]
fileExt = filename.split('.')[1]

PATH_DIR = os.path.abspath('android/app/src/main/res/')
LIST_DIR = os.listdir(PATH_DIR)

hdpiFiles = ['mipmap-hdpi', 'mipmap-mdpi', 'mipmap-xhdpi', 'mipmap-xxhdpi', 'mipmap-xxxhdpi']
sizeLoc = {"mipmap-hdpi":72,"mipmap-mdpi":48,"mipmap-xhdpi":96,"mipmap-xxhdpi":144,"mipmap-xxxhdpi":192}

hdpi = 72,72
mdpi = 48,48
xhdpi = 96,96
xxhdpi = 144,144
xxxhdpi = 192,192


def checkFiles(hdpiFiles, LIST_DIR):
    try: 
        for i in hdpiFiles:
            if i not in LIST_DIR:
                print(i, 'is missing. Creating that file...')
                print('')
                os.makedirs(PATH_DIR + '/' + i)
            else:
                print('No Files are Missing!')
                print('starting to resize...')
                print('')
                break
    except Exception as e:
        print(e)

def resize(hdpi, mdpi, xhdpi, xxhdpi, xxxhdpi, sizeLoc):
    if fileExt != 'png':
        print('Only the PNG Format is accepted.')
    else:
        return None
    try: 
        defaultImage = Image.open(filename) 
        sizelist = [hdpi,mdpi,xhdpi,xxhdpi,xxxhdpi]
        for x in sizelist:
            resizedImage = defaultImage.resize(x)
            for k,v in sizeLoc.items():
                if resizedImage.size[0] == v:
                    resizedImage.save(str(PATH_DIR + '/' + k + '/' + 'ic_launcher' + "." + fileExt))
                    print(k,str(v) + 'x' + str(v),'saved!',)
            
            
    except Exception as e:
        print(e)
            
if __name__ == '__main__':
    checkFiles(hdpiFiles, LIST_DIR)
    resize(hdpi,mdpi,xhdpi,xxhdpi,xxxhdpi,sizeLoc)
