from FileWatcher.AbstractFileWatcher.AbstractFileWatcher import AbstractFileWatcher
from FileWatcher.Watchdog.WatchdogEventHandlerThread import WatchdogEventHandlerThread
import queue
import time
from typing import Dict
import threading


class WatchdogFileWatcher(AbstractFileWatcher):
    def __init__(self, p_root_dir: str):
        super().__init__(p_root_dir)
        self.queue = queue.Queue()
        self.event_handler: WatchdogEventHandlerThread = WatchdogEventHandlerThread(self.root_dir, self.queue)
        self.event_handler.start()

        self.event_batch_processor = None
        printer_worker = threading.Thread(name='printer', target=self.printer)
        printer_worker.start()

    def printer(self):
        while True:
            if not self.queue.empty():
                print("Printer queue:")
                batch: Dict[str, queue.Queue] = self.queue.get()
                for key in batch:
                    print("{0}: {1}".format(key, batch[key]))
                    while not batch[key].empty():
                        print("\t{0}".format(batch[key].get()))
            time.sleep(10)
