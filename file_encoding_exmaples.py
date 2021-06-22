#opt 1
def predict_encoding(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)['encoding']
    
#opt 2   
import magic

blob = open('unknown-file', 'rb').read()
m = magic.Magic(mime_encoding=True)
encoding = m.from_buffer(blob)

#opt 3

import magic

blob = open('unknown-file', 'rb').read()
m = magic.open(magic.MAGIC_MIME_ENCODING)
m.load()
encoding = m.buffer(blob)  # "utf-8" "us-ascii" etc

#opt4:
from bs4 import UnicodeDammit
with open('automate_data/billboard.csv', 'rb') as file:
   content = file.read()

suggestion = UnicodeDammit(content)
suggestion.original_encoding


import os, shutil, glob

#Source file 
sourcefile = 'Desktop/00/'

# for loop then I split the names of the image then making new folder 
for file_path in glob.glob(os.path.join(sourcefile, '*.jpg*')):
    new_dir = file_path.rsplit('.', 1)[0]    
    # If folder does not exist try making new one
    try:
        os.mkdir(os.path.join(sourcefile, new_dir))
    # except error then pass
    except WindowsError:
        pass
    # Move the images from file to new folder based on image name
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
#'iso-8859-1'

opt5:
   
