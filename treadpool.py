import threading
import queue

class ThreadPool:
    def __init__(self, num_threads=5):
        self.num_threads = num_threads
        self.task_queue = queue.Queue()
        self.workers = []

        self._create_workers()

    def _create_workers(self):
        for _ in range(self.num_threads):
            worker = threading.Thread(target=self._worker_loop)
            worker.daemon = True
            self.workers.append(worker)
            worker.start()

    def _worker_loop(self):
        while True:
            task, args, kwargs, event = self.task_queue.get()
            if task is None:
                break
            try:
                result = task(*args, **kwargs)
                event.set()  # Signal that the task is completed
            except Exception as e:
                result = e
            self.task_queue.task_done()

    def submit_task(self, task, *args, **kwargs):
        event = threading.Event()
        self.task_queue.put((task, args, kwargs, event))
        return event

    def shutdown(self):
        for _ in range(self.num_threads):
            self.task_queue.put((None, None, None))
        self.task_queue.join()
        for worker in self.workers:
            worker.join()


# Example usage:
def example_task(task_id):
    print(f"Task {task_id} is being executed in thread {threading.current_thread().name}")
    return task_id * 2

if __name__ == "__main__":
    thread_pool = ThreadPool(num_threads=3)

    tasks = [1, 2, 3, 4, 5]
    results = []

    for task_id in tasks:
        event = thread_pool.submit_task(example_task, task_id)
        results.append((task_id, event))

    thread_pool.shutdown()

    for task_id, event in results:
        event.wait()  # Wait for the task to complete
        print(f"Task {task_id} result: {task_id * 2}")

