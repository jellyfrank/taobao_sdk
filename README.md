# Taobao SDK

第三方淘宝SDK

## Usage

使用方法：

```python
from taobao.api import TaoBao

taobao = TaoBao(key, secret, session)
taobao.tradeapi.trade_sold_get(...)
```

## Api

### 交易类

* trade_sold_get：查询卖家已卖出的交易数据
* trade_fullinfo_get： 获取单笔交易的详细信息
* trade_amount_get： 交易账务查询
* trade_memo_update: 修改交易备注

### 菜鸟配货

* 商品信息查询
