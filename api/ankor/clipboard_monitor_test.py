from time import sleep

import xerox

from clipboard_monitor import ClipboardMonitor

TEST_INTERVAL = .1
TEST_STRING = 'clipboard_test'


def TEST_REPORTER(*args):
    pass


class TestClipboardMonitor:
    """ ClipboardMonitor class tests. """

    def test_run(self):
        """ Test if ClipboardMonitor will report changes to callback
        function. """
        def reporter(str):
            assert TEST_STRING == str

        cb_monitor = ClipboardMonitor(reporter, TEST_INTERVAL)
        cb_monitor.start()

        xerox.copy(TEST_STRING)
        sleep(TEST_INTERVAL)

        cb_monitor.stop()

    def test_stop(self):
        """ Test if ClipboardMonitor can stop itself. """
        cb_monitor = ClipboardMonitor(TEST_REPORTER, TEST_INTERVAL)
        cb_monitor.stop()

        assert cb_monitor._stopping is True
