import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('C:/Users/Mentall/Desktop/sort/jpg/jpg.zip', 'w')
 
for folder, subfolders, files in os.walk('C:/Users/Mentall/Desktop/'):
 
    for file in files:
        if file.endswith('.jpg'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:/Users/Гусев/Desktop/'), compress_type = zipfile.ZIP_DEFLATED)
 		
 
fantasy_zip.close()
