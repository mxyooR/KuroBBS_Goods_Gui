from .utils import geeUtils
import time

def getCurrentStampMs():
    return round(time.time() * 1000)

def get_geeTestData():
    captcha_id = "3f7e2d848ce0cb7e7d019d621e556ce2"
    callBackSign = f"geetest_{getCurrentStampMs()}"
    seccode = geeUtils.geeSecCode(callBackSign=callBackSign, captcha_id=captcha_id)
    #为了保证效率所有的log都注释掉了
    return seccode

