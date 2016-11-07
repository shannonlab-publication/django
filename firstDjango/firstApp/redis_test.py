import RedisHelper
r = RedisHelper.RedisHelper()
r.set_value("test", 123)
r.set_value("test_list", [1,2,3])

print(r.get_value("test"))
print(r.get_value("test_list"))
