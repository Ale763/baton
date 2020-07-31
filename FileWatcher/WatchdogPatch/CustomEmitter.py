from watchdog.observers.api import DEFAULT_EMITTER_TIMEOUT
from watchdog.observers.polling import PollingEmitter


class CustomEmitter(PollingEmitter):

    def __init__(self, event_queue, watch,
                 timeout=DEFAULT_EMITTER_TIMEOUT,
                 stat=default_stat, listdir=os.listdir, logger=None):
        super(CustomEmitter, self).__init__(event_queue,
                                            watch,
                                            timeout,
                                            stat,
                                            listdir)
        self._take_snapshot = lambda: self._take_safe_snapshot(
            self.watch.path, self.watch.is_recursive, stat=stat,
            listdir=listdir)
        self.logger = logger
        self.folder_was_missing = None

def _take_safe_snapshot(self, path, is_recursive, stat, listdir):
    try:
        snapshot = DirectorySnapshot(path, is_recursive,
                                     stat=stat,
                                     listdir=listdir)
        if self.folder_was_missing:
            self.logger.info("Observer successfully found the missing "
                             "directory {}.".format(path))
        self.folder_was_missing = False
        return snapshot
    except FileNotFoundError as fe:
        if not self.folder_was_missing:
            self.folder_was_missing = True
            self.logger.info("Observer can't find the directory {}."
                             "".format(path))
            self.logger.exception(fe)
            if self.logger.level == logging.DEBUG:
                traceback.print_exc()

    def queue_events(self, timeout):

        # We don't want to hit the disk continuously.
        # timeout behaves like an interval for polling emitters.
        if self.stopped_event.wait(timeout):
            return

        with self._lock:
            if not self.should_keep_running():
                return

            # Get event diff between fresh snapshot and previous snapshot.
            # Update snapshot.
            new_snapshot = self._take_snapshot()
            if new_snapshot is None:
                return
            events = DirectorySnapshotDiff(self._snapshot, new_snapshot)
            self._snapshot = new_snapshot

            # Files.
            for src_path in events.files_deleted:
                self.queue_event(FileDeletedEvent(src_path))
            for src_path in events.files_modified:
                self.queue_event(FileModifiedEvent(src_path))
            for src_path in events.files_created:
                self.queue_event(FileCreatedEvent(src_path))
            for src_path, dest_path in events.files_moved:
                self.queue_event(FileMovedEvent(src_path, dest_path))

            # Directories.
            for src_path in events.dirs_deleted:
                self.queue_event(DirDeletedEvent(src_path))
            for src_path in events.dirs_modified:
                self.queue_event(DirModifiedEvent(src_path))
            for src_path in events.dirs_created:
                self.queue_event(DirCreatedEvent(src_path))
            for src_path, dest_path in events.dirs_moved:
                self.queue_event(DirMovedEvent(src_path, dest_path))