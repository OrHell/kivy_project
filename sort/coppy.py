import os
import zipfile
surce = input()
surces = input()
fantasy_zip = zipfile.ZipFile(surce, 'w')
 
for folder, subfolders, files in os.walk(surces):
 
    for file in files:
        if file.endswith('.jpg'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), surces), compress_type = zipfile.ZIP_DEFLATED)
 		
 
fantasy_zip.close()
