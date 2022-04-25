import docx, os, datetime
import comtypes.client
masterdir=os.getcwd()
folder="test"
print (str(datetime.datetime.now()))
for roots,dirs,files in os.walk(masterdir+'/'+folder):
    for file in files:
        if ".doc" in file:
            word = comtypes.client.CreateObject('Word.Application')
            doc = word.Documents.Open(os.path.join(roots,file))
            doc.SaveAs(os.path.join(roots,"".join(file.split(".")[:-1])+'_readable.pdf'), FileFormat=17)
            doc.Close()
        else:
            print ("non-Word file found - " + file) 
print (str(datetime.datetime.now()))
