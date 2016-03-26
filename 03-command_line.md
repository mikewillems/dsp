# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1 'grep regX files_or_dirs' but defaults to current directory. (just reviewed grep, but still worth it)

2 if 'man _thing_' or 'help _thing_' doesn't work, '_thing_ --help' may be useful
piping to send output multiple places by stacking the pipes.

3 'export ENV-VAR-NAME=env-var-value'

4 equivalently, '$env:ENV-VAR-NAME=env-var-value'

5 'unset env-var-name'

6 '$env:MY_ENV_NAME' (redirect or pipe to editor or console) - shows content (if any) of that env var

7 'get-childitem Env:'   shows all the environment variables defined (unless filtered by grep, e.g.)

8 '(set -o posix ; set )' _pipe or redirect output_    shows all terminal but NOT environmental (i.e. non-exported variables). 

9 'export -n ENV-VAR-NAME'   demotes ENV-VAR-NAME to a shell variable.

10 '_some-command_ > /dev/null 2>&1 &'    can't not throw this in here as a reminder: runs some-command in the background, silencing all output by redirecting to devnull. I used to bash alias 'bkg' to do this appendix for when I want to open a program from the terminal, but now most linux flavors allow you to MOD- and start typing program names, which is usually faster.


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

list files in a directory (current if no argument)
list files including hidden files (which start with a '.')
list files with details (long listing)
list files with size in human readable format
list files with all modifications of l, a, and h
list files with modification time
list files, inhibiting group info but otherwise listing metadata and appending a filetype indicator to each filename

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:
1) -R is probably my most used, which lists recursively. I tried to write a windows interface to recursively browse to a user-variable depth.
2) -u sort by time last run/used - this is very useful for modifying the last-edited version of a file when going back through historical versions for bug fixes, but I've found it finnicky between systems.
3) -Q This is another I .bashrc alias to happen every time just because I think it's easier to read, and it encloses file names in double quotes.
4) -r reverses the order of a sort - useful surprisingly often.
5) -t sort by modification time - same reason as 2

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs breaks up long bash command argument lists into chunks that can be handled by various utilities, applying the specified command piecewise to each chunk. Generally, this is application of typical bash commands to many files. One example would be making a file for each name in a list such that these files can be written to programmatically. Say that you have a huge list of people and that each one needs to have some info added. You can grep for the list of .npp filenames:
    grep npp filenames.txt
 then use xargs to touch each filename:
    | xargs touch

changed by adding this line to allow restaging
