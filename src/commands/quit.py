import sys

from commands.base import Command


class QuitCommand(Command):
    def execute(self):
        sys.exit
