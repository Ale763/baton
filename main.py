# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FileWatcher.WatchdogFileWatcher.WatchdogFileWatcher import WatchdogFileWatcher
from FileWatcher.fileWatcherIndex import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_watcher_strategy = WatchdogFileWatcher("/Users/ale/Documents/BatonTest")
    file_watcher_strategy.monitor()


