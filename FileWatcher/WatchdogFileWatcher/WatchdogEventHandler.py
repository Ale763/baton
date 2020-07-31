from watchdog.events import FileModifiedEvent, FileCreatedEvent
from typing import Dict
from FileWatcher.AbstractFileWatcher.AbstractEventHandler import *
import threading
import queue


class WatchdogEventHandler(AbstractEventHandler):
    def __init__(self):
        super().__init__()
        self.batch: Dict[str, any] = {}
        self.batch_lock = threading.Lock()

    def checkout_batch(self) -> Dict[str, any]:
        self.batch_lock.acquire()
        current_batch: Dict[str, any] = self.batch
        self.batch: Dict[str, any] = {}
        self.batch_lock.release()
        return current_batch

    # def on_any_event(self, event: FileCreatedEvent) -> None:
    #     event_time: str = AbstractEventHandler.get_time()
    #     event_type: str = event.event_type
    #     modified_item_type: str = "folder" if event.is_directory else "file"
    #     payload = "{0} - {1}: {2} : {3}".format(event_time, event_type, modified_item_type, event.src_path)
    #     print(payload)
    #
    #     self.batch_lock.acquire()
    #     if event.src_path not in self.batch:
    #         self.batch[event.src_path] = queue.Queue()
    #     self.batch[event.src_path].put(payload)
    #     self.batch_lock.release()

    def on_created(self, event):
        event_time: str = AbstractEventHandler.get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        payload = "{0} - {1}: {2} : {3}".format(event_time, event.event_type, modified_item_type, event.src_path)
        # print(payload)

        self.batch_lock.acquire()
        if event.src_path not in self.batch:
            self.batch[event.src_path] = queue.Queue()
        self.batch[event.src_path].put(payload)
        self.batch_lock.release()

    def on_modified(self, event):
        event_time: str = AbstractEventHandler.get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        payload = "{0} - {1}: {2} : {3}".format(event_time, event.event_type, modified_item_type, event.src_path)
        # print(payload)

        self.batch_lock.acquire()
        if event.src_path not in self.batch:
            self.batch[event.src_path] = queue.Queue()
            self.batch[event.src_path].put(payload)
        self.batch_lock.release()

    def on_deleted(self, event):
        event_time: str = AbstractEventHandler.get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        payload = "{0} - {1}: {2} : {3}".format(event_time, event.event_type, modified_item_type, event.src_path)
        # print(payload)

        self.batch_lock.acquire()
        if event.src_path in self.batch:
            del self.batch[event.src_path]
        self.batch[event.src_path] = queue.Queue()
        self.batch[event.src_path].put(payload)
        self.batch_lock.release()

    def on_moved(self, event):
        event_time: str = AbstractEventHandler.get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        payload = "{0} - {1}: {2} : from {3} to {4}".format(event_time, event.event_type, modified_item_type, event.src_path, event.dest_path)
        # print(payload)

        self.batch_lock.acquire()
        if event.src_path not in self.batch:
            self.batch[event.src_path] = queue.Queue()
        self.batch[event.src_path].put(payload)
        self.batch_lock.release()


    # def on_modified(self, event: FileModifiedEvent):
    #     event_time: str = AbstractEventHandler.get_time()
    #     modified_item_type: str = "folder" if event.is_directory else "file"
    #     print("{0} - Modified: {1} : {2}".format(event_time, modified_item_type, event.src_path))
    #
    # def on_created(self, event: FileCreatedEvent):
    #     event_time: str = AbstractEventHandler.get_time()
    #     modified_item_type: str = "folder" if event.is_directory else "file"
    #     print("{0} - Created: {1} : {2}".format(event_time, modified_item_type, event.src_path))
    #
    # def on_modified(self, event: FileModifiedEvent):
    #     event_time: str = AbstractEventHandler.get_time()
    #     modified_item_type: str = "folder" if event.is_directory else "file"
    #     print("{0} - Modified: {1} : {2}".format(event_time, modified_item_type, event.src_path))