import redis
import settings

redis_client = redis.StrictRedis(host=settings.REDIS_CONFIG['HOST'],
                                 port=settings.REDIS_CONFIG['PORT'],
                                 db=settings.REDIS_CONFIG['SESSION_DB'])

def get_session_value(mobile):
    redis_key = "VerifyCode:{0}".format(mobile)
    redis_value = redis_client.get(redis_key)
    return redis_value

def get_sms_captcha(mobile):
    return get_session_value(mobile)
