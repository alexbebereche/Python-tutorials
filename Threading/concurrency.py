import threading
import time


def funct():
    print('start')
    time.sleep(4)
    print('end')


# t1 = threading.Thread(target=funct)
# t1.start()

threads = []

for _ in range(5):
    t1 = threading.Thread(target=funct)
    threads.append(t1)
    t1.start()
    # t1.join()

for thread in threads:
    thread.join()  # threads are gonna start and finish together

print(threading.active_count())
