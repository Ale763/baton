import threading
import time
import logging
from watchdog.observers import Observer
from FileWatcher.Watchdog.WatchdogEventHandler import *


class WatchdogEventHandlerThread(threading.Thread):
    def __init__(self, p_root_dir: str, p_queue: queue.Queue):
        super().__init__()
        self.batch_queue: queue.Queue = p_queue
        self.root_dir = p_root_dir
        # self.event_handler: LoggingEventHandler = LoggingEventHandler()
        self.event_handler: WatchdogEventHandler = WatchdogEventHandler()

    def run(self) -> None:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        path = self.root_dir
        observer = Observer()
        observer.schedule(self.event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(10)
                batch = self.event_handler.checkout_batch()
                if batch != {}:
                    self.batch_queue.put(batch)

        except KeyboardInterrupt:
            observer.stop()
        observer.join()
