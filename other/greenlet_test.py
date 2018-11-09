import gevent


def func1():
    print("func1 beginning...")
    gevent.sleep(2)
    print("func1 again...")


def func2():
    print("func2 beginning...")
    gevent.sleep(1)
    print("func2 again")


def func3():
    print("func3 beginning")
    gevent.sleep(0)
    print("func3 again")


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3)
])