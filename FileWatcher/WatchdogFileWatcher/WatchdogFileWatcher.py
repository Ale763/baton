import time
import logging
from watchdog.observers import Observer
from FileWatcher.AbstractFileWatcher.AbstractFileWatcher import AbstractFileWatcher
from FileWatcher.WatchdogFileWatcher.WatchdogEventHandler import WatchdogEventHandler



class WatchdogFileWatcher(AbstractFileWatcher):
    def __init__(self, p_root_dir):
        super().__init__(p_root_dir)

    def monitor(self) -> None:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        path = self.root_dir
        # event_handler = LoggingEventHandler()
        event_handler = WatchdogEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()