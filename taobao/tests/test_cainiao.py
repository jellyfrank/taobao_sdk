
import unittest
from taobao.api import TaoBao
import json


class TestCaiNiao(unittest.TestCase):

    def test_wlb_wms_sku_get(self):
        tb = TaoBao("23229023", "497eb6372b6f152059a65015775838c8", "6100b28fe461f6883cf4040163de9c53a0f618ecea5c5582999166418")
        # print(tb.tradeapi.trade_sold_get("orders"))
        res = tb.cainiao.wlb_wms_sku_get(item_id="10732069",owner_user_id=1)
        print(json.dumps(res))

    def test_wlb_wms_inventory_query(self):
        tb = TaoBao("23229023", "497eb6372b6f152059a65015775838c8", "6100b28fe461f6883cf4040163de9c53a0f618ecea5c5582999166418")
        res = tb.cainiao.wlb_wms_inventory_query()
        print(json.dumps(res))

if __name__ == "__main__":
    unittest.main()
