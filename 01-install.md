# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

###Q1. Python Version 2 or 3

Did you install Python 2 or 3? Why?  

I installed both with 3 as default because I want to support the growth to 3. 3 also has nicer syntax sometimes (that is stricter and more C-like, which I prefer). On the other hand, I have had a very much easier time using external libraries with 2, and dislike the removal of parameter packing. It makes something that is already confusing and imo juvenile for a language even more difficult to understand. So if I have to do that using someone else's code, I really don't want to work around it in a weird way.

###Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

At the prompt, simply typing python -V should display it.
