class Bai1:
    def HinhVuong(sefl, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()
        print("-------")
    def HinhTamGiac(sefl, n):
        #TamGiac vuong
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()
        print("-------")
        #TamGiac vuong nguoc
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(i + 1):
                print("*", end="")
            print()
        print("-------")
        #TamGiac can
        for i in range(1, n+1):
                for j in range(n-i):
                    print(" ", end="")
                for j in range((2*i)-1):
                    print("*", end="")
                print()
        print("-------")
        #TamGiac deu lay tu tam giac can
        for i in range(1, int((n+1)/2)+1):
                for j in range(n-i):
                    print(" ", end="")
                for j in range((2*i)-1):
                    print("*", end="")
                print()
        print("-------")
        #TamGiac deu chay tu vong lap
        for i in range(n+1):
            if(i%2!=0):
                for j in range((n-i)//2):
                    print(" ", end="")
                for j in range(i):
                    print("*", end="")
                print()
    def inHinhTheoDinhDang(self, n):
        for i in range(1, n+1):
            print("*" * n)
        print("-------")
        for i in range(1, n+1):
            print(("*" * i).ljust(n))
        print("-------")
        for i in range(1, n+1):
            print(("*" * i).rjust(n))
        print("-------")
        for i in range(1, n+1):
            if i%2!=0:
                print(("*" * i).center(n))
        print("-------")

class Bai2:
    def inputList(self):
        n = int(input("So phan tu: "))
        a =[]
        for i in range(n):
            a.append(int(input("Phan tu thu %d: "%(i+1))))
        return a
    def minMax(self, a, n):
        minA = min(a)
        maxD = max(a)
        if maxD < 0:
            print("So duong lon nhat: *")
        else:
            print("So duong lon nhat: ", maxD)

        if minA > 0:
            print("So am be nhat: *")
        else:
            print("So am be nhat: ", minA)

class Bai3:
    Dict = {'Developer':'lap trinh vien', 'Tester':'Kiem thu vien'}
    def addItem(self, key, value):
        if (key not in self.Dict.keys()):
            self.Dict[key] = value
    def printItems(self):
        return self.Dict.items()
    def printLength(self):
        return len(self.Dict)
    def find_EN(self, key):
        if(key in self.Dict.keys()):
            return key, self.Dict[key]
        else: print("Khong tim thay!!"); return
    def deleteItem(self, key):
        if (key in self.Dict.keys()):
            del self.Dict.key
            # self.Dict.pop(key)
            print("Xoa thanh cong!!")
            return
        else: print ("Xoa that bai!!"); return

class Bai4:
    employees = [{
        "ma_nv": 1,
        "ten_nv": "Nguyễn Văn A",
    }, {
        "ma_nv": 2,
        "ten_nv": "Dương Trọng C",
    }, {
        "ma_nv": 3,
        "ten_nv": "Nguyễn Thanh N",
    }]
    n = len(employees)
    def printItems(self):
        for i in range(0, self.n):
            print("Ma nhan vien: {0}".format(self.employees[i]["ma_nv"]))
            print("Ten nhan vien: {0}".format(self.employees[i]["ten_nv"]))
    def findItem(self, keyword):
        for i in range(0, self.n):
            if(self.employees[i]["ten_nv"].find(keyword) != -1):
                print("Ma nhan vien: {0}".format(self.employees[i]["ma_nv"]))
                print("Ten nhan vien: {0}".format(self.employees[i]["ten_nv"]))
    def deleteItem(self, id):
        for i in range(0, self.n):
            if (self.employees[i]["ma_nv"] == id):
                del self.employees[i]
                self.n = len(self.employees)
                print(self.n)
                self.printItems()
                return
    def addItem(self):
        id = str(input("Nhap ma nhan vien: "))
        for i in range(0, self.n):
            if (self.employees[i]["ma_nv"] == str(id)):
                print("Ma nhan vien da ton tai!")
                return -1

        name = str(input("Nhap ten nhan vien: "))
        newItem = {'ma_nv':id, 'ten_nv': name}
        self.employees.append(newItem)
        self.n = len(self.employees)
        print(self.n)
        self.printItems()
        return

# n = int(input("Enter number: "))
# bt1 = Bai1()
# # bt1.HinhVuong(n)
# # bt1.HinhTamGiac(n)
# bt1.inHinhTheoDinhDang(n)
# bt2 = Bai2()
# a = bt2.inputList()
# print(a)
# bt2.minMax(a, len(a))
# bt3 = Bai3()
# bt3.addItem("a","b")
# print(bt3.printItems())
# print(bt3.printLength())
# print(bt3.find_EN("Tester"))
# print(bt3.deleteItem("a"))
# print(bt3.printItems())

bt4 = Bai4()
bt4.printItems()
bt4.findItem("Thanh")
bt4.deleteItem(3)
bt4.addItem()