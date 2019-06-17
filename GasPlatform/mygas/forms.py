from django import forms
from mygas.models import *
from mygas.views import *

#登录
class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={"class":"form-control"}),
        required=True
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control"}),
        required=True
    )

#编辑用户信息表
class UserEditForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}),
        required=True
    )
    # oldpassword = forms.CharField(
    #     widget=forms.PasswordInput(attrs={"class": "form-control"}),
    #     required=True
    # )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True
    )


VALUE_TYPE = (
        ('', ''),
        ('膜式表', '膜式表'),
        ('修正仪', '修正仪'),
        ('超声波', '超声波'),
        ('IC卡-膜式表', 'IC卡-膜式表'),
        ('IC卡-修正仪', 'IC卡-修正仪'),
        ('IC卡-超声波', 'IC卡-超声波'),
    )
VALUE_STATE = (
        ('', ''),
        ('待审核', '待审核'),
        ('通过', '通过'),
        ('不通过', '不通过'),
)
VALUE_STATE0 = (
        ('', ''),
        (1, '通过'),
        (0, '不通过'),
)
VALUE_MANU = (
    ('',''),
    ('1','上海蓝宝石'),
    ('2','宁海蓝宝石'),
    ('3','上海克罗姆'),
    ('4','埃创'),
    ('5','丹东热工'),
    ('6','浙江荣鑫'),
    ('7','天津五机'),
    ('8','上海埃科'),
    ('9','浙江苍南'),
    ('10','浙江天信'),
    ('11','天信德莱塞'),
    ('12','埃尔斯特'),
    ('13','日本'),
    ('14','丹尼尔'),
    ('15','丹东思凯'),
    ('16','杭州先锋'),
    ('17','郑州安然'),
    ('18','成都千嘉'),
    ('19','杭州金卡'),
    ('20','航天动力'),
    ('21','上海佳盛'),
    ('22','上海飞奥'),
    ('23','上海众德'),
    ('24','上海金速'),
    ('25','四川海力'),
    ('26','浙江松川'),
    ('27','上海安居利'),
    ('28','宁波佳德'),
    ('29','杭州鸿鹄'),
    ('30','上海真兰'),
    ('31','山东思达特'),
    ('32','RMG'),
    ('33','FISHER'),
    ('34','其他'),
    ('35','浙江威星'),
    ('36','上海玮轩'),
    ('37','兆富电子'),
    ('38','无锡云感'),
)

#厂商用的查询/data/
class MeterQueryForm1(forms.Form):
    MeterId = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={"class":"form-control",'placeholder': '请输入表号'}),
    )
    MeterType = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_TYPE, attrs={"class": "form-control"})
    )
    Subtime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )

#厂商用的查询/dataresult/
class MeterQueryForm2(forms.Form):
    MeterId = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={"class":"form-control",'placeholder': '请输入表号'}),
    )
    MeterType = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_TYPE, attrs={"class": "form-control"})
    )
    MeterState = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_STATE,attrs={"class": "form-control"})
    )
    Subtime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )

#测试人员用的待审核/datacheck/
class MeterQueryForm3(forms.Form):
    MeterId = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={"class":"form-control",'placeholder': '请输入表号'}),
    )
    MeterType = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_TYPE, attrs={"class": "form-control"})
    )
    Subtime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )
    ManufactureName_id = forms.IntegerField(
        required=False,
        widget=forms.Select(choices=VALUE_MANU,
                            attrs={"class": "form-control"}),
    )

#测试人员用的审核结果/checkresult/
class MeterQueryForm4(forms.Form):
    MeterId = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={"class":"form-control",'placeholder': '请输入表号'}),
    )
    MeterType = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_TYPE, attrs={"class": "form-control"})
    )
    Subtime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )
    CheckTime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )
    ManufactureName_id = forms.IntegerField(
        required=False,
        widget=forms.Select(choices=VALUE_MANU,
                            attrs={"class": "form-control"}),
    )
    DataCheckedResult = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_STATE0, attrs={"class": "form-control"})
    )

#测试人员用的待分配/allocation/
class MeterQueryForm5(forms.Form):
    MeterId = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={"class":"form-control",'placeholder': '请输入表号'}),
    )
    MeterType = forms.CharField(
        required=False,
        widget=forms.Select(choices=VALUE_TYPE, attrs={"class": "form-control"})
    )
    Subtime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )
    CheckTime = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control"})
    )
    ManufactureName_id = forms.IntegerField(
        required=False,
        widget=forms.Select(choices=VALUE_MANU,
                            attrs={"class": "form-control"}),
    )

#选择表类型
class MeterTypeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MeterTypeForm, self).__init__(*args, **kwargs)
        self.fields['ManufactureName_id'].widget.choices = Manufacture.objects.all().values_list('id', 'ManufactureName')

    SELVALUE = (
        ('膜式表', '膜式表'),
        ('修正仪', '修正仪'),
        ('超声波', '超声波'),
        ('IC卡-膜式表', 'IC卡-膜式表'),
        ('IC卡-修正仪', 'IC卡-修正仪'),
        ('IC卡-超声波', 'IC卡-超声波'),
    )
    MeterId = forms.CharField(
        required=True,
        min_length=12,
        max_length=12,
        widget=forms.TextInput(attrs={"class":"form-control"})
    )   #还没有规定字符长度
    MeterType = forms.CharField(
        widget=forms.Select(choices=SELVALUE,attrs={"class":"form-control"}),
        required=True
    )
    ManufactureName_id = forms.IntegerField(
        widget=forms.Select(attrs={"class":"form-control"}),
        required=True
    )
    TimeOfProduce = forms.CharField(
        widget=forms.DateInput(attrs={"class":"form-control"}),
        required=True
    )

#IC卡
class Meter_ICForm(forms.Form):
    # MeterId = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),required=True)
    #计费数据
    ChargingStatusWord = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CurrentVol = forms.DecimalField(max_digits=12, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RemainingSum = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CumulativeSum = forms.DecimalField(max_digits=12, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CurrentPrice = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CurrentPriceInitialVol = forms.DecimalField(max_digits=12, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    LastPrice = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    LastPriceInitialVol = forms.DecimalField(max_digits=12, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ChargingTime = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##设置延时价格体系
    VerComparison = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceSysDate = forms.CharField(max_length=10,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceMode = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceSysVer = forms.CharField(max_length=4,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceNormal = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceSysCycle = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceCycleDate = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceClearSign = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##第一阶段
    PriceEndDateOne = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOne1 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOneAmount1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOne2 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOneAmount2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOne3 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##第二阶段
    PriceEndDateTwo = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwo1 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwoAmount1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwo2 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwoAmount2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwo3 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##第三阶段
    PriceEndDateThree = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThree1 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThreeAmount1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThree2 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThreeAmount2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThree3 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##第四阶段
    PriceEndDateFour = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFour1 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFourAmount1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFour2 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFourAmount2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFour3 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##第五阶段
    PriceEndDateFive = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFive1 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFiveAmount1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFive2 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFiveAmount2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFive3 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ##当前价格体系
    PriceSysDate_C = forms.CharField(max_length=10,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceSysCycle_C = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceMode_C = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False) # 常规01 其他02
    PriceCycleDate_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceSysVer_C = forms.CharField(max_length=4,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceClearSign_C = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)  # 01清 00不清
    PriceNormal_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    DelayExists_C = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)  # 0不存在  1存在
    ## 第一阶段
    PriceEndDateOne_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOne1_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOneAmount1_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOne2_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOneAmount2_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceOne3_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ## 第二阶段
    PriceEndDateTwo_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwo1_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwoAmount1_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwo2_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwoAmount2_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceTwo3_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ## 第三阶段
    PriceEndDateThree_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThree1_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThreeAmount1_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThree2_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThreeAmount2_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceThree3_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ## 第四阶段
    PriceEndDateFour_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFour1_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFourAmount1_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFour2_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFourAmount2_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFour3_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ## 第五阶段
    PriceEndDateFive_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFive1_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFiveAmount1_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFive2_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFiveAmount2_C = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PriceFive3_C = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    # 卡片充值记录
    RechargeDate1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RemainingSumBefore1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeSum1 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeDate2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RemainingSumBefore2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeSum2 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeDate3 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RemainingSumBefore3 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeSum3 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeDate4 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RemainingSumBefore4 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeSum4 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeDate5 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RemainingSumBefore5 = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    RechargeSum5 = forms.CharField(max_length=8,initial="FFFFFFFF",widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

#膜式表
class Meter_MSBForm(forms.Form):
    # MeterId = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)

    Com_no_msb = forms.CharField(max_length=16,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Sw_rlse_msb = forms.CharField(max_length=4,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    Real_vol = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Meter_v = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Temperature_msb = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Status = forms.CharField(max_length=4,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    DropMeter1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    DropMeter2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ReverseInstall1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    ReverseInstall2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    MeasureBreakdown1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    MeasureBreakdown2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    TSensorBreakdown1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    TSensorBreakdown2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PSensorBreakdown1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    PSensorBreakdown2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    TrafficAbnormality1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    TrafficAbnormality2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ComVol1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    ComVol2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    BaseVol1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    BaseVol2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CollectFault1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CollectFault2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    GasLeakClose1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    GasLeakClose2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    GasStolenClose1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    GasStolenClose2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ResetClose1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    ResetClose2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    LowVolClose1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    LowVolClose2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    CollectClose1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CollectClose2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    CommandClose1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    CommandClose2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ManulOpen1_msb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    ManulOpen2_msb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    #FTP远程升级数据
    FTPUserName_msb = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control"}),required=True,initial='01')
    FTPPassword_msb = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control"}),required=True,initial='01')
    FTPAddress_msb = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True,initial='139.199.191.23')
    FTPCatalog_msb = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}),required=True,initial='D:\FTPPoint\File')
    FileName_msb = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class":"form-control"}),required=True)

#修正仪
class Meter_XZYForm(forms.Form):
    # MeterId = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)

    Com_no_xzy = forms.CharField(max_length=16,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    Sw_rlse_xzy = forms.CharField(max_length=4,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)

    MeterNum = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),required=False)

    Temperature_xzy = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    Disturb_Total_Vol = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    Pressure = forms.CharField(max_length=8,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)

    Correction_E = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    Stan_Total_Vol = forms.DecimalField(max_digits=12, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    Stan_Ins_Ele_xzy = forms.DecimalField(max_digits=6, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    Work_Total_Vol = forms.DecimalField(max_digits=12, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Work_Ins_Ele_xzy = forms.DecimalField(max_digits=6, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    DropMeter1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    DropMeter2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ReverseInstall1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    ReverseInstall2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    MeasureBreakdown1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    MeasureBreakdown2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    TSensorBreakdown1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    TSensorBreakdown2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PSensorBreakdown1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    PSensorBreakdown2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    TrafficAbnormality1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}),required=False)
    TrafficAbnormality2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ComVol1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    ComVol2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    BaseVol1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    BaseVol2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CollectFault1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CollectFault2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    GasLeakClose1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    GasLeakClose2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    GasStolenClose1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    GasStolenClose2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ResetClose1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    ResetClose2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    LowVolClose1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    LowVolClose2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    CollectClose1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CollectClose2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    CommandClose1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CommandClose2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ManulOpen1_xzy = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    ManulOpen2_xzy = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    # FTP远程升级数据
    FTPUserName_xzy = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='01')
    FTPPassword_xzy = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='01')
    FTPAddress_xzy = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='139.199.191.23')
    FTPCatalog_xzy = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='D:\FTPPoint\File')
    FileName_xzy = forms.CharField(max_length=8, widget=forms.TextInput(attrs={"class": "form-control"}),required=True)

#超声波
class Meter_CSBForm(forms.Form):
    # MeterId = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True)

    Com_no_csb = forms.CharField(max_length=16,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Sw_rlse_csb = forms.CharField(max_length=4,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    Vol1 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Stan_Ins_Ele_csb = forms.DecimalField(max_digits=6, decimal_places=3,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Vol2 = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Work_Ins_Ele_csb = forms.DecimalField(max_digits=6, decimal_places=3,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    MeterStateWord = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Temperature_csb = forms.DecimalField(max_digits=4, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    MeterInStateWord = forms.CharField(max_length=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PValue = forms.DecimalField(max_digits=8, decimal_places=3,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Stan_Total_Ele = forms.DecimalField(max_digits=10, decimal_places=3,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Peak_Ele = forms.DecimalField(max_digits=6, decimal_places=3,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    Work_Total_Ele = forms.DecimalField(max_digits=10, decimal_places=3,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    DropMeter1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    DropMeter2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ReverseInstall1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    ReverseInstall2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    MeasureBreakdown1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    MeasureBreakdown2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    TSensorBreakdown1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    TSensorBreakdown2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    PSensorBreakdown1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    PSensorBreakdown2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    TrafficAbnormality1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    TrafficAbnormality2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ComVol1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    ComVol2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    BaseVol1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    BaseVol2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    CollectFault1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CollectFault2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    GasLeakClose1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    GasLeakClose2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    GasStolenClose1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control"}),required=False)
    GasStolenClose2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    ResetClose1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    ResetClose2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    LowVolClose1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    LowVolClose2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    CollectClose1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CollectClose2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    CommandClose1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    CommandClose2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ManulOpen1_csb = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}), required=False)
    ManulOpen2_csb = forms.DecimalField(max_digits=8, decimal_places=2,widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    AF_ULimit1 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_DLimit1 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_LLimit1 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_ULimit2 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_DLimit2 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_LLimit2 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_ULimit3 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_DLimit3 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)
    AF_LLimit3 = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),required=False)

    # FTP远程升级数据
    FTPUserName_csb = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='01')
    FTPPassword_csb = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='01')
    FTPAddress_csb = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='139.199.191.23')
    FTPCatalog_csb = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=True, initial='D:\FTPPoint\File')
    FileName_csb = forms.CharField(max_length=8, widget=forms.TextInput(attrs={"class": "form-control"}),required=True)


