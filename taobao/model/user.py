
from .base import BaseResponse


class Subscribe(BaseResponse):
    """appstore应用订购"""

    def __init__(self, data):
        super(Subscribe, self).__init__(data)
        if data.get("appstore_subscibe_get_response", None):
            self.appstore_subscibe_get_response = object()
            self.construct_obj(
                self.appstore_subscibe_get_response, data.get("appstore_subscibe_get_response"))
