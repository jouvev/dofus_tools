from threading import Thread
import threading
import time
from concurrent.futures import ThreadPoolExecutor

class Test(Thread):
    def __init__(self):
        Thread.__init__(self,name="test")
        self.executor = ThreadPoolExecutor(4,thread_name_prefix="DofusManager(ThreadPool)")
    
    def run(self):
        time.sleep(5)
        
t = Test()
t.start()
for thread in threading.enumerate(): 
    print(thread.name, "running")
t.join()
