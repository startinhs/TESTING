
from __future__ import print_function
from __future__ import unicode_literals



#Hinh chu nhat
def HinhChuNhat(n):
    print("Hinh chu nhat theo for")
    for i in range(0,n):
        print("*" * n)
    print("Hinh chu nhat theo while")
    i=0
    while i<n:
        print("*" * n)
        i=i+1

#Hinh Tam giac vuong
def TamGiacVuong(n):
    print("Tam giac vuong")
    for i in range(1,n+1):
        print("*" * i)
    #Hinh Tam giac vuong nguoc
    print("Tam giac vuong nguoc")
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * i)

#Hinh Tam giac can
def TamGiacCan(n):
    print("Tam giac can")
    for i in range(1,n+1):
        s = n-i
        #print(" " * s + "*" * ((2*i)-1))
        print(" " * s, end='')
        print("*" * ((2 * i) - 1))


#Bai2.

def TimMinMax(a,n):
    n = int(input("Nhap vao gia tri n: "))
    if n<=0:
        exit()
    a=[]
    for i in range(n):
        a.append(int(input("Nhap vao gia tri phan"
                           "tu thu %d: " % (i+1))))
    print (a)
    highist = max(a)
    lowest=min(a)

    if highist<0:
        print("So duong lon nhat la: *")
    else:
        print("So duong lon nhat la: ", highist)
    if lowest>0:
        print("So am nho nhat la: *")
    else:
        print("So am nho nhat la: ", lowest)

#Bai3
def TuDien():
    dict ={'tester': 'Kiem thu vien',
           'developer': 'lap trinh vien',
           'Project manager': 'Quan ly du an'
           }
    print(dict)
    dict.update({'QA': 'Kiem soat chat luong'})
    print(dict)
    print("so phan tu: %d" %len(dict))

    co='false'
    k= raw_input("Nhap gia tri can tim:")
    #k="tester"
    for key in dict.keys():
        if key == k:
            co='true'
            break
    if co == 'false':
        print ("Khong tim thay")
    else:
        print("Tim thay")
        del dict[k]
        print(dict)


class Cau4:
    listEmployee = [
        {"MaNV": "1", "TenNV": "Nguyen Van A"},
        {"MaNV": "2", "TenNV": "Duong Trong B"},
        {"MaNV": "3", "TenNV": "Nguyen Thanh N"}
    ]
    n= len(listEmployee)

    def GetAllEmployee(self):

        for i in range(0,self.n):
            print("Ma nhan vien: {0}".format(self.listEmployee[i]["MaNV"]))
            print("Ten nhan vien: {0}".format(self.listEmployee[i]["TenNV"]))
    def FindEmployee(self, name):
        for i in range(0,self.n):
            if self.listEmployee[i]["TenNV"].find(name) !=-1:
                print("Ma nhan vien: {0}".format(self.listEmployee[i]["MaNV"]))
                print("Ten nhan vien: {0}".format(self.listEmployee[i]["TenNV"]))
    def AddEmployee(self):
        #print("Nhap ma nhan vien (int)")
        id = raw_input("Nhap ma nhan vien: ")
        #Kiem tra neu ma da ton tai thi khong them
        for i in range(0,self.n):
            if self.listEmployee[i]["MaNV"] == id:
                print("Ma NV da ton tai")
                return -1
        employeeName = raw_input("Nhap ten nhan vien: ")
        newEployee = {"MaNV": id, "TenNV": employeeName}
        self.listEmployee.append(newEployee)
        self.n = len(self.listEmployee)
        print("DS NV da cap nhat")
        self.GetAllEmployee()
    def DeleteEmployee(self,id):
        for i in range(0,self.n):
            if self.listEmployee[i]["MaNV"] == id:
                del self.listEmployee[i]
                self.n = len(self.listEmployee)
                print("DS NV sau khi xoa")
                self.GetAllEmployee()
                return
        print("Khong ton tai nhan vien")

btCau4 = Cau4()
btCau4.GetAllEmployee() #1

btCau4.FindEmployee(raw_input("Nhap tu khoa tim kiem: "))
btCau4.AddEmployee()
btCau4.DeleteEmployee(raw_input("Nhap id can xoa: "))