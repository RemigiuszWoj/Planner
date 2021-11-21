a = [{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 3}, {"x": 4, "y": 4}]
a = iter(a)

ob = next(a)
previous = ob
while a:
    try:
        ob = previous
        next_ob = next(a)
        print(ob, next_ob)
        previous = next_ob
    except StopIteration:
        break


import datetime

time = datetime.datetime(2020, 2, 19, 8, 0, 0)
print(time + datetime.timedelta(minutes=5))
