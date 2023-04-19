### Clue 1: The Hunt Begins ###

#### `man` ####

The first command we are going to learn is `man`, which is short for manual.
Typing `man [command]` will give you a help page (usually called a manpage)
for most commands.

#### `ls` ####

The next command we need to learn is `ls` (list). Type `man ls` and read the
description. Press `q` to exit. Then type `ls` and you should see something
like this:

    APPENDIX.md clues hide_clues.py LICENSE.md answer.py README.md

Items which are blue are directories and everything else is a file. Any time
you need to know which files and directories are available, type `ls`.

#### `cd` ####

We need a couple more tools before we can start clue hunting. To change to
another directory we use `cd` (change directory). You may notice that
`man cd` doesn't work. Sometimes there is no manpage for a command. In that
case google is your friend. Changing directories is pretty simple:

    cd clues

This puts us in the clues directory. To go up a directory, we can do this:

    cd ..

If you ever get lost, just do

    cd ~/scavenger-hunt

to return home. If you `cd` to the `clues` directory and do an `ls`, you
will notice that there are a lot of clue directories. Most of them contain
fake clues. Throughout our hunt we will be looking for real clues. Using
`cd`, navigate to `clues/12345` and type `ls`. You should see a single
file named `clue`.

#### `cat` ####

Finally we need to be able to look at our clues. First read the manpage for
`cat`, then do:

    cat clue

This should list the clue in your terminal. From now on, everything we need
will be contained in these clue files. It's a good idea to keep track of
all the clue folders (like `12345`) on a piece of paper. You can also do
things like copy all the clue files to your home folder, or cut and paste
the clue text into another file.

#### `Finding Clue 2` ####

Once you figure out the answer the question, run
python3 answer.py, to learn the location of the next clue.

If you give the wrong answer, the clue will not be there.

For this first clue, your answer is: 42

Run 'python3 answer.py', this is clue number 1, and the answer is 42
