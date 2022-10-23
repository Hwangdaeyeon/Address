import os
from LinkedList import *
from Bst import *

Ad = LinkedList()
map_phone = BSTMap()
map_name = BSTMap()
adcontents = ["[이   름]", "[전화번호]", "[이 메 일]","[주   소]"]
class Node:				                    
    def __init__ (self, rec, link=None):	
        self.rec = rec 			        
        self.link = link

class AddressCode(object):
    """description of class"""

    def __init__(self, name = None, phone = None, mail = None, addr = None):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.addr = addr
        self.__menuNumber=1
        pos = 0
    @property
    def MenuNumber(self):
        return self.__menuNumber

    def print(self):
        os.system("cls")
        contents = ["이   름", "전화번호"]
        print("\n\n\n\n\n")
        print("\t\t================================")
        print("\t\t\t",end="")       
        print("\n")
        i=0
        for content in contents:
            print("\t\t", end="")
            i = i + 1
            print(i, end=". ")
            print(content, end="검색 :")
            print("\n")

        print("\n\t\t================================")
        print("\n\t\t번호를 입력하세요 : ", end=' ')


    def getMenuNumber(self):
        try:
            self.__menuNumber = int(input())
            if 1<= self.__menuNumber <= 2:
                return self.__menuNumber
            else:
                raise Exception("숫자가 범위를 벗어 났습니다.")
        except ValueError as e:
            print()
            print("숫자를 입력하지 않았습니다.")
        except Exception as e:
            print()
            print(e)
        input()
        return - 1

    def read(self):
        self.__menuNumber = self.getMenuNumber()
        while self.__menuNumber < 0:
            self.print()
            self.__menuNumber = self.getMenuNumber()
        return self.__menuNumber


    def InAd(self):
        os.system("cls")
        print("\n\n\n\n\n<<주소록 등록>>")
        name = input("[이   름] 입력:")
        phone = input("[전화번호] 입력:")
        mail = input("[이 메 일] 입력:")
        addr = input("[주   소] 입력:")
        info = (name, phone, mail, addr)
        Ad.insert(0, info)
        Ad.display()
        linkedinfo = Ad.getEntry(0)
        rec1 = AddressCode(linkedinfo[0], linkedinfo[1], linkedinfo[2], linkedinfo[3])
        n1 = Node(rec1)
        map_phone.insert(n1.rec.phone, n1) 
        map_name.insert(n1.rec.name, n1)
        print("\n## 주소 등록 완료")
        print("================================")
        i = 0
        for content in Ad.getEntry(0):
            print(adcontents[i] + content)
            i = i + 1
        print("================================")
        map_name.display()
        map_phone.display()


    def FindAd(self):
        os.system("cls")
        print("<<주소록 검색>>")
        self.print()
        self.read()
        if self.__menuNumber == 1:
            print("<<이름 검색>>")
            Sname = input("이름 입력:")
            Sresult = map_name.search(Sname)
            print(Sresult.key)
            if Sresult != None :
                print('[탐색 성공]')
                print(adcontents[0] + "{0}".format(Sresult.value.rec.name))
                print(adcontents[1] + "{0}".format(Sresult.value.rec.phone))
                print(adcontents[2] + "{0}".format(Sresult.value.rec.mail))
                print(adcontents[3] + "{0}".format(Sresult.value.rec.addr))
            else:
                print("{0}는 저장되지 않은 이름입니다.".format(Sname))
        else:
            print("<<전화번호 검색>>")
            Sphone = input("전화번호 입력:")
            Sresult = map_phone.search(Sphone)
            if Sresult != None : 
                print('[탐색 성공]')
                print(adcontents[0] + "{0}".format(Sresult.value.rec.name))
                print(adcontents[1] + "{0}".format(Sresult.value.rec.phone))
                print(adcontents[2] + "{0}".format(Sresult.value.rec.mail))
                print(adcontents[3] + "{0}".format(Sresult.value.rec.addr))
            else:
                print("[탐색 실패]\n{0}는 저장되지 않은 번호입니다.".format(Sphone))

    def DelAd(self):
        os.system("cls")
        print("<<주소록 삭제>>")
        self.print()
        self.read()
        if self.__menuNumber == 1:
            print("<<이름 검색>>")
            Dname = input("삭제할 이름 입력:")
            Dresult = map_name.search(Dname)
            if Dresult != None : 
                print('[탐색 성공]')
                print(adcontents[0] + "{0}".format(Dresult.value.rec.name))
                print(adcontents[1] + "{0}".format(Dresult.value.rec.phone))
                print(adcontents[2] + "{0}".format(Dresult.value.rec.mail))
                print(adcontents[3] + "{0}".format(Dresult.value.rec.addr))
                choice = input("★삭제하려면 0 입력, enter 는 삭제 취소 :")
                if choice == "0":
                    map_name.delete(Dname)
                    map_phone.delete(Dresult.value.rec.phone)
                    map_name.display()
                    map_phone.display()
                    Ad.delete(Ad.getPos((Dresult.value.rec.name, Dresult.value.rec.phone, Dresult.value.rec.mail, Dresult.value.rec.addr)))
                    Ad.display()
                    print("## 주소 삭제 완료")
                else:
                    print("## 삭제 취소")
            else:
                print("{0}는 저장되지 않은 이름입니다.".format(Dname))

        else:
            print("<< 전화번호 검색>>")
            Dphone = input("삭제할 전화번호 입력:")
            Dresult = map_phone.search(Dphone)
            if Dresult != None : 
                print('[탐색 성공]')
                print(adcontents[0] + "{0}".format(Dresult.value.rec.name))
                print(adcontents[1] + "{0}".format(Dresult.value.rec.phone))
                print(adcontents[2] + "{0}".format(Dresult.value.rec.mail))
                print(adcontents[3] + "{0}".format(Dresult.value.rec.addr))
                choice = input("★삭제하려면 0 입력, enter 는 삭제 취소 :")
                if choice == "0":
                    map_phone.delete(Dphone)
                    map_name.delete(Dresult.value.rec.name)
                    map_phone.display()
                    map_name.display()
                    Ad.delete(Ad.getPos((Dresult.value.rec.name, Dresult.value.rec.phone, Dresult.value.rec.mail, Dresult.value.rec.addr)))
                    Ad.display()
                    print("## 주소 삭제 완료")
                else:
                    print("## 삭제 취소")
            else:
                print("{0}는 저장되지 않은 번호입니다.".format(Dphone))
