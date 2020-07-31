# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FileWatcher.Watchdog.WatchdogFileWatcher import WatchdogFileWatcher
from FileWatcher.fileWatcherIndex import *
import os
import queue
import time
from typing import Dict
import threading

from Indexer.TreeStrategies.BaseTree import BaseTree

# ROOT_DIR = "/Users/ale/Documents/BatonTest"
ROOT_DIR = "C:\\Users\\aless\\Documents\\BatonTest"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # event_queue = queue.Queue()
    # file_watcher_strategy = WatchdogFileWatcher(ROOT_DIR)
    tree = BaseTree()
    tree.parse_from_dir(ROOT_DIR)
    print("done")

