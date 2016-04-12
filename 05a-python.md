# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?
<br><br>
Lists and tuples are both python 'sequences' and have the sequence methods for accessing elements. These include array-style access via bracket notation, length (len) and comparison (cmp) operators, max and min functions, and functions (tuple and list) to convert between the two.
<br><br>
The chief ideological difference between the two is that a list stores many instances of something (ideally the same thing to get good performance), while tuples are essentially intended to be that instance (one of many). A tuple is a lightweight structure (similar to a struct in C) that packages multiple pieces of data into a unit - basically a compound data type. A tuple can store whatever type of information, but becomes useful when multiple tuples are used to store the same classes of information in the same places. This allows efficient (and nameless) access to the elements within.
<br><br>
Lists are similar to lists in other languages, and store heterogeneous types, but are most useful when storing the same type, so that memory can be managed for them more efficiently. They are fully mutable (unlike tuples which are completely immutable), and contain all the expected functions for adding, retrieving, and removing elements in arbritrary locations. Lists use bracket notation, while tuples use commas.
<br><br>
Of course, the lightweight, primitive-esque nature of tuples makes them suitable for dictionary keys, and python as such allows tuples (and of course not lists) as dictionary keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?
<br><br>
Like lists and tuples, sets and lists are both sequence types (in this case both mutable) in python and contain comparison, equivalence, and max/min operators (though set's comparisons actually use primitive notation, which is very convenient for set math). The primary difference is that list is inherently ordered, whereas a set is inherently unordered.
<br><br>
Accordingly, lists can be referenced and modified by index (a numerical key) and iterated over, while sets have no concept of a key or index, and each element acts as its own key. Thus, sets necessarily have no duplicates, because any duplicates represent the same key. Sets also have all common mathematical set operations built in, which is handy, whereas lists have sort operations built in. Finally, the set class can output a sorted list of its elements.
<br><br>
Performance for finding an element depends on how you're finding it, and on what's stored. If you have a sorted list or if you know an element's index, then performance finding an element is very fast, however finding an element without either of these conditions is slow (linear instead of constant time) because it requires iteration. Sets, on the other hand, behave similarly to a heap structure and are very fast at random searches, though not as fast in most cases as a numerically indexed lookup. When using sets to store integers (their ideal data type), however, the search time becomes similar. Note that both lists and sets can store arbitrary types.
<br><br>
An example of a list:<br>
I want to store a collection of email accounts, each containing an "account" object. I would furthermore like to be able to sort this list according to attributes of the objects. I use a list and allow my example to double for question 3. Note that I use sorted instead of sort with the cmp parameter, as sort was removed in python3 in favor of sorted, which works on any iterable collection and not just lists, as well as implementing timsort.<br>
```
# note to self - apparently underscores are significant in markdown files
from operator import attrgetter
#assume accounts.py has a list of account tuples
email_list=\[importAccountList(accounts.db)\]
emails_by_creation_date=sorted(email_list, key=attrgetter('creationDate'))
```
If the email data fields were stored in a tuple instead of an object for each account, then I would have to import itemgetter and use the itemgetter(field\_index) instead.
<br><br>
Sets are tricky, because most of the examples are mathematical in order to really justify using this data structure. Even so, one example might be a set of addresses. If I am a delivery service, I want to quickly check whether an address is in my database of deliverable addresses before looking up where it is and how much it would cost. So I might implement a seperate address set where each of the addresses is stored as a string with a standard formatting. (In reality, I would format the strings upon input and alphabetize the whole thing so that search would be very fast using a list, but bear with me...) 
<br><br>
In this case, I write a function to import addresses, probably in csv, and store them in a set. We were required to set up pandas, so I'll assume that's fair game and not roll a reader directly from scratch. Instead, I use the following and also the pickle library:
```
import pandas as pd
import cpickle as pk

reader=pd.read_csv(engine='c',filepath_or_buffer='https://www.address_list_provider.com/address_list.csv',chunksize=1)
address_set=set()
for chunk in reader:
	address_set.add(str(chunk))
f=open('/var/local/mailing_pos/address_set.save','wb')
pk.dump(address_set,f,-1)
f.close()
```

The next time I wanted to load the set, I could simply do it with 
```
f=open(addr_set_path,'rb')
address_set=pk.load(f)
f.close()
```

Now, with the data in the address\_set variable, I attempt a lookup with the new address:<br>
```
if newAddress in address_set:
	lookupAddressInfo()
else:
	raise ADDR_NOT_RECOGNIZED
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

The lambda construct is a convenient and intuitive way to combine the C concepts of abstract and inline functions. A lambda is a function which can be passed anonymously (in addition to just via a reference), and whose definition syntax allows it to be defined within other functions. More importantly, the anonymity prevents name conflicts where a function is needed for a parameter (in callback syntax, e.g., though python doesn't name them "callbacks"), but where multiple functions might be used for the same condition under different contexts.

Say you had a list, and wanted to use pyspread (a great library by Martin Manns) to display it and play with the values. You want to implement a sort function on all of the data points in a column (after the first) that initiates upon clicking the cell. I haven't fully learned how to do this, but presumably, a function is taken as an argument for a click in the GUI. You could specify this function as follows (some pseudocode is used):

```
import pyspread as sp

--- 
Assume that you have a spreadsheet object, S, which has location data in the first column of the first table. The object stored by each cell 2-N in column 1 is a pair of form (latitude, longitude) which you wish to sort by latitude to split into time zones. Now assume that there is a button for which you must provide a sorting function. 	
---

# other functions...



```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are awesome - it's a way of constructing lists by giving a formula for each term, and the syntax is close to mathematical notation (yay!). The main limitation (and what makes it not as powerful for certain scenarios) is the clarity and flexibility with which you can increment over a given range. The syntax for list comprehensions cannot process complex statements (past for and if loops), while the lambda used by map/filter can process a dynamic
function passed in at runtime.

For example, the following functions output equivalent code:

```
listEx = 'Metis is the best'.split()

def listComp():
    print [[word[len(word)-1]] for word in listEx]

def mapList():
    print map(lambda word: word[len(word)-1], listEx)
```

Set and dictionary comprehensions:

```
# Dictionary comprehensions take an argument for the key # for a particular value and assign it programmatically.

diction={x: x**2 for x in range(5,10)}

```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
```
from datetime import *
difference = datetime.datetime.strptime(date_stop,%m-%d-%Y) - datetime.datetime.strptime(date_start)

```

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





