from pathlib import Path

files = sorted(Path('./allphotos').iterdir(), key=lambda f: f.stat().st_ctime)
# files = os.listdir('./allphotos')

res = '<div class="grid column3   photos  js-list"><h1> Photos </h1>'
for fi in files:
    f = str(fi)
    arr = f.split("/")
    f = arr[1]
    if '.jpg' in f or '.jpeg' in f:
        res = res + '''<div class="photo">
            <a href="'''
        path = "../images/ourcs19/otherphotos/"+f.lower()
        res = res + path + '''" target="_self">
        <span><img alt="ourcs19 image" src=" ''' + path + '''"/></span>
        </a>
        </div>
        '''
res = res + '</div>'
print(res)
