import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('C:/Users/Гусев/Desktop/sorts/py/py.zip', 'w')
 
for folder, subfolders, files in os.walk('C:/Users/Гусев/Desktop/'):
 
    for file in files:
        if file.endswith('.jpg'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:/Users/Гусев/Desktop/'), compress_type = zipfile.ZIP_DEFLATED)
 		
 
fantasy_zip.close()
