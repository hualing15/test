import pyperclip
from PIL import ImageGrab,Image

def getRGB(SC,h):
    R,G,B,F=SC.getpixel((400,910))
    times = 1
    for x in range(300,1620):
        for y in range(910,1035):
            #print(times,x,y,R,G,B,SC.getpixel((x,y)))
            r,g,b,f=SC.getpixel((x,y))
            if R==r and G==g and B==b and R>210 and G>210 and B>210:
                times=times+1
            else:
                times=1
                R=r
                G=g
                B=b
            if times>h:
                return R,G,B
    return getRGB(SC,h-1)

def getBorder(SC,R,G,B):
    Left=1920
    Right=0
    Up=1080
    Down=0
    for x in range(300,1620):
        for y in range(910,1035):
            r,g,b,f=SC.getpixel((x,y))
            if R==r and G==g and B==b:
                Right=x
                if x<Left:
                    Left=x
                if Up>y:
                    Up=y
                if Down<y:
                    Down=y
    return Left,Up,Right,Down

def getChinese(ScreenCapture):
    ScreenCapture.resize((1920,1080))
    SC = ScreenCapture
    BOX=(300,910,1620,1035)
    R,G,B=getRGB(SC,12)
    print(R,G,B)
    Left,Up,Right,Down=getBorder(SC,R,G,B)
    List=int((Down-Up)/35)
    print(Left,Up,Right,Down)
    TE = ScreenCapture.crop(BOX)
    #TE.show()
    TE2=SC.crop((Left-1,Up-1,Right+1,Down+1))
    TE2.show()
    TE2.save("./Image/Check.png")
    return ScreenCapture

Screenleft=0.23
box=(200,865,1920,1080)

def getScreenShoot():
    return ImageGrab.grab()

ScreenCapture = getScreenShoot()
ScreenCapture.crop(box)
ScreenCapture.save("./Image/1.png")
Test1 = Image.open("./Image/test1.png")
Test2 = Image.open("./Image/test2.png")
Test3 = Image.open("./Image/test3.png")
Test4 = Image.open("./Image/test4.png")
getChinese(Test2)
W,H= ScreenCapture.size
left = int(H*(1.0-Screenleft))
box=(0,left,W,H)
#abox=(0,865,1280,1030)
img = ScreenCapture.crop(box)
print(W,H)
#ScreenCapture.show()
#img.show()

