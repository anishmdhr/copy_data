import os, shutil


# get the directory you want to copy from
# walk through all the folders in the directory tree    
# create the respective directory and copy the respective files 
# copy the files to a new directory(backup directory)

# get the directory you want to copy from
copy_directory = 'D:\\S777\\SIT771'
copy_to_directory = os.path.join(copy_directory, 'backup')



# creating the directory structure for the files to be copied into
if not os.path.exists('D:\\S777\\SIT771\\backup'):
    os.makedirs(copy_to_directory + '\\images')
    os.makedirs(copy_to_directory + '\\videos')
    os.makedirs(copy_to_directory + '\\documents')
    os.makedirs(copy_to_directory + '\\music')

for folderName, subfolders, filenames in os.walk(copy_directory):

# check if the files are photos or videos or pdf
    for file in filenames:
        # all types of image files
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif') or file.endswith('.jpeg') or file.endswith('.tif') or file.endswith('.tiff') or file.endswith('.psd') or file.endswith('.ai') or file.endswith('.raw') or file.endswith('.svg') or file.endswith('.heic'):
            # Check if the file already exists
            # print(copy_to_directory + '\\images' + file)
            if not os.path.exists(copy_to_directory + '\\images' + '\\' +file):
                # copy the files to new created directory 
                try:
                    shutil.copy(os.path.join(folderName, file), copy_to_directory + '\\images')
                except shutil.SameFileError:
                    print('Image file: ' + file + ' already exists')

        if file.endswith('.pdf') or file.endswith('.docx'):
            if not os.path.exists(copy_to_directory + '\\documents' + file):
                try:
                    shutil.copy(os.path.join(folderName, file), copy_to_directory + '\\documents')
                except shutil.SameFileError:
                    print('Document file: ' + file + ' already exists')
        # all types of video files
        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.flv') or file.endswith('.mov') or file.endswith('.wmv') or file.endswith('.webm'):
            if not os.path.exists(copy_to_directory + '\\videos' + file):
                try:
                    shutil.copy(os.path.join(folderName, file), copy_to_directory + '\\videos')
                except shutil.SameFileError:
                    print('Video file: ' + file + ' already exists')
        # all types of music files
        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.wma') or file.endswith('.aac') or file.endswith('.flac') or file.endswith('.ogg') or file.endswith('.alac') or file.endswith('.aiff'):
            if not os.path.exists(copy_to_directory + '\\music' + file):
                try:
                    shutil.copy(os.path.join(folderName, file), copy_to_directory + '\\music')
                except shutil.SameFileError:
                    print('Music file: ' + file + ' already exists')
 



