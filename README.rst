.. image:: https://img.shields.io/pypi/v/cleaner.svg?maxAge=3600   :target: https://github.com/Shir0kamii/cleaner

#######
Cleaner
#######

Cleaner is a cool interactive shell that allows you to clean your directories
with less eforts.

=============
Why Cleaner ?
=============

Have you ever been tired to clean a messy `~/Downloads/` directory ? Do you
think this bunch of `ls` and `rm <file>` or `mv <file> <destination>` are
needed ?

Cleaner solve exactly this problem, submiting to you each file of the directory
you want to clean, and reducing the commands to type to `rm` and `mv
<destination>`.

============
Installation
============

Via pip
=======

you can just `pip install cleaner`

=====
Usage
=====

Use `cleaner <directory>` to clean a messy directory

A shell will be spawn, with the prompt containing a filename. The command you
will type will take effect on this file. Next, another filename will be prompted
and each file of the directory will be submited to you this way.

Directories end with a '/' character on the prompt.

To exit the shell, you can either type `quit`, `Ctrl-D` or `Ctrl-C`.

The `info` command prints a line containing some useful informations. The
default format is `<mode> | <user>:<group>` wiht `<mode>` being in the same
format than the first columns of a `ls --long` command in bash.

Use `enter` on a directory to list its tree. The directory will be printed
again after the traversal.

Use `rm` on a filename to remove an entry. If it's used on a directory, it
will recursively remove all its tree.

Use `mv <destination>` to move an entry to `<destination>`. If it's used on
a directory, it will recursively move all its tree to `<destination>`.

Use `chmod <mode>` to modify permissions of a file or directory. The shell will
keep the same file after this command.

Use `chown <user>[:<group>]` to modify ownership of the file or directory. The
shell will keep the same file after this command.

If you don't type anything, the shell will go to the next element. This same
effect will take place if you type `pass`.
