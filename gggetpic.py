import requests,json,shutil,threading,re
with open('urls.txt','r',encoding='utf8') as r:
    li=r.readlines()
def download(filename,url):
    try:
        res=requests.get(url,stream=True)
    except:
        return
    if res.status_code == 200:
        with open( filename, 'wb') as f:
            try:
                shutil.copyfileobj(res.raw, f) 
            except:
                pass

th=[]

for i,n in enumerate(li):
    fileformat=None
    for j in ['jpg','jpeg','JPG','png']:
        if j in n:
            #print(n,j)
            fileformat='.'+j
            break 
    if fileformat:
        filename='imgs/test/a' + str(i)  + fileformat
        t=threading.Thread(target=download,args=[filename,n])
        th.append(t)
        t.start()

for i in th:
    i.join()
# with open('picjson.json','w',encoding='utf8') as jr:
#     json.dump(j,jr,indent=4)