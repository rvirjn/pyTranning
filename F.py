import time
class Timer:

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()

    def get_time_taken(self):
        return  self.stop_time - self.start_time


class ContextTimer(Timer):
    def __enter__(self):
        print("Inside enter...")
        self.start()
        name= 'ravi'
        return name

    def __exit__(self, a,b,c):
        print ('inside exist')
        self.stop()
        print self.get_time_taken()
        return 'ranjan'

class person:
    pass
if __name__ == "__main__":
    # t = Timer()
    # t.start()
    # time.sleep(5)
    # t.stop()
    # print ('Time taken', t.get_time_taken())

    with ContextTimer() as a:
        for i in range(10000):
            for j in range(1000):
                s = 1 * j * 1.0
        print a
