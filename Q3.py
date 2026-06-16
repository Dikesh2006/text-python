from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def receipt(self):
        pass

1
class GPay(Payment):

    def pay(self):
        print("Payment done using GPay")

    def receipt(self):
        print("GPay Receipt Generated")



class CreditCard(Payment):

    def pay(self):
        print("Payment done using Credit Card")

    def receipt(self):
        print("Credit Card Receipt Generated")



g = GPay()
c = CreditCard()


g.pay()
g.receipt()

c.pay()
c.receipt()