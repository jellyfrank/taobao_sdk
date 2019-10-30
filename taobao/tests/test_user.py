
import unittest
from taobao.api import TaoBao
from taobao.exception import SignError


class TestUser(unittest.TestCase):

    def test_appstore_subscibe_get(self):
        taobao = TaoBao("12345678", "helloworld", "abcd", sanbox=True)
        r, data = taobao.userapi.appstore_subscibe_get("test123")
        self.assertEqual(r, False)


if __name__ == "__main__":
    unittest.main()
