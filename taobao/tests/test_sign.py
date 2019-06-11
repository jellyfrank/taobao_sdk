
import unittest
from taobao.api import TaoBao
from taobao.exception import SignError


class TestComm(unittest.TestCase):

    def test_sign(self):
        c = TaoBao("12345678", "helloworld", "abcd", sanbox=True)
        data = "123"
        self.assertRaises(SignError, c.sign, data)
        data = {
            "method": "taobao.item.seller.get",
            "app_key": "12345678",
            "session": "test",
            "timestamp": "2016-01-01 12:00:00",
            "format": "json",
            "v": "2.0",
            "sign_method": "md5",
            "fields":"num_iid,title,nick,price,num",
            "num_iid":"11223344"
        }
        r = c.sign(data,type="md5")
        self.assertEqual(r,"66987CB115214E59E6EC978214934FB8")


if __name__ == "__main__":
    unittest.main()
