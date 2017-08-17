import urllib.request
import threading

files = open("imagenet_synset.txt","r")

string = files.read()
ali = string.split('\n')
    
def d1(a=0):
    for i in range(0,len(ali),5):
        try:
            print('downloading from:' ,ali[i])
            urllib.request.urlretrieve('%s' % ali[i] ,'%s.jpg' % a)
            a += 5
        except Exception as e:
            print(e)

def d2(b=1):
    for i in range(1,len(ali),5):
        try:
            print('downloading from:' ,ali[i])
            urllib.request.urlretrieve('%s' % ali[i] ,'%s.jpg' % b)
            b += 5
        except Exception as e:
            print(e)
def d3(c=2):
    for i in range(2,len(ali),5):
        try:
            print('downloading from:' ,ali[i])
            urllib.request.urlretrieve('%s' % ali[i] ,'%s.jpg' % c)
            c += 5
        except Exception as e:
            print(e)
def d4(d=3):
    for i in range(0,len(ali),5):
        try:
            print('downloading from:' ,ali[i])
            urllib.request.urlretrieve('%s' % ali[i] ,'%s.jpg' % d)
            d += 5
        except Exception as e:
            print(e)
def d5(f=4):
    for i in range(0,len(ali),5):
        try:
            print('downloading from:' ,ali[i])
            urllib.request.urlretrieve('%s' % ali[i] ,'%s.jpg' % f)
            f += 5
        except Exception as e:
            print(e)


t = threading.Thread(name = 'd1' , target = d1)
w = threading.Thread(name = 'd2' , target = d2)
q = threading.Thread(name = 'd3' , target = d3)
y = threading.Thread(name = 'd4' , target = d4)
u = threading.Thread(name = 'd5' , target = d5)


w.start()
q.start()
t.start()
y.start()
u.start()
