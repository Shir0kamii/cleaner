from cmd import Cmd
from enum import Enum
import grp
import os
import pwd
import shlex
import shutil
import stat
import sys

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
            return True  # exits

        self.set_prompt()
        self.traversal_argument = None


class FileActionShell(DirectoryTraversalShell):
    info_template = "{mode} | {user}:{group}"

    def default(self, line):
        return self.error("Unknow Syntax: {}", line)

    def error(self, error_msg=None, *args, **kwargs):
        if not error_msg:
            error_msg = "Unknow Error"
        error_msg = "*** " + error_msg.format(*args, **kwargs)
        print(error_msg, file=sys.stderr)
        return IterationCommand.keep

    def do_EOF(self, _):
        return IterationCommand.quit

    def emptyline(self):
        return IterationCommand.next

    def do_pass(self, _):
        return IterationCommand.next

    def do_enter(self, _):
        if not os.path.isdir(self.file):
            return self.error("enter command must be used on a directory")
        self.traversal_argument = True

    def do_quit(self, line):
        return IterationCommand.quit

    def do_help(self, line):
        super().do_help(line)
        return IterationCommand.keep

    @parsed_arguments_method
    def do_info(self):
        stat_info = os.stat(self.file)
        file_info = {}

        file_info["mode"] = stat.filemode(stat_info.st_mode)
        file_info["user"] = pwd.getpwuid(stat_info.st_uid).pw_name
        file_info["group"] = grp.getgrgid(stat_info.st_gid).gr_name
        print(self.info_template.format(**file_info))
        return IterationCommand.keep

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
        return IterationCommand.keep

    @parsed_arguments_method
    def do_chown(self, user_group_string):
        user_group = user_group_string.split(':', 1)
        if len(user_group) == 1:
            user, group = user_group[0], None
        else:
            user, group = user_group
        shutil.chown(self.file, user, group)
        return IterationCommand.keep

    @parsed_arguments_method
    def do_ls(self):
        if not os.path.isdir(self.file):
            return self.error("ls command must be used on a directory")
        for entry in os.listdir(self.file):
            print(entry)
        return IterationCommand.keep

    @parsed_arguments_method
    def do_cat(self):
        if not os.path.isfile(self.file):
            return self.error("{file} must be a file")
        with open(self.file) as fp:
            for line in fp:
                print(line.rstrip())
        return IterationCommand.keep
