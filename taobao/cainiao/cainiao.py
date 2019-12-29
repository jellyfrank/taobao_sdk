#!/usr/bin/python3
# @Time    : 2019-12-29
# @Author  : Kevin Kong (kfx2007@163.com)

# 菜鸟配货仓API

import inspect
from taobao.comm import Common


class CaiNiaoApi(Common):

    def wlb_wms_sku_get(self, item_code=None, item_id=None, owner_user_id=None):
        """
        商品信息查询
        """
        data = {
            "item_code": item_code,
            "item_id": item_id,
            "owner_user_id": owner_user_id
        }

        return self.post("taobao.wlb.wms.sku.get", data)

    def wlb_wms_inventory_query(self, item_id=None, store_code=None, inventory_type=None,
                                type=None, batch_code=None, produce_date=None, due_date=None,
                                channel_code=None, page_no=None,
                                page_size=None):
        """
        菜鸟商品库存查询 
        """
        data = {
            "item_id": item_id,
            "store_code": store_code,
            "inventory_type": inventory_type,
            "type": type,
            "batch_code": batch_code,
            "produce_date": produce_date,
            "due_date": due_date,
            "channel_code": channel_code,
            "page_no": page_no,
            "page_size": page_size
        }

        return self.post("taobao.wlb.wms.inventory.query", data)
