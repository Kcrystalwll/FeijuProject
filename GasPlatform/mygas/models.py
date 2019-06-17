from django.db import models
from rbac.models import User_info
from django.contrib.auth.models import User

# Create your models here.
#管理所有厂商
class Manufacture(models.Model):
    ManufactureName = models.CharField(max_length=30,verbose_name="生产厂商")
    code = models.CharField(max_length=2,verbose_name="生产厂商代码")

    class Meta:
        verbose_name_plural = "生产厂商表"
        verbose_name = "生产厂商"

    def __str__(self):
        return  self.ManufactureName

class GS_MeterTypeInfo(models.Model):
    user = models.ForeignKey(User_info)  # 和登录用户相连(录入人员）
    check_user = models.CharField(max_length=50,null=True)  #审核人员
    allo_user = models.CharField(max_length=50,null=True)  #分配人员

    MeterId = models.CharField(unique=True,max_length=12)  # 表号 设备类型+厂商代码+年月日+生产流水号
    # 燃气表表类型编号  00膜式表  01修正仪  03超声波  20IC卡-膜式表  21IC卡-修正仪  23IC卡-超声波
    MeterType = models.CharField(max_length=10)
    TimeOfProduce = models.DateField()  # 燃气表生产日期
    ManufactureName = models.ForeignKey('Manufacture')  # 燃气表生产厂商  Manufacture_id
    Subtime = models.DateTimeField(null=True)  # 提交时间
    CheckTime = models.DateTimeField(null=True)  # 审核时间

    IsSubmit = models.BooleanField(default=0)  # 是否提交 1提交  0未提交

    IsDataChecked = models.BooleanField(default=0)  # 数据是否审核 1已审核 0待审核
    DataCheckedResult = models.BooleanField(default=0)  # 审核结果 1通过 0不通过

    IsAllocated = models.BooleanField(default=0)  # 是否分配  1已分配  0未分配
    # 分配结果
    CommandTest = models.CharField(max_length=10,null=True)
    ICTest = models.CharField(max_length=10,null=True)
    ChuTest = models.CharField(max_length=10,null=True)
    ZhoTest = models.CharField(max_length=10,null=True)
    MianTest = models.CharField(max_length=10,null=True)
    MeterPrivilege = models.CharField(max_length=1, default="0")  # 优先

    IsTest = models.BooleanField(default=0)  # 是否测试入库  1测试完成 0测试未完成

    #测试人员可以是登录用户
    TestUnit = models.CharField(max_length=50,default='上海燃气有限公司')

    class Meta:
        ordering = ['-Subtime']   #从大到小排序

#IC卡数据表
class GS_MeterInfo_IC(models.Model):
    MeterTypeId=models.OneToOneField('GS_MeterTypeInfo',unique=True,null=True)
    MeterId = models.CharField(max_length=12,unique=True)
    ##计费数据
    ChargingStatusWord = models.CharField(max_length=2,null=True)
    CurrentVol = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    RemainingSum = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    CumulativeSum = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    CurrentPrice = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    CurrentPriceInitialVol = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    LastPrice = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    LastPriceInitialVol = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    ChargingTime = models.CharField(max_length=8,null=True)
    ##设置延时价格体系
    VerComparison = models.CharField(max_length=2,null=True)
    PriceSysDate = models.CharField(max_length=10,null=True)
    PriceMode = models.CharField(max_length=2,null=True) #常规01 其他02
    PriceSysVer = models.CharField(max_length=4,null=True)
    PriceNormal = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceSysCycle = models.CharField(max_length=2,null=True)
    PriceCycleDate = models.CharField(max_length=8,null=True)
    PriceClearSign = models.CharField(max_length=2,null=True)  #01清 00不清
    ##第一阶段
    PriceEndDateOne = models.CharField(max_length=8,null=True)
    PriceOne1 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceOneAmount1 = models.CharField(max_length=8,null=True)
    PriceOne2 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceOneAmount2 = models.CharField(max_length=8,null=True)
    PriceOne3 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ##第二阶段
    PriceEndDateTwo = models.CharField(max_length=8,null=True)
    PriceTwo1 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceTwoAmount1 = models.CharField(max_length=8,null=True)
    PriceTwo2 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceTwoAmount2 = models.CharField(max_length=8,null=True)
    PriceTwo3 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ##第三阶段
    PriceEndDateThree = models.CharField(max_length=8,null=True)
    PriceThree1 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceThreeAmount1 = models.CharField(max_length=8,null=True)
    PriceThree2 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceThreeAmount2 = models.CharField(max_length=8,null=True)
    PriceThree3 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ##第四阶段
    PriceEndDateFour = models.CharField(max_length=8,null=True)
    PriceFour1 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFourAmount1 = models.CharField(max_length=8,null=True)
    PriceFour2 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFourAmount2 = models.CharField(max_length=8,null=True)
    PriceFour3 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ##第五阶段
    PriceEndDateFive = models.CharField(max_length=8,null=True)
    PriceFive1 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFiveAmount1 = models.CharField(max_length=8,null=True)
    PriceFive2 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFiveAmount2 = models.CharField(max_length=8,null=True)
    PriceFive3 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ##当前价格体系
    PriceSysDate_C = models.CharField(max_length=10,null=True)
    PriceSysCycle_C = models.CharField(max_length=2,null=True)
    PriceMode_C = models.CharField(max_length=2,null=True) #常规01 其他02
    PriceCycleDate_C = models.CharField(max_length=8,null=True)
    PriceSysVer_C = models.CharField(max_length=4,null=True)
    PriceClearSign_C = models.CharField(max_length=2,null=True)  #01清 00不清
    PriceNormal_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    DelayExists_C = models.CharField(max_length=2,null=True) #0不存在  1存在
    ## 第一阶段
    PriceEndDateOne_C = models.CharField(max_length=8,null=True)
    PriceOne1_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceOneAmount1_C = models.CharField(max_length=8,null=True)
    PriceOne2_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceOneAmount2_C = models.CharField(max_length=8,null=True)
    PriceOne3_C= models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ## 第二阶段
    PriceEndDateTwo_C = models.CharField(max_length=8,null=True)
    PriceTwo1_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceTwoAmount1_C = models.CharField(max_length=8,null=True)
    PriceTwo2_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceTwoAmount2_C = models.CharField(max_length=8,null=True)
    PriceTwo3_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ## 第三阶段
    PriceEndDateThree_C = models.CharField(max_length=8,null=True)
    PriceThree1_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceThreeAmount1_C = models.CharField(max_length=8,null=True)
    PriceThree2_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceThreeAmount2_C = models.CharField(max_length=8,null=True)
    PriceThree3_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ## 第四阶段
    PriceEndDateFour_C = models.CharField(max_length=8,null=True)
    PriceFour1_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFourAmount1_C = models.CharField(max_length=8,null=True)
    PriceFour2_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFourAmount2_C = models.CharField(max_length=8,null=True)
    PriceFour3_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ## 第五阶段
    PriceEndDateFive_C = models.CharField(max_length=8,null=True)
    PriceFive1_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFiveAmount1_C = models.CharField(max_length=8,null=True)
    PriceFive2_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    PriceFiveAmount2_C = models.CharField(max_length=8,null=True)
    PriceFive3_C = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    ##卡片充值记录
    RechargeDate1 = models.CharField(max_length=8, null=True)
    RemainingSumBefore1 = models.CharField(max_length=8, null=True)
    RechargeSum1 = models.CharField(max_length=8, null=True)
    RechargeDate2 = models.CharField(max_length=8, null=True)
    RemainingSumBefore2 = models.CharField(max_length=8, null=True)
    RechargeSum2 = models.CharField(max_length=8, null=True)
    RechargeDate3 = models.CharField(max_length=8, null=True)
    RemainingSumBefore3 = models.CharField(max_length=8, null=True)
    RechargeSum3 = models.CharField(max_length=8, null=True)
    RechargeDate4 = models.CharField(max_length=8, null=True)
    RemainingSumBefore4 = models.CharField(max_length=8, null=True)
    RechargeSum4 = models.CharField(max_length=8, null=True)
    RechargeDate5 = models.CharField(max_length=8, null=True)
    RemainingSumBefore5 = models.CharField(max_length=8, null=True)
    RechargeSum5 = models.CharField(max_length=8, null=True)

#膜式表数据表
class GS_MeterInfo_MSB(models.Model):
    MeterTypeId = models.OneToOneField('GS_MeterTypeInfo', unique=True, null=True)
    MeterId=models.CharField(max_length=12,unique=True)

    #常规数据（供初检用）
    Com_no_msb=models.CharField(max_length=16,null=True)
    Sw_rlse_msb=models.CharField(max_length=4,null=True)

    Real_vol=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    Meter_v=models.DecimalField(max_digits=4,decimal_places=2,null=True)
    Temperature_msb=models.DecimalField(max_digits=4,decimal_places=2,null=True)
    Status=models.CharField(max_length=4,null=True)

    DropMeter1_msb=models.DateTimeField(null=True)
    DropMeter2_msb=models.DecimalField(max_digits=8,decimal_places=2,null=True)
    ReverseInstall1_msb=models.DateTimeField(null=True)
    ReverseInstall2_msb=models.DecimalField(max_digits=8,decimal_places=2,null=True)
    MeasureBreakdown1_msb=models.DateTimeField(null=True)
    MeasureBreakdown2_msb=models.DecimalField(max_digits=8,decimal_places=2,null=True)
    TSensorBreakdown1_msb=models.DateTimeField(null=True)
    TSensorBreakdown2_msb=models.DecimalField(max_digits=8,decimal_places=2,null=True)
    PSensorBreakdown1_msb=models.DateTimeField(null=True)
    PSensorBreakdown2_msb=models.DecimalField(max_digits=8,decimal_places=2,null=True)
    TrafficAbnormality1_msb=models.DateTimeField(null=True)
    TrafficAbnormality2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    ComVol1_msb = models.DateTimeField(null=True)
    ComVol2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    BaseVol1_msb = models.DateTimeField(null=True)   #计量电压低
    BaseVol2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    CollectFault1_msb = models.DateTimeField(null=True) #采集故障
    CollectFault2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    GasLeakClose1_msb = models.DateTimeField(null=True)
    GasLeakClose2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    GasStolenClose1_msb = models.DateTimeField(null=True)
    GasStolenClose2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    ResetClose1_msb = models.DateTimeField(null=True)
    ResetClose2_msb = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    LowVolClose1_msb = models.DateTimeField(null=True)  #计量低电压关阀
    LowVolClose2_msb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CollectClose1_msb = models.DateTimeField(null=True)  # 超声波计量故障关阀
    CollectClose2_msb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CommandClose1_msb = models.DateTimeField(null=True)  # 关阀指令关阀
    CommandClose2_msb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ManulOpen1_msb = models.DateTimeField(null=True)  # 人工开阀
    ManulOpen2_msb = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    #程序远程升级数据
    FTPUserName_msb = models.CharField(max_length=25,default='01')
    FTPPassword_msb = models.CharField(max_length=25,default='01')
    FTPAddress_msb = models.CharField(max_length=50,default='139.199.191.23')
    FTPCatalog_msb = models.CharField(max_length=50,default='D:\FTPPoint\File')
    FileName_msb = models.CharField(max_length=8,null=True)

#修正仪数据表
class GS_MeterInfo_XZY(models.Model):
    MeterTypeId = models.OneToOneField('GS_MeterTypeInfo', unique=True, null=True)
    MeterId = models.CharField(max_length=12,unique=True)

    # 常规数据（供初检用）
    Com_no_xzy = models.CharField(max_length=16, null=True)
    Sw_rlse_xzy = models.CharField(max_length=4, null=True)

    MeterNum = models.IntegerField(null=True)

    Temperature_xzy = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    Disturb_Total_Vol = models.DecimalField(max_digits=8,decimal_places=2,null=True)
    Pressure = models.CharField(max_length=8, null=True)

    Correction_E = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    Stan_Total_Vol = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    Stan_Ins_Ele_xzy = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    Work_Total_Vol = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    Work_Ins_Ele_xzy = models.DecimalField(max_digits=6,decimal_places=2,null=True)

    DropMeter1_xzy = models.DateTimeField(null=True)
    DropMeter2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ReverseInstall1_xzy  = models.DateTimeField(null=True)
    ReverseInstall2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    MeasureBreakdown1_xzy  = models.DateTimeField(null=True)
    MeasureBreakdown2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    TSensorBreakdown1_xzy  = models.DateTimeField(null=True)
    TSensorBreakdown2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    PSensorBreakdown1_xzy  = models.DateTimeField(null=True)
    PSensorBreakdown2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    TrafficAbnormality1_xzy = models.DateTimeField(null=True)
    TrafficAbnormality2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ComVol1_xzy  = models.DateTimeField(null=True)
    ComVol2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    BaseVol1_xzy = models.DateTimeField(null=True)  # 计量电压低
    BaseVol2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CollectFault1_xzy = models.DateTimeField(null=True)  # 采集故障
    CollectFault2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    GasLeakClose1_xzy = models.DateTimeField(null=True)
    GasLeakClose2_xzy  = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    GasStolenClose1_xzy  = models.DateTimeField(null=True)
    GasStolenClose2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ResetClose1_xzy  = models.DateTimeField(null=True)
    ResetClose2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    LowVolClose1_xzy = models.DateTimeField(null=True)  # 计量低电压关阀
    LowVolClose2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CollectClose1_xzy = models.DateTimeField(null=True)  # 超声波计量故障关阀
    CollectClose2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CommandClose1_xzy = models.DateTimeField(null=True)  # 关阀指令关阀
    CommandClose2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ManulOpen1_xzy = models.DateTimeField(null=True)  # 人工开阀
    ManulOpen2_xzy = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    # 程序远程升级数据
    FTPUserName_xzy = models.CharField(max_length=25, default='01')
    FTPPassword_xzy = models.CharField(max_length=25, default='01')
    FTPAddress_xzy = models.CharField(max_length=50, default='139.199.191.23')
    FTPCatalog_xzy = models.CharField(max_length=50, default='D:\FTPPoint\File')
    FileName_xzy = models.CharField(max_length=8, null=True)

#超声波数据表
class GS_MeterInfo_CSB(models.Model):
    MeterTypeId = models.OneToOneField('GS_MeterTypeInfo', unique=True, null=True)
    MeterId = models.CharField(max_length=12, unique=True)

    # 常规数据（供初检用）
    Com_no_csb = models.CharField(max_length=16, null=True)
    Sw_rlse_csb = models.CharField(max_length=4, null=True)

    Vol1 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    Stan_Ins_Ele_csb = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    Vol2 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    Work_Ins_Ele_csb = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    MeterStateWord = models.CharField(max_length=2, null=True)
    Temperature_csb = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    MeterInStateWord = models.CharField(max_length=2, null=True)
    PValue = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    Stan_Total_Ele = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    Peak_Ele = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    Work_Total_Ele = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    DropMeter1_csb = models.DateTimeField(null=True)
    DropMeter2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ReverseInstall1_csb = models.DateTimeField(null=True)
    ReverseInstall2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    MeasureBreakdown1_csb = models.DateTimeField(null=True)
    MeasureBreakdown2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    TSensorBreakdown1_csb = models.DateTimeField(null=True)
    TSensorBreakdown2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    PSensorBreakdown1_csb = models.DateTimeField(null=True)
    PSensorBreakdown2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    TrafficAbnormality1_csb = models.DateTimeField(null=True)
    TrafficAbnormality2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ComVol1_csb = models.DateTimeField(null=True)
    ComVol2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    BaseVol1_csb = models.DateTimeField(null=True)  # 计量电压低
    BaseVol2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CollectFault1_csb = models.DateTimeField(null=True)  # 采集故障
    CollectFault2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    GasLeakClose1_csb = models.DateTimeField(null=True)
    GasLeakClose2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    GasStolenClose1_csb = models.DateTimeField(null=True)
    GasStolenClose2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ResetClose1_csb = models.DateTimeField(null=True)
    ResetClose2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    LowVolClose1_csb = models.DateTimeField(null=True)  # 计量低电压关阀
    LowVolClose2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CollectClose1_csb = models.DateTimeField(null=True)  # 超声波计量故障关阀
    CollectClose2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    CommandClose1_csb = models.DateTimeField(null=True)  # 关阀指令关阀
    CommandClose2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    ManulOpen1_csb = models.DateTimeField(null=True)  # 人工开阀
    ManulOpen2_csb = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    AF_ULimit1 = models.CharField(max_length=20, null=True)
    AF_DLimit1 = models.CharField(max_length=20, null=True)
    AF_LLimit1 = models.CharField(max_length=20, null=True)
    AF_ULimit2 = models.CharField(max_length=20, null=True)
    AF_DLimit2 = models.CharField(max_length=20, null=True)
    AF_LLimit2 = models.CharField(max_length=20, null=True)
    AF_ULimit3 = models.CharField(max_length=20, null=True)
    AF_DLimit3 = models.CharField(max_length=20, null=True)
    AF_LLimit3 = models.CharField(max_length=20, null=True)

    # 程序远程升级数据
    FTPUserName_csb = models.CharField(max_length=25, default='01')
    FTPPassword_csb = models.CharField(max_length=25, default='01')
    FTPAddress_csb = models.CharField(max_length=50, default='139.199.191.23')
    FTPCatalog_csb = models.CharField(max_length=50, default='D:\FTPPoint\File')
    FileName_csb = models.CharField(max_length=8, null=True)

#测试进度追踪（当前的测试的智能表）
class Meter_Test(models.Model):
    MeterId = models.CharField(max_length=12, primary_key=True, unique=True)  #表号是主键
    MeterType = models.CharField(max_length=10)
    MeterComState = models.CharField(max_length=25)
    MeterIcState = models.CharField(max_length=25)
    MeterChuState = models.CharField(max_length=25)
    MeterZhongState = models.CharField(max_length=25)
    MeterState = models.CharField(max_length=25, default='初始')
    MeterTest = models.CharField(max_length=25, default='空闲')
    MeterRand_num = models.CharField(max_length=25, null=True)
    Meteriport = models.CharField(max_length=50, null=True)
    MeterTime = models.DateTimeField(auto_now_add=True, null=True)  # 当前时间
    MeterCancel = models.CharField(max_length=10,default="否")   #是否取消测试
    MeterEvery = models.CharField(max_length=32, default="00000000000000000000000000000000") #单项结果
    MeterPrivilege = models.CharField(max_length=1,default="0") #优先

    ManufactureName = models.ForeignKey('Manufacture',null=True)  # 燃气表生产厂商  Manufacture_id
    Subtime = models.DateTimeField(null=True)  # 提交时间
    CheckTime = models.DateTimeField(null=True)  # 审核时间

class Meter_Result(models.Model):
    MeterId = models.CharField(max_length=12, primary_key=True, unique=True)  #表号是主键
    MeterType = models.CharField(max_length=10)
    MeterComState = models.CharField(max_length=25)
    MeterIcState = models.CharField(max_length=25)
    MeterChuState = models.CharField(max_length=25)
    MeterZhongState = models.CharField(max_length=25)
    MeterState = models.CharField(max_length=25, default='初始')
    MeterTest = models.CharField(max_length=25, default='空闲')
    MeterRand_num = models.CharField(max_length=25, null=True)
    Meteriport = models.CharField(max_length=50, null=True)
    MeterTime = models.DateTimeField(auto_now_add=True, null=True)  # 当前时间
    MeterCancel = models.CharField(max_length=10,default="否")   #是否取消测试
    MeterEvery = models.CharField(max_length=32, default="00000000000000000000000000000000") #单项结果
    MeterPrivilege = models.CharField(max_length=1,default="0") #优先

    ManufactureName = models.ForeignKey('Manufacture', null=True)  # 燃气表生产厂商  Manufacture_id
    Subtime = models.DateTimeField(null=True)  # 提交时间
    CheckTime = models.DateTimeField(null=True)  # 审核时间

    class Meta:
        ordering = ['-MeterTime']   #从大到小排序

class Meter_Result_Record(models.Model):
    MeterId = models.CharField(max_length=12, primary_key=True, unique=True)  #表号是主键
    MeterType = models.CharField(max_length=10)
    MeterComState = models.CharField(max_length=25)
    MeterIcState = models.CharField(max_length=25)
    MeterChuState = models.CharField(max_length=25)
    MeterZhongState = models.CharField(max_length=25)
    MeterState = models.CharField(max_length=25, default='初始')
    MeterTest = models.CharField(max_length=25, default='空闲')
    MeterRand_num = models.CharField(max_length=25, null=True)
    Meteriport = models.CharField(max_length=50, null=True)
    MeterTime = models.DateTimeField(auto_now_add=True, null=True)  # 当前时间
    MeterCancel = models.CharField(max_length=10,default="否")   #是否取消测试
    MeterEvery = models.CharField(max_length=32, default="00000000000000000000000000000000") #单项结果
    MeterPrivilege = models.CharField(max_length=1,default="0") #优先

    ManufactureName = models.ForeignKey('Manufacture', null=True)  # 燃气表生产厂商  Manufacture_id
    Subtime = models.DateTimeField(null=True)  # 提交时间
    CheckTime = models.DateTimeField(null=True)  # 审核时间

    class Meta:
        ordering = ['-MeterTime']   #从大到小排序

class PlanInfo(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)     #不自增，主键
    IP = models.CharField(max_length=30)
    PlatComs = models.CharField(max_length=20)
    PlatIcs = models.CharField(max_length=20)
    PlatChus_msb = models.CharField(max_length=20)
    PlatChus_xzy = models.CharField(max_length=20)
    PlatChus_csb = models.CharField(max_length=20)
    PlatZhos = models.CharField(max_length=20)
    PlatComp = models.CharField(max_length=20, null=True)
    PlatIcp = models.CharField(max_length=20, null=True)
    PlatChup_msb = models.CharField(max_length=20, null=True)
    PlatChup_xzy = models.CharField(max_length=20, null=True)
    PlatChup_csb = models.CharField(max_length=20, null=True)
    PlatZhop = models.CharField(max_length=20, null=True)

class MeterPlat(models.Model):
    MeterId = models.CharField(max_length=12, primary_key=True, unique=True)  # 表号是主键
    Meterip_Com = models.CharField(max_length=10, null=True)
    Meterip_IC = models.CharField(max_length=10, null=True)
    Meterip_Chu = models.CharField(max_length=10, null=True)
    Meterip_Zhong = models.CharField(max_length=10, null=True)