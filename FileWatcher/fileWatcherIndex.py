from enum import Enum
from FileWatcher.AbstractFileWatcher.AbstractFileWatcher import AbstractFileWatcher


class FileWatcherStrategies(Enum):
    WATCHDOG = 0

    @staticmethod
    def get_all():
        result = {}
        for strategy in FileWatcherStrategies:
            result[strategy.name] = strategy
        return result

    @staticmethod
    def get_strategy(p_strategy_name):
        for strategy in FileWatcherStrategies:
            if p_strategy_name == strategy.name:
                return strategy
        return None

    @staticmethod
    def get_default():
        return FileWatcherStrategies.WATCHDOG


class FileWatcherFactory:
    @staticmethod
    def get_strategy(p_strategy=FileWatcherStrategies.WATCHDOG) -> AbstractFileWatcher:
        strategy_switch = {
            FileWatcherStrategies.WATCHDOG: AbstractFileWatcher,
        }



