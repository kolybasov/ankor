from time import sleep
from threading import Thread

import xerox


class ClipboardMonitor(Thread):
    """ Monitor clipboard changes and report. """

    def __init__(self, reporter, interval=5):
        """ Create ClipboardMonitor instance as new Thread. """
        super().__init__()

        self._reporter = reporter
        self._interval = interval
        self._stopping = False

    def run(self):
        """ Run clipboard pooling and report to reporter function
        if content has been changed. """
        recent_value = ''
        while not self._stopping:
            new_value = xerox.paste()
            if new_value != recent_value:
                recent_value = new_value
                self._reporter(recent_value)
            sleep(self._interval)

    def stop(self):
        """ Stop clipboard poooling. """
        self._stopping = True
