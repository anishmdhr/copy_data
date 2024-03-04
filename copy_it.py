import os, shutil


# get the directory you want to copy from
# walk through all the folders in the directory tree    
# create the respective directory and copy the respective files 
# copy the files to a new directory(backup directory)

for folderName, subfolders, filenames in os.walk('D:\\S777\\SIT771'):

# check if the files are photos or videos or pdf
    for file in filenames:
        # all types of image files
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif') or file.endswith('.jpeg') or file.endswith('.tif') or file.endswith('.tiff') or file.endswith('.psd') or file.endswith('.ai') or file.endswith('.raw') or file.endswith('.svg'):
            print(file)
            #shutil.copy(os.path.join(folderName, file),os.path.join(folderName, file + '.backup'))
            
        if file.endswith('.pdf') or file.endswith('.docx'):
            print(file)
        # all types of video files
        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.flv') or file.endswith('.mov') or file.endswith('.wmv') or file.endswith('.webm'):
            print(file)
        
            # shutil.copy(os.path.join(folderName, file),os.path.join(folderName, file + '.backup'))
 



