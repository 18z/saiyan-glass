import datetime
from common.abstracts import Module


class print_timestamp(Module):

    def run(self, timestamp):

        ts = float(timestamp)
        _datetime = datetime.datetime.fromtimestamp(
            ts).strftime('%Y-%m-%d %H:%M:%S')

        return _datetime
