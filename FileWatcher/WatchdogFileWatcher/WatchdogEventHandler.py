from watchdog.events import FileModifiedEvent, FileCreatedEvent

from FileWatcher.AbstractFileWatcher.AbstractEventHandler import *


class WatchdogEventHandler(AbstractEventHandler):
    def __init__(self):
        super().__init__()

    def on_created(self, event: FileCreatedEvent):
        event_time: str = AbstractEventHandler.get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        print("{0} - Modified: {1} : {2}".format(event_time, modified_item_type, event.src_path))

    def on_modified(self, event: FileModifiedEvent):
        event_time: str = AbstractEventHandler.get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        print("{0} - Modified: {1} : {2}".format(event_time, modified_item_type, event.src_path))