import os

BASE_DIR = '/Users/ajay/Desktop/Django/appdjango/myapp'

print(os.path.join(BASE_DIR,'Templates'))

a_url = (os.path.join(BASE_DIR,'Templates'))

print(a_url)
print(os.listdir())
os.curdir = a_url
print(os.curdir)
print(os.path.join(os.curdir,'emp/about.html'))
# return redirect ( requires / slash vlaue )
# retrun render() function does NOT require the slash values.. 

