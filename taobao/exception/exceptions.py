

class SignError(Exception):
    """签名异常"""
    pass

class SignTypeError(Exception):
    pass

class ValidateError(Exception):
    """验证错误"""
    pass

class PostError(Exception):
    """请求失败"""
    pass

class TradeError(Exception):
    """交易类错误"""
    pass

