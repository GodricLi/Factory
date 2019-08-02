# _*_ coding=utf-8 _*_


from abc import ABCMeta, abstractmethod

"""
不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品的实例
优点：1隐藏对象创建的实现细节
      2客户端不需要修改代码
缺点：每增加一个角色就需要增加一个类

"""


class Payment(metaclass=ABCMeta):
    """抽象产品角色"""

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    """具体产品角色"""

    def __init__(self, hb=False):
        self.hb = hb

    def pay(self, money):
        if self.hb:
            print("花呗支付%s元" % money)
        else:
            print("支付宝支付%s元" % money)


class WechatPay(Payment):
    """具体产品角色"""

    def pay(self, money):
        print("微信支付%s元" % money)


class Factory(metaclass=ABCMeta):
    """工厂角色"""

    @abstractmethod
    def create_payment(self, method):
        pass


class AliPayment(Factory):

    def create_payment(self, method):
        if method == 'hb':
            return Alipay(hb=True)
        return Alipay()


class WechatPayment(Factory):

    def create_payment(self, method):
        return WechatPay()


# client 调用代码层
pf = AliPayment()
p = pf.create_payment('hb')
p.pay(100)
