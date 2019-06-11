
from taobao.comm import Common


class UserApi(Common):
    """用户接口"""

    def appstore_subscibe_get(self, nick):
        """
        查询appstore应用订购关系
        nick: 用户昵称
        """

        data = {
            "nick": nick
        }

        return self.post("taobao.appstore.subscribe.get", data)
