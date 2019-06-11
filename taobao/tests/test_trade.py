
import unittest
from taobao.api import TaoBao
from taobao.exception import TradeError


class TestTrade(unittest.TestCase):

    def test_trade_sold_get(self):
        tb = TaoBao("12345678", "helloworld", "12345", sanbox=True)
        self.assertRaises(TradeError,tb.tradeapi.trade_sold_get,"tid,type,status,payment,orders,rx_audit_status")
        tb.tradeapi.trade_sold_get("tid,type,status,payment,orders,rx_audit_status"))
        
        r, data = tb.tradeapi.trade_sold_get(
            "tid,type,status,payment,orders,rx_audit_status", "2019-02-01")
        print(r, data)


if __name__ == "__main__":
    unittest.main()
