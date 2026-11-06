#abstraction

from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def check_bal():
        pass
    @abstractmethod
    def withdraw():
        pass
    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def update_pin():
        pass
class NewATM(ATM):
    name='ICICI'
    loc='vijaynagar'
    def __init__(self,name,accno,pin,bal):
        self.name=name
        self.accno=accno
        self.pin=pin
        self.bal=bal
    def check_bal(self):
        p=int(input("enter your atm pin:"))
        if p==self.pin:
            print('the available bal is:',self.bal)
        else:
            print('invalid pin')
    def update_pin(self):
        p=int(input("enter your existing atm pin:"))
        if p==self.pin:
            new=int(input("enter your new pain:"))
            self.pin=new
            print('pin upadated successfully')
        else:
            print('invalid pin')
    def deposit(self):
        p=int(input("enter your existing atm pin:"))
        if p==self.pin:
            amount=int(input("enter the amount to deposit:"))
            self.bal=self.bal+amount
            print('deposit successfull')
        else:
            print('invalid pin')
    def withdraw(self):
         p=int(input("enter your existing atm pin:"))
         if p==self.pin:
            amount=int(input("enter the amount to withdraw:"))
            if self.bal>+amount:
               self.bal=self.bal-amount
               print('withdraw successfull')
            else:
                print('insufficient balance')
         else:
            print('invalid pin')

c1=NewATM('Anu',987655458787656,1234,25000)
#output
'''c1.check_bal()
enter your atm pin:456
invalid pin
c1.check_bal()
enter your atm pin:1234
the available bal is: 25000
c1.update_pin()
enter your existing atm pin:1234
enter your new pain:4321
pin upadated successfully
c1.deposit()
enter your existing atm pin:4321
enter the amount to deposit:20000
deposit successfull
c1.withdraw()
enter your existing atm pin:4321
enter the amount to deposit:5000
withdraw successfull
c1.check_bal()
enter your atm pin:4321
the available bal is: 40000'''
'''def operations(obj):
    print('enter 1'''
       
    
    
    










'''PRINT ALSO WILL NOT WORK-->IMPLEMENTATION WILL NOT WPRK
C1.check_bal'''
