import os
import logging
# from pprint import PrettyPrinter

import click
import click_log

log = logging.getLogger(__name__)
click_log.basic_config(log)


class OsxLaunchCleaner(object):

    def __init__(self):
        log.debug("OsxLaunchCleaner()")

        self.files = {
            '/Library/LaunchAgents/': [],
            '/Library/LaunchDaemons/': [],
            os.path.expanduser('~/Library/LaunchAgents/'): []
        }

        for p in self.files.keys():
            self.files[p] = os.listdir(p)

    def report(self):
        log.debug('report()')

        for p in self.files.keys():
            files = self.files[p]
            for f in files:
                file_str = click.style(f, fg='green')
                print(os.path.join(p, file_str))


@click.command()
@click_log.simple_verbosity_option(log)
def main():
    log.debug('main')
    olc = OsxLaunchCleaner()
    olc.report()


if __name__ == '__main__':
    main()
