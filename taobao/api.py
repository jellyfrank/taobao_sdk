
from taobao.user import UserApi
from taobao.trade import  TradeApi
from taobao.comm import Common

class TaoBao(object):
    """淘宝SDK"""

    def __init__(self, key, secret, session, ssl=False, sanbox=False):
        """
        参数列表：
        key:
        secret:
        session: 
        ssl: 是否使用HTTPS
        sandbox: 是否沙箱环境
        """
        self._key = key
        self._secret = secret
        self._session = session
        if ssl:
            if sanbox:
                self._url = "https://gw.api.tbsandbox.com/router/rest"
            else:
                self._url = "https://eco.taobao.com/router/rest"
        else:
            if sanbox:
                self._url = "http://gw.api.tbsandbox.com/router/rest"
            else:
                self._url = "http://gw.api.taobao.com/router/rest"

    userapi = UserApi()
    tradeapi = TradeApi()
