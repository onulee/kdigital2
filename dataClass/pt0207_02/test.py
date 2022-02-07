import calendar
import time


ts = calendar.timegm(time.gmtime())
type(ts)
print("{}{}".format(ts,"_a.jpg"))
print(type(ts))