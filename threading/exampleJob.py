import threading
import time
from queue import Queue 

print_lock = threading.Lock()

q = Queue()
# the job whcich we want to perform
def job(worker):
	time.sleep(.5)
	with print_lock:
		print(threading.current_thread().name,worker)


# creating threader
def threader():
	while True:
		worker = q.get()
		job(worker)
		q.task_done()

# creating no of thread which we wnt to perform
for x in range(500): # example 10 thread
	t = threading.Thread(target = threader)
	t.daemon = True
	t.start()

start_time = time.time()

#no of tasks which we want to perform
for worker in range(500):
	q.put(worker)

q.join()
# for x in range(50):
# 	print(q[x])

print('whole task complete in :',time.time() - start_time)