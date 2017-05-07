from redis import Redis

class DataCache:

    def __init__(self):
        self.redis = Redis(host='redis', port=6379)

    def save_list(self, key, list):
        for i in list:
            self.redis.lpush(key, i)

    def get_saved_list(self, key):
        return list(map(lambda n: n.decode(), self.redis.lrange(key, 0, -1)))
