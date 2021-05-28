from queue import Queue
from threading import Thread

from knotprot_download import get_proteins, download_link, setup_download_dir, time_it

def run_sequentially(dir):
    for p in get_proteins():
        download_link(dir, p)


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            dir, prot = self.queue.get()
            try:
                download_link(dir, prot)
            finally:
                self.queue.task_done()


def run_workers(dir):
    proteins = get_proteins()
    queue = Queue()
    for n in range(8):
        worker = DownloadWorker(queue)
        # Stop when the thread that stared it (main) stops
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((dir, p))
    queue.join()

mydir = setup_download_dir()
#time_it(run_sequentially, mydir)

time_it(run_workers, mydir)