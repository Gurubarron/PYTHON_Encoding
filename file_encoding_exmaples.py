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
