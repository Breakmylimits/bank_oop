users = [
    {"name":"Aris", "money": 1500,"phone":"0643197367"},
    {"name":"Justin", "money": 1000000,"phone":"0753254780"},
    {"name":"Ai", "money": 4000,"phone":"0547854726"},
    {"name":"Meepo", "money": 500,"phone":"2365412598"},
    {"name":"Donut", "money": 30000,"phone":"0125415635"},
    {"name":"Jose", "money": 500,"phone":"0541235983"},
    {"name":"Destro", "money": 543500,"phone":"0542157836"},
    {"name":"Aui", "money": 560040000,"phone":"0245251256"},
    {"name":"Bee", "money": 700,"phone":"0254785457"},
    {"name":"Maple", "money": 740,"phone":"0247154698"},
    {"name":"Dart", "money": 2100,"phone":"03256478956"},
    {"name":"Alpha", "money": 5000,"phone":"0132546987"},
    {"name":"John", "money": 1000,"phone":"0912545379"},
    {"name":"Molly", "money": 5410,"phone":"0812532014"},
    {"name":"Gosh", "money": 400,"phone":"0736225648"},
    {"name":"Foo", "money": 65420,"phone":"0542176323"},
    {"name":"Will", "money": 1200,"phone":"086215432"},
    {"name":"Bible", "money": 50000,"phone":"0365124595"},
    {"name":"Cee", "money": 548120000,"phone":"08561423562"},
    {"name":"Jeab", "money": 20000,"phone":"0642516354"},
    {"name":"Micky", "money": 57800,"phone":"0214365873"},
    {"name":"Alexander", "money": 2500,"phone":"0865425698"},
    {"name":"Jor", "money": 2000000000,"phone":"0564223651"},
    {"name":"Calvin", "money": 7700,"phone":"0514265397"},
    {"name":"Demon", "money": 666,"phone":"0975485431"},
    {"name":"Geoge", "money": 7,"phone":"0631452369"},
    {"name":"Carl", "money": 55500,"phone":"04216536257"},
    {"name":"Domon", "money": 77000,"phone":"0236521487"},
]


class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
    def deposit(self, money):
        self.money =+ money

    def withdraw(self, money):
        self.money =- money

   
    def __str__(self):
        return "<{}>:<{}>".format(self.name ,self.money)  


class MobileBanking(BankAccount):
    
    def __init__(self, name, money, phone):
            super().__init__(name, money)  
            self.phone = phone
               
    @staticmethod  
    def check(self, money):
        if money >= money:
            print("ไม่สามารถถอนเงินได้")
        elif money < money:
            print("สามารถถอนเงินได้")
    
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,money):
        if money >= 500:
            self.__money =  money
        else :
            raise ValueError("ต้องมีเงินอย่างน้อย 500 บาท")


    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self,phone):
        if phone == None:
            raise ValueError("ไม่ได้ใส่เบอร์โทรศัพท์")
        else :
            self.__phone = phone
    
            
    def __str__(self):
        return "{}".format(super().__str__())

    

   
        
        


if __name__ == "__main__":
    
    
    s2 =BankAccount("Aris",400)
    print(s2)
    s4 =MobileBanking("Aris",1500, "0643197367")
    print(s4)
    print(s4)
  
    newusers = []
    for ojt in users:
        n = list(ojt.values())
        newusers.append(n)
        resuit=sorted(newusers)
    print(newusers)
    print("-"*100)
    print(resuit)

    for user in resuit:
        data=BankAccount(user[0],user[1])
        print(data)
    print("-"*100)
    for user in resuit:
        data2=MobileBanking(user[0],user[1],user[2])
        #newusers.append(data2) 
        print(data2)
       
        

        
        

    
    
   

   
   
        



"""
ในสถาการณ์นี้เรามี 
==============
1. List 'users' ที่เก็บข้อมูลของ user ทุกคน
2. class 'BankAccount' เพื่อการทำธุรกรรมกับธนาคาร ฝากเงิน และ ถอนเงิน

โจทย์
====
-1. สร้าง class ใหม่ขึ้นมาชื่อว่า 'MobileBanking' ซึ่งมี function พื้นฐานเหมือน class 'BankAccount'
-2. ใน class MobileBanking ให้ใส่ข้อมูลเบอร์โทรศัพท์ของ user เพิ่ม
-3. ใน class MobileBanking ต้องสามารถแสดงข้อมูลของ user ใน format '<name>: <money>' ได้
4. ใน class MobileBanking ดัดแปลง function withdraw ให้ทำการเช็คก่อนว่า user มีเงินพอต่อการถอนหรึ่อไม่
-5. ใน class MobileBanking จำเป็นต้องเช็คก่อนว่าต้องมีเงืนอย่างน้อย 500 บาท และมีเบอร์โทรศัพท์จึงจะสามารถเปิดบัญชีได้(สร้าง instance)
-6. จากข้อ 5. สร้าง instance ของ MobileBanking โดยใช้ List 'users' 
-7. จากข้อ 6. สามารถแสดงข้อมูลทุกคนที่ลงทะเบียนใน MobileBanking โดยเรียงตามตัวอักษรของชื่อ user
8. จากข้อ 6. สามารถแสดงข้อมูลทุกคนที่ลงทะเบียนใน MobileBanking โดยเรียงตามจำนวนเงินจากมากไปน้อย
-9. BankAccount มีอะไรผิดไป"""

"""  for ojt in users:
        n = list(ojt.values())
        n.sort()
        n.append(newusers)
        print(newusers)
        
         def __lt__(self, other):
        if self.money == other.money:
            return self.name < other.name
        else:
            return self.money > other.money
          
        
        
        """
