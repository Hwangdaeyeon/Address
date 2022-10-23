import os

class Menu:
    """description of class"""
    def __init__(self, title, contents):
        self.__title=title
        self.__contents=contents
        self.__menuNumber=1

    @property
    def MenuNumber(self):
        return self.__menuNumber
    @property
    def ExitMenuNumber(self):
        return len(self.__contents)+1

    def print(self):
        os.system("cls")
        print("\n\n\n\n\n")
        print("\t\t================================")
        print("\t\t\t",end="")
        print(self.__title)
        print("\n")
        i=0
        for content in self.__contents:
            print("\t\t", end="")
            i=i+1
            print(i,end=". ")
            print(content)
            print()

        print("\t\t", end="")
        i=i+1
        print(i,end=". ")
        print("종료")
        print("\n\t\t================================")
        print("\n\t\t$$번호 입력 : ", end=' ')


    def getMenuNumber(self):
        try:
            self.__menuNumber = int(input())
            if 1<= self.__menuNumber <=self.ExitMenuNumber:
                return self.__menuNumber
            else:
                raise Exception("숫자가 범위를 멋어 났습니다.")
        except ValueError as e:
            print()
            print("숫자를 입력하지 않았습니다.")
        except Exception as e:
            print()
            print(e)
        input()
        return - 1

    def read(self):
        #self.__menuNumber=int(input())
        #return self.__menuNumber
        self.__menuNumber = self.getMenuNumber()
        while self.__menuNumber < 0:
            self.print()
            self.__menuNumber = self.getMenuNumber()
        return self.__menuNumber

    def printNread(self):
        self.print()
        self.read()

    def isExitNumber(self):
        if self.__menuNumber==(len(self.__contents)+1):
            return True
        else:
            return False

