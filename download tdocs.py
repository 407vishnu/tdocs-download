from bs4 import BeautifulSoup
import requests,csv,zipfile,os
from zipfile import BadZipfile
URL="https://netovate.com/doc-search/?fname="
linksonly=1
infile=open('tdoc list.csv')
outfile=open('TDoc links output.csv' ,'a+',newline="")
outfile.seek(0)
processed=[]
for row in csv.reader(outfile):
    processed.append(row[0])
csvreader=csv.reader(infile)
csvwriter=csv.writer(outfile)
next(csvreader)
csvwriter.writerow(['TDoc','Link','Filename'])
if not os.path.exists("zips"):
    os.mkdir("zips")
    os.mkdir("zips/Extracted")
    
for row in csvreader:
##    print (row[0])
    if row[0] in processed:
        continue
    page=requests.get(URL+row[0])
    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        if a_href["href"].endswith(".zip"):
            if linksonly==1:
                csvwriter.writerow([row[0],a_href["href"],row[2]])
                break
            r=requests.get(a_href["href"])
            with open(os.path.join(os.getcwd(),"zips",a_href["href"].split("/")[-1]),'wb') as f:
                f.write(r.content)
            try:
                with zipfile.ZipFile(os.path.join(os.getcwd(),"zips",a_href["href"].split("/")[-1])) as zf:
                    zf.extractall(os.path.join(os.getcwd(),"zips","Extracted",row[2],row[0]))
                    for file in os.listdir(os.path.join(os.getcwd(),"zips","Extracted",row[2],row[0])):
                        csvwriter.writerow([row[0],a_href["href"],row[2],file])
            except BadZipfile:
                print (row[0]+" ******BadZipFile*****")
            break
    if not a_href["href"].endswith(".zip"):
        csvwriter.writerow([row[0],"",row[2]])
infile.close()
outfile.close()


