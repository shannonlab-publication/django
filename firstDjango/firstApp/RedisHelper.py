# -*- coding: utf-8 -*-
#from django.conf import settings
try:
    import cPickle as pickle
except:
    import pickle

import redis

class RedisHelper(object):
    def __init__(self, host='localhost', port=6379, db=0): 
        self.r = redis.StrictRedis(host = host, port = port, db = db)
        self.EXPIRE_TIME = 3 * 60 * 60
        #self.KEY_BASE = settings.APP_NAME
        self.KEY_BASE = "myApp"
        
    def set_value(self, key, value, nx = False):   #値をセット(上書きしない)
        my_key = self.KEY_BASE + key
        self.r.set(my_key, pickle.dumps(value),nx)
        self.r.expire(my_key, self.EXPIRE_TIME)

    def get_value(self,key):
        my_key = self.KEY_BASE + key
        pickled_value = self.r.get(my_key)
        if pickled_value is None:
            return None
        # pickle化された値を戻す
        return pickle.loads(pickled_value)   

    def delete_value(self,key):
        my_key = self.KEY_BASE + key
        return self.r.delete(my_key) 

    def exists(self,key):
        my_key = self.KEY_BASE + key
        return  self.r.exists(my_key)      

if __name__ == "__main__":
    r = RedisHelper()
    r.set_value("test",123456)
    print(r.get_value("test"))
