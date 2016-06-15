import time
import pyperclip
import notify2

from core.parser import __parser__
from core.plugins import __modules__
from common.colors import red
from subprocess import call


def notify(process_result):

    notify2.init('Slx7hS3ns3on')
    notify = notify2.Notification(
        'Slx7hS3ns3on', process_result, "dialog-info")
    notify.show()


def process(clipboard_content):

    if __parser__.url(clipboard_content) is True:

        url_result = __modules__['print_url'].run(clipboard_content)
        notify(str(url_result))

    elif __parser__.timestamp(clipboard_content) is True:

        timestamp_result = __modules__['print_timestamp'].run(clipboard_content)
        notify(str(timestamp_result))

    else:
        print red(clipboard_content + " not in patterns")


class ClipboardWatcher(object):

    def __init__(self, pause):
        self._pause = pause
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            if pyperclip.paste() != recent_value:
                recent_value = pyperclip.paste()
                process(recent_value)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True

if __name__ == "__main__":

    watcher = ClipboardWatcher(1)
    call(["xsel", "-bc"])

    while True:
        try:
            watcher.run()
        except KeyboardInterrupt:
            watcher.stop()
            break
