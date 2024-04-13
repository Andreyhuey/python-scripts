import collections
import os
import glob
import shutil
import gc
import threading
from time import time
from functools import wraps
from pathlib import Path
from PIL import Image
import win32com.client as win32

# folder to save resized photos
target = 'prod'

# folder to save original photos
archive_path = 'src'

to_email = "andreyhuey777@gmail.com"


def main():
    process_sf_photos()


def count_files_to_resize():
    global c
    global d
    c = collections.Counter(p.suffix for p in Path.cwd().glob('*.jpg'))
    d = c['.jpg']
    print(f'There are {d} files to resize.')


def resize():
    new_size = (180, 240)
    global file_count
    file_count = 0
    for i in Path.cwd().iterdir():
        if i.suffix == '.jpg':
            file = Image.open(i.name)
            file = file.resize(new_size)
            file.save(os.path.join(target, i.name[:-4] + '.jpg'))
            file_count += 1
    print(f'{file_count} images were resized', '.....', sep='\n')


# Copies each re-sized file into archive folder
def copy_to_archive():
    global copy_count
    copy_count = 0
    print('Copying files to SubSFPhotos - Archive...')
    for fn in glob.glob(os.path.join(target, '*.jpg')):
        shutil.copy(fn, archive_path)
        copy_count += 1

    print('Finished! ', f'{copy_count} files copied.', '.....', sep='\n')


def delete_old_files():
    global delete_count
    delete_count = 0
    print('Deleting old files...')
    
    # Create 'src' directory if it doesn't exist
    os.makedirs(archive_path, exist_ok=True)
    
    os.chdir(target)
    for i in Path.cwd().iterdir():
        if i.suffix == '.jpg':
            os.remove(i.name)
            delete_count += 1
    print('Finished!', f'{delete_count} files deleted.', '.....', sep='\n')


def thread_resize():
    threadResize = threading.Thread(target=resize)
    threadResize.start()
    threadResize.join()


def thread_copy():
    threadCopy = threading.Thread(target=copy_to_archive)
    threadCopy.start()
    threadCopy.join()


def thread_delete():
    threadCopy = threading.Thread(target=delete_old_files)
    threadCopy.start()
    threadCopy.join()


def good_email():
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')
    new_mail = outlook.CreateItem(0)
    new_mail.Subject = "Photos resized with no problems"
    message = f'Number of files to resize: {d}.\n{file_count} were resized.\n' \
              f'{copy_count} files were copied.\n{delete_count} files were deleted. '
    new_mail.Body = message
    new_mail.To = to_email
    new_mail.Send()


def bad_email():
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')
    new_mail = outlook.CreateItem(0)
    new_mail.Subject = "Photo resize error."
    message = "There was an error in resizing the images."
    new_mail.Body = message
    new_mail.To = to_email
    new_mail.Send()


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f'Process runs in {format(end - start)} seconds.')
        return result

    return wrapper


@timer
def process_sf_photos():
    try:
        count_files_to_resize()
        thread_resize()
        thread_copy()
        thread_delete()
        gc.collect()
        # good_email()
    except Exception as x:
        print(f"Looks like we have a problem: {type(x)} -> {x}")
        # bad_email()


if __name__ == '__main__':
    run = 1
    if run == 1:
        main()
    else:
        print("Program didn't run. Set 'run' to 1 to run it.")

    gc.collect()
