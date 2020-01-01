from django.db import models

class Goods(models.Model):
    img_url = models.ImageField(verbose_name='商品缩略图', blank=True, null=True)
    price = models.DecimalField(verbose_name='价格',max_digits=7,decimal_places=2)
    detail = models.TextField(verbose_name='商品详情',blank=True, null=True)
    desc = models.TextField(verbose_name='说明',blank=True, null=True)
    lease_price = models.DecimalField(verbose_name='租用价格',max_digits=7,decimal_places=2)
    lease_deposit = models.DecimalField(verbose_name='租用押金',max_digits=7, decimal_places=2)


class User(models.Model):
    name = models.CharField(verbose_name='用户名',max_length=64)
    mobile = models.CharField(verbose_name='注册手机号码',max_length=24)
    bank = models.CharField(verbose_name='开户行', max_length=24)
    account = models.CharField(verbose_name='账号', max_length=24)
    vx = models.CharField(verbose_name='微信', max_length=24)
    alipay = models.CharField(verbose_name='支付宝', max_length=24)
    password = models.CharField(verbose_name='密码', max_length=64)
    re_moble = models.CharField(verbose_name='推荐人手机号码', max_length=24)
    wle_income = models.DecimalField(verbose_name='批发收益',max_digits=8, decimal_places=2)
    retail_income = models.DecimalField(verbose_name='零售收益', max_digits=8, decimal_places=2)
    token = models.CharField(verbose_name='登录token', max_length=64)
    refresh_token = models.CharField(verbose_name='刷新token', max_length=64)
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    last_login_time = models.DateTimeField(verbose_name='最后登录时间2',auto_now_add=True)
    score = models.IntegerField(verbose_name='积分', null=True, blank=True)


class Order(models.Model):
    order_sn = models.CharField(verbose_name='订单号', max_length=64)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, verbose_name='商户', on_delete=models.CASCADE, related_name='seller_id')
    type_buy = models.CharField(verbose_name='购买方式', max_length=16)
    price = models.DecimalField(verbose_name='价格', max_digits=8, decimal_places=2)
    shipping_status = models.SmallIntegerField(verbose_name='发货状态',default=0)
    createtime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    pay_status = models.SmallIntegerField(verbose_name='订单状态', default=0)
    pay_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    pay_way = models.CharField(verbose_name='订单号', max_length=64)
    pay_get_raw = models.TextField(verbose_name='支付信息')
    pay_raw = models.TextField(verbose_name='支付信息')
    status = models.SmallIntegerField(verbose_name='收货状态',default=0)
