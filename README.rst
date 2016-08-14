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

=====
Usage
=====

Use `cleaner <directory>` to clean a messy directory

A shell will be spawn, with the prompt containing a filename. The command you
will type will take effect on this file. Next, another filename will be prompted
and each file of the directory will be submited to you this way.

To exit the shell, you can either type `quit`, `Ctrl-D` or `Ctrl-C`.

Use `rm` on a filename to remove an entry. If it's used on a directory, it
will recursively remove all its tree.

Use `mv <destination>` to move an entry to `<destination>`. If it's used on
a directory, it will recursively move all its tree to `<destination>`.

If you don't type anything, the shell will go to the next element. This same
effect will take place if you type `pass`.
