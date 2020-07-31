from watchdog.events import FileSystemEventHandler, FileSystemMovedEvent
from datetime import datetime
import pytz
TIMEZONE = "Europe/Brussels"


class AbstractEventHandler(FileSystemEventHandler):
    @staticmethod
    def get_time() -> str:
        now = datetime.now()
        timezone = pytz.timezone(TIMEZONE)
        return timezone.localize(now).strftime("%m/%d/%Y, %H:%M:%S")

    def on_created(self, event: FileSystemMovedEvent):
        pass

    def on_modified(self, event: FileSystemMovedEvent):
        pass

    def on_deleted(self, event: FileSystemMovedEvent):
        pass

    def on_moved(self, event: FileSystemMovedEvent):
        pass