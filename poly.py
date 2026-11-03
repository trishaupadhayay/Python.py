class cashPayment:
    def pay(self,amount):
        print("Paid",amount,"using cash")

class UPIPayment:
    def upipay(self,amount):
        print("paid",amount,"using UPI")

class CardPayment:
    def pay(self,amount):
        print("paid",amount,"using card")

class NetBanking:
    def pay(self,amount):
        print("Paid",amount,"using NetBanking")


choice=input("choose payment method (cash/upi/card/netbanking):")
if choice == "cash":
    payment=cashPayment()
elif choice == "upi":
    payment= UPIPayment()
elif choice == "card":
    payment = CardPayment()
elif choice == "netbanking":
    payment = NetBanking()
    exit()


payment.pay(1000)    

class Notification:
    def send_notification(self):
        pass


class MobilePush(Notification):
    def send_notification(self):
        print("Sending Mobile Push Notification")


class Email(Notification):
    def send_notification(self):
        print("Sending Email Notification")


class SMS(Notification):
    def send_notification(self):
        print("Sending SMS Notification")

n1 = MobilePush()
n2 = Email()
n3 = SMS()


n1.send_notification()
n2.send_notification()
n3.send_notification()