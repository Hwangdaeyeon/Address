from Menu import *
from LinkedList import *
from AddressCode import *
import os

title = "<<주소록 메인>>"
contents = ["등록", "검색", "삭제"]

myMenu = Menu(title, contents)
myMenu.print()
myMenu.read()
while not myMenu.isExitNumber():
    myAd = AddressCode()
    if myMenu.MenuNumber == 1:
        myAd.InAd()
    elif myMenu.MenuNumber == 2:
        myAd.FindAd()
    else:
        myAd.DelAd()
    input("\n<<주소록 메인>> 으로 가려면 [Enter]를 입력하시오")
    myMenu.printNread()

print()
print("\t\t안녕히 가세요")
input()
