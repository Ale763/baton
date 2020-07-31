import sys
import time
import threading
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class AbstractFileWatcher(threading.Thread):
    def __init__(self, p_root_dir):
        self.root_dir = p_root_dir

    def run(self) -> None:
        pass