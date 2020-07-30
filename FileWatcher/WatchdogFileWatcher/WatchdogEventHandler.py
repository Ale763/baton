from FileWatcher.AbstractFileWatcher.AbstractEventHandler import *


class WatchdogEventHandler(BaseEventHandler):
    def on_modified(self, event: FileSystemMovedEvent):
        event_time = self.__get_time()
        modified_item_type: str = "folder" if event.is_directory else "file"
        print("{0} - Modified: {1} : {2}".format(event_time, modified_item_type, event.src_path))