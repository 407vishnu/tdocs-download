import os
path="C:\\Users\\vishn\\Desktop\\Scripts\\tdocs download\\zips\\Extracted"
for roots,dirs,files in os.walk(path):
    for file in files:
        os.rename(os.path.join(roots,file),os.path.join(roots,file.replace("#"," ").replace("&"," and ")))
        print (os.path.join(roots,file.replace("#"," ")))
    
