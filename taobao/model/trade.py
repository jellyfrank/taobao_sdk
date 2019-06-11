
from .base import BaseResponse, PositiveResponse


class SoldGetResponse(BaseResponse):
    """卖出的交易数据"""

    def __init__(self, data):
        super(SoldGetResponse, self).__init__(data)
        if data.get("trades_sold_get_response", None):
            self.trades_sold_get_response = PositiveResponse()
            self.construct_obj(self.trades_sold_get_response,
                               data.get("trades_sold_get_response"))
