from cmd import Cmd
import os
import shlex

from .filesystem import traversal, remove, move

ERROR_IGNORE = (KeyboardInterrupt,)
ERROR_PRINT = (Exception,)


def parsed_arguments_method(method):
    def new_method(self, line):
        return method(self, *shlex.split(line))
    return new_method

def filename_argument(argument):
    return os.path.expanduser(argument)


def launch_shell(directory):
    shell = FileActionShell()
    try:
        shell.launch(directory)
    except ERROR_IGNORE:
        pass
    except ERROR_PRINT as e:
        print("FATAL ERROR: {}".format(e))


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

    def postcmd(self, stop, line):
        if not self.iter_file():
            return True # exits

        self.set_prompt()
        self.traversal_argument = None
        return stop


class FileActionShell(DirectoryTraversalShell):

    def do_EOF(self, _):
        return True

    def emptyline(self):
        pass

    def do_pass(self, _):
        pass

    def do_enter(self, _):
        self.traversal_argument = True

    def do_quit(self, line):
        return True

    @parsed_arguments_method
    def do_rm(self):
        remove(self.file)

    @parsed_arguments_method
    def do_mv(self, filename):
        destination = filename_argument(filename)
        move(self.file, destination)
