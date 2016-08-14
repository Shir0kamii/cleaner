from cmd import Cmd
from enum import Enum
import os
import shlex
import shutil

from .filesystem import traversal, remove, move

ERROR_IGNORE = (KeyboardInterrupt,)
ERROR_PRINT = (Exception,)


def parsed_arguments_method(method):
    def new_method(self, line):
        return method(self, *shlex.split(line))
    return new_method


def filename_argument(argument):
    return os.path.expanduser(argument)


def filemode_argument(argument):
    return int(argument, base=8)


def launch_shell(directory):
    shell = FileActionShell()
    try:
        shell.launch(directory)
    except ERROR_IGNORE:
        pass
    except ERROR_PRINT as e:
        print("FATAL ERROR: {}".format(e))


class IterationCommand(Enum):
    keep = 0
    next = 1
    quit = 2


class DirectoryTraversalShell(Cmd):

    def launch(self, directory):
        self.traversal_argument = None
        self.file_iterator = traversal(directory)
        if not self.iter_file():
            return
        self.set_prompt()
        self.cmdloop()

    def iter_file(self):
        try:
            self.file = self.file_iterator.send(self.traversal_argument)
        except StopIteration:
            return False
        return True

    def set_prompt(self):
        self.prompt = "{} > ".format(self.file)

    def postcmd(self, iter_cmd, line):
        if iter_cmd is None:
            iter_cmd = IterationCommand.next
        if (iter_cmd == IterationCommand.quit or
                (iter_cmd == IterationCommand.next and not self.iter_file())):
            return True # exits

        self.set_prompt()
        self.traversal_argument = None


class FileActionShell(DirectoryTraversalShell):

    def do_EOF(self, _):
        return IterationCommand.quit

    def emptyline(self):
        return IterationCommand.next

    def do_pass(self, _):
        return IterationCommand.next

    def do_enter(self, _):
        self.traversal_argument = True

    def do_quit(self, line):
        return IterationCommand.quit

    @parsed_arguments_method
    def do_rm(self):
        remove(self.file)

    @parsed_arguments_method
    def do_mv(self, filename):
        destination = filename_argument(filename)
        move(self.file, destination)

    @parsed_arguments_method
    def do_chmod(self, mode):
        mode = filemode_argument(mode)
        os.chmod(self.file, mode)

    @parsed_arguments_method
    def do_chown(self, user_group_string):
        user_group = user_group_string.split(':', 1)
        if len(user_group) == 1:
            user, group = user_group[0], None
        else:
            user, group = user_group
        shutil.chown(self.file, user, group)
