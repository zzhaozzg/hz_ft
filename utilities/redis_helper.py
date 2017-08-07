import redis
import settings

redis_client = redis.StrictRedis(host=settings.REDIS_CONFIG['HOST'], port=settings.REDIS_CONFIG['PORT'])


def clean_redis():
    redis_client.flushall()