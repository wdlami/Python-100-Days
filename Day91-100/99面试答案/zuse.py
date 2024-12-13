import threading
import time

def short_task():
    time.sleep(0.1)

threads = [threading.Thread(target=short_task) for _ in range(100000)]
start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Total time: {time.time() - start:.2f}s")
