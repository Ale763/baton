import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class BaseFileWatcher:
    def __init__(self, p_root_dir):
        self.root_dir = p_root_dir

    def monitor(self) -> None:
        pass