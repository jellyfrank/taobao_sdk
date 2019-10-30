
import unittest
from taobao.api import TaoBao
from taobao.exception import TradeError


class TestTrade(unittest.TestCase):

    def test_trade_sold_get(self):
        tb = TaoBao("1023173103", "sandbox5e4645d3045c1dd3365afe74c", "12345", sanbox=True)
        tb._get_session_key()
        # self.assertRaises(TradeError,tb.tradeapi.trade_sold_get,"tid,type,status,payment,orders,rx_audit_status")
        tb.tradeapi.trade_sold_get("tid,type,status,payment,orders,rx_audit_status")
        
        r, data = tb.tradeapi.trade_sold_get(
            "tid,type,status,payment,orders,rx_audit_status", "2019-02-01")
        print(r, data)


if __name__ == "__main__":
    unittest.main()
