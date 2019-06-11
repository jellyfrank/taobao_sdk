

class ErrorResponse(object):

    request_id = None
    code = None
    msg = None
    sub_code = None
    sub_msg = None


class PositiveResponse(object):
    pass


class BaseResponse(object):
    """响应基类"""

    def __init__(self, data=None):
        """
        初始化
        data：请求返回的实体
        """
        if data.get("error_response", None):
            self.positive = False
            self.error_response = ErrorResponse()
            self.construct_obj(
                self.error_response, data.get("error_response"))
        else:
            self.positive = True

    @staticmethod
    def construct_obj(instance, data):
        """构造返回实体"""
        if isinstance(data, dict):
            for key, val in data.items():
                if isinstance(val, dict):
                    setattr(instance, key, PositiveResponse())
                    BaseResponse.construct_obj(getattr(instance, key), val)
                else:
                    setattr(instance, key, val)
