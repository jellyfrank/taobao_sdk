

from taobao.exception import SignError, SignTypeError, ValidateError, PostError
from hashlib import md5
import hmac
import traceback
from datetime import datetime
import json
import requests
from taobao.model.base import BaseResponse


class Common(object):
    """公共请求参数"""

    def __get__(self, instance, owner):
        self._secret = instance._secret
        self._key = instance._key
        self._session = instance._session
        self._url = instance._url
        return self

    def sign(self, data, type="hmac"):
        """
        签名算法
        data: 待签名的数据字典
        type: 签名算法类型，可选值：hmac和md5
        """
        if not isinstance(data, dict):
            raise SignError("签名数据格式错误")

        if type not in ("hmac", "md5"):
            raise SignTypeError("签名算法错误")

        try:
            # 按字母序排序
            keys = sorted([key for key, val in data.items() if not (
                key == "sign" or isinstance(val, bytes))])
            # 拼接字符串
            strs = "".join(f"{key}{data[key]}" for key in keys)
            if type == "md5":
                return md5(f"{self._secret}{strs}{self._secret}".encode("utf-8")).hexdigest().upper()
            else:
                return hmac.new(strs).hexdigest().upper()
        except Exception as err:
            raise SignError(f"数据签名异常：{traceback.format_exc()}")

    def _get_comm_args(self, method, target_app_key=None, sign_method="md5", format="json", version="2.0", partner_id=None, simplify=False):
        """
        获取公共请求参数
        method: 方法名
        target_app_key： 被调用的目标AppKey，仅当被调用的API为第三方ISV提供时有效
        sign_method： 签名算法，默认md5
        format: 返回格式，默认json
        version: API协议版本，默认2
        partner_id：合作伙伴标识
        simplify： 是否采用精简JSON返回格式，仅当format=json时有效，默认值为：False
        """

        data = {
            "method": method,
            "app_key": self._key,
            "session": self._session,
            "timestamp": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
            "format": format,
            "v": version,
            "sign_method": sign_method
        }

        if target_app_key:
            data['target_app_key'] = target_app_key
        if partner_id:
            data['partner_id'] = partner_id
        if simplify:
            data['simplify'] = simplify

        return data

    def _parse_comm_response(self, method, data):
        """
        公共响应
        data: 淘宝返回的结果
        """

        if "taobao." in method:
            method = method.split("taobao.")[1].replace(".", "_")

        # return BaseResponse(method, data=data)

        if data.get("error_response", False):
            return False, data["error_response"]

        if data.get(f"{method}_response", False):
            return True, data[f"{method}_response"]

    def post(self, method, data):
        """
        提交请求
        method: 请求方法
        data: 接口参数
        return: 返回结果 
        """
        if not isinstance(data, dict):
            raise ValidateError("数据格式错误")

        try:
            # 组织请求数据
            comm_data = self._get_comm_args(method)
            data.update(comm_data)
            data['sign'] = self.sign(data, type=data['sign_method'])

            headers = {
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
            }

            response = requests.post(
                self._url, data=data, headers=headers).json()
            # print(response)
            # return response
            return self._parse_comm_response(method, response)
        except Exception as err:
            raise PostError(f"接口：{method} 调用失败:{traceback.format_exc()}")
