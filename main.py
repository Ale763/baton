# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FileWatcher.WatchdogFileWatcher.WatchdogFileWatcher import WatchdogFileWatcher
from FileWatcher.fileWatcherIndex import *
import os


def rec_walk(dir, p_depth=0):
    contents = os.listdir(dir)  # read the contents of dir
    for item in contents:  # loop over those contents
        print("\t"*p_depth+item)  # do something else with non-directory items
        if os.path.isdir(os.path.join(dir, item)):
            rec_walk(dir + "\\" + item, p_depth + 1)  # recurse on subdirectories

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # file_watcher_strategy = WatchdogFileWatcher("/Users/ale/Documents/BatonTest")
    file_watcher_strategy = WatchdogFileWatcher("C:\\Users\\aless\\Documents\\BatonTest")
    # file_watcher_strategy.monitor()

    # rec_walk("C:\\Users\\aless\\Documents\\BatonTest")

