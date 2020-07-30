from watchdog.events import FileSystemEventHandler, FileSystemMovedEvent
from datetime import datetime


class AbstractEventHandler(FileSystemEventHandler):
    @staticmethod
    def get_time() -> str:
        now = datetime.now()
        return now.strftime("%m/%d/%Y, %H:%M:%S")

    def on_modified(self, event: FileSystemMovedEvent):
        pass