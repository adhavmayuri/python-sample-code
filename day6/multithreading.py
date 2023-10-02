import threading

def foo():
    for _ in range(5):
        print("Foo")

def bar():
    for _ in range(5):
        print("Bar")

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)

t1.start()
t2.start()

t1.join()
t2.join()
