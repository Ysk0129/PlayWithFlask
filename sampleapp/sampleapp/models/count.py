from redis import Redis

class Counter:

    def __init__(self):
        self.redis = Redis(host='redis', port=6379)

    def incrCount(self):
        self.redis.incr('counts')

    def getCount(self):
        return int(self.redis.get('counts'))
