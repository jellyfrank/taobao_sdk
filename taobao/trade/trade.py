# 交易类接口

import inspect
from taobao.comm import Common
from taobao.exception import TradeError

STATUS = {
    "WAIT_BUYER_PAY": "等待买家付款",
    "WAIT_SELLER_SEND_GOODS": "等待卖家发货",
    "SELLER_CONSIGNED_PART": "卖家部分发货",
    "WAIT_BUYER_CONFIRM_GOODS": "等待买家确认收货",
    "TRADE_BUYER_SIGNED": "买家已签收（货到付款专用）",
    "TRADE_FINISHED": "交易成功",
    "TRADE_CLOSED": "交易关闭",
    "TRADE_CLOSED_BY_TAOBAO": "交易被淘宝关闭",
    "TRADE_NO_CREATE_PAY": "没有创建外部交易（支付宝交易）",
    "WAIT_PRE_AUTH_CONFIRM": "余额宝0元购合约中",
    "PAY_PENDING": "外卡支付付款确认中",
    "ALL_WAIT_PAY": "所有买家未付款的交易（包含：WAIT_BUYER_PAY、TRADE_NO_CREATE_PAY）",
    "ALL_CLOSED": "所有关闭的交易（包含：TRADE_CLOSED、TRADE_CLOSED_BY_TAOBAO）",
    "PAID_FORBID_CONSIGN": "该状态代表订单已付款但是处于禁止发货状态"
}

DEFAULT_TYPE = "guarantee_trade,auto_delivery,ec,cod,step"
OPTION_TYPE = [
    "fixed",  # 一口价
    "auction",  # 拍卖
    "guarantee_trade",  # 一口价、拍卖
    "step",  # 分阶段
    "independent_simple_trade",  # 旺店入门版
    "independent_shop_trade",  # 旺店标准版
    "auto_delivery",  # 自动发货
    "ec",  # 直冲
    "cod",  # 货到付款
    "game_equipment",  # 游戏装备
    "shopex_trade",  # SHopex
    "netcn_trade",  # 万网交易
    "external_trade",  # 同一外部交易
    "instant_trade ",  # 即时到账
    "b2c_cod",  # 大商家货到付款
    "hotel_trade",  # 酒店类型
    "super_market_trade",  # 商超交易
    "super_market_cod_trade",  # 商超货到付款
    "taohua",  # 淘花网
    "waimai",  # 外卖
    "o2o_offlinetrade",  # O2O交易
    "nopaid",  # 即时到帐/趣味猜交易类型
    "eticket",  # 电子凭证
    "tmall_i18n",  # 天猫国际
    "nopaid",  # 无付款交易
    "insurance_plus",  # 保险
    "finance",  # 基金
    "pre_auth_type",  # 预授权交易
    "lazada",  # lazada
]

TRADE_TYPE = {
    "default": DEFAULT_TYPE,
    "all": ",".join(OPTION_TYPE)
}

REFUND_STATUS = {
    "WAIT_SELLER_AGREE": "买家已经申请退款",
    "WAIT_BUYER_RETURN_GOODS": "卖家已经同意退款，等待买家退货",
    "WAIT_SELLER_CONFIRM_GOODS": "买家已经退货，等待卖家确认收货",
    "SELLER_REFUSE_BUYER": "卖家拒绝退款",
    "CLOSED": "退款关闭",
    "SUCCESS": "退款成功"
}


class TradeApi(Common):

    def trade_sold_get(self, fields, start_created=None, end_created=None, status=None, buyer_nick=None,
                       type=DEFAULT_TYPE, ext_type=None, rate_status=None,
                       tag=None, page_no=None, page_size=None, use_has_next=None):
        """
        查询卖家已卖出的交易数据
        feilds: 需要返回的字段列表，逗号分隔
        start_created： 交易开始时间（三个月内）
        end_created： 交易结束时间
        status：交易状态
        buyer_nick: 买家昵称
        type： 交易类型（默认查询5种类型）
        ext_type：扩展类型
        rate_status: 评价状态
        tag： 交易自定义分组
        page_no： 页码
        page_size： 每页条数
        use_has_next： 是否启用has_next的分页方式
        """

        data = {
            "fields": fields
        }

        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for ar in args:
            if values[ar]:
                data[ar] = values[ar]

        return self.post("taobao.trades.sold.get", data)

    def trade_fullinfo_get(self, fields, tid):
        """
        获取单笔交易的详细信息
        1. 只有在交易成功的状态下才能取到交易佣金，其它状态下取到的都是零或空值 
        2. 只有单笔订单的情况下Trade数据结构中才包含商品相关的信息 
        3. 获取到的Order中的payment字段在单笔子订单时包含物流费用，多笔子订单时不包含物流费用 
        4. 获取红包优惠金额可以使用字段 coupon_fee 
        """

        data = {
            "fields": fields,
            "tid": tid
        }

        return self.post("taobao.trade.fullinfo.get", data)

    def trade_amount_get(self, fields, tid):
        """
        交易账务查询
        1. 只供卖家使用，买家不可使用 
        2. 可查询所有的状态的交易，但不同状态时交易的相关数据可能会有不同
        """
        data = {
            "fields": fields,
            "tid": tid
        }

        return self.post("taobao.trade.amount.get", data)

    def trade_memo_update(self, tid, memo="", flag=0, reset=False):
        """
        修改交易备注
        需要商家或以上权限才可调用此接口，可重复调用本接口更新交易备注，本接口同时具有添加备注的功能
        参数：
        tid： 交易编号
        memo： 交易备注（1000字节）
        flag： 卖家交易备注旗帜，可选值为：0(灰色), 1(红色), 2(黄色), 3(绿色), 4(蓝色), 5(粉红色)，默认值为0
        reset： 是否对memo的值置空若为true
        """
        data = {
            "tid": tid,
            "memo": memo,
            "flag": flag,
            "reset": reset
        }

        return self.post("taobao.trade.memo.update", data)
