from is_api.commands.command import Command
from is_api.utils.requestor import Requestor


class CommandInvoker:

    def __init__(self, requestor: Requestor):
        self.__requestor = requestor

    def execute(self, command: Command):
        requestor = self.__requestor

        requestor.request(method=command.method(), url=command.url(), params=command.params(), data=command.data())
