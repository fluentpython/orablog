N reasons to level up with Python
==========================================

by Luciano Ramalho, author of `Fluent Python <http://shop.oreilly.com/product/0636920032519.do>`_

    Here’s the plan: when someone uses a feature you don’t understand, simply shoot them. This is easier than learning something new, and before too long the only living coders will be writing in an easily understood, tiny subset of Python 0.9.6 <wink>.

    *Tim Peters, legendary Python core developer and author of* The Zen of Python.

It's easy to write useful code in Python, but to be really productive you should become fluent in it. Python is highly consistent and expressive. Many of Python's best shortcuts are not special cases but actually leverage powerful abstractions that apply across the board. Learning and applying those idioms will make your code shorter, faster and easier to understend by other Pythonistas.

Python Data Model...

#1 Avoid reinventing the wheel
------------------------------

This is a one-liner to generate one of 4.7e+21 passwords from the best random bytes source your OS provides::

    >>> import os, base64; base64.b64encode(os.urandom(9))
    'Ai6TAmUrr1cw'

The motto of the Python standard library is "batteries included". From ...



#_ Grok advanced libraries
---------------------------

Your Python code probably depends on powerful packages such as `pandas`_, `SQLAlchemy`_ or `Django`_. Such sophisticated tools take full advantage of the Python Data Model, operator overloading, and the instrospection and metaprogramming features of the language. For example, `Flask`_ uses function decorators pretty much everywhere. Speaking of Web frameworks, consider this simple Django model class::

    class Movie(models.Model):
    
        title = models.CharField(max_length=255)
        year = models.PositiveIntegerField()
    
        class Meta:
            ordering = ('title', 'year')
            unique_together = ('title', 'year')
   
        def __str__(self):
            return '{} ({})'.format()

What does that assigment to ``title`` really mean? How about the inner class, is that a metaclass? And how does Django process it? Short answers: the ``model.CharField`` class is a descriptor, the inner class is not a metaclass and Django reads its attributes through introspection of the model class body at import time. A descriptor is bound to a class attribute, as the assignment suggests, but its goal is to control access to instance attributes -- the fields of individual records in the ``Movie`` model. Django uses the metaclass mechanism of Python behind the scenes to perform much of the magic of its ORM, but there is no hint of that in the example code. Descriptors, introspection and metaclasses are some of the advanced Python features you won't see in the official Python tutorial or in introductory courses and books. Also, knowing the distinction between "import time" and "run time" is a key for non-trivial Python programming, including function decorators and all the advanced features I just mentioned.

To make the most of the best frameworks and libraries available for Python -- and to create the next big hit on PyPI -- you need m... 





Python data model and metaprogramming features such as attribute descriptors, decorators and metaclasses.  


#_ Prevent bugs
----------------

Iteration is one area of Python that's ripe with powerful idioms. Python's ``for`` loop is great because it frees us from handling an index variable directly, avoiding off-by-one errors that are common in other languages. But sometimes we want the index, for example, if you want to number the items in a list when displaying it. Here is a non-idiomatic way to number a list from ``1``::

    >>> fruit = ['apple', 'banana', 'cheery', 'kiwi']
    >>> for i in range(1, len(fruit) + 1):
    ...     print(i, fruit[i])
    ...
    1 apple
    2 banana
    3 cheery
    4 kiwi


Tinkering with the index variable invites bugs. The idiomatic solution to this example uses the ``enumerate`` built-in generator function::

    s = 'Hello'
    for i, c in enumerate(s, 1):
        print(i, '->', c)

Another common reason for manually computing index values manually is iterating over two or more sequences in parallel. That use case is covered by the ``zip`` built-in generator. Again, no index variable needed.

The ``with`` construct is another feature that prevents bugs: a spring-loaded mechanism that closes files, releases locks and creates . An tuple unpacking, eminently Pythonic, catches bugs early by making sure the number of items provided match exactly the number of items expected. These are just some of the bug-saving features built in the language. Use them well.


#2 Leverage new features and APIs
--------------------------------------------

I've been witnessing the evolution of Python since 1998, and what I've seen is harmonious, consistent and significant progress. So it's always been worthwhile to keep up with what's new in the language and the standard library. Recently I fixed script that read CSV files simply by tweaking it to run in Python 3, because the standard library ``csv`` module in Python 2 does not handle Unicode well. However, if we rely primarily on blog posts, StackOverflow answers and hearsay to learn how to use Python we may not always get the most up-do-date solutions.



Only rarely I've seen new features that were not real improvements. The transition from Python 1.6 to 2.0 was remarkably smooth. The jump to 3.0 was traumatic, but I 

#X Better performance

Intelligent use of built-in types can make your programs run much faster. For example, the various set operators can save you from writing many lines of code, and they are built with extensively tested C code -- so those operators can reliably handle millions of items per second. Arrays can replace lists while saving memory, and also allow faster operations. The `struct` module allows high-level, yet efficient processing of binary data, and the `memoryview` type lets you do it all while sharing memory, avoiding much unnecessary data hauling. Beyond the built-ins, libraries like NumPy and `pandas` provide very powerful, highly optimized data structures and functions to process them using all available cores of your machine.

Besides efficient data structures, Python also provides modern control structures that you may not have seen elsewhere. With the `yield` keyword we can write functions that may be suspended and resumed later. This is the basis of generator functions like those in the itertools module that can handle streams of data of any size on-demand, without wasting memory or CPU cycles. Once you get the hang of `yield`, you'll discover new ways of organizing your code to handle large data sets.

Generator functions can also be used as coroutines for concurrent programming. The ``asyncio`` package bundled in Python 3.4` -- also for 3.3, from PyPI -- allows efficient, asynchronous programming the same ideas that made Node.js famous, but with a much more pleasant, maintainable and safe coding style, using coroutines and futures natively. No need to look into the abyss of callback hell. If you're stuck with Python 2 but considering new projects in Node.js for asynchronous network programming, take a deep look at ``asyncio`` and its young but growing eco-system of external libraries. The well-established Tornado asynchronous framework is now compatible with `asyncio`, so you can mix and match features of both.

Speaking of concurrency, there are some myths and misconceptions regarding Python concurrency... Some regard threads in Python as useless because of the GIL -- the Global Interpreter Lock which prevents multiple Python threads from running in parallel. However, the GIL has a small impact on I/O bound systems, especially for network I/O, given the high latency of TCP/IP. That's why Node.js with its single application thread manages to scale. If you prefer to use threads instead of `asyncio` you'll be happy to know that every I/O function in the Python standard library releases the GIL while waiting for a response from the OS, I/O bound threads actually do make progress in parallel thanks to the concurrency features of the underlying OS network stack. Therefore, if you're comfortable with threads and locks, you can use them profitably for network programming in Python. But before settling on the traditional way of doing things with the ``threading`` module, take the time to study the new ``concurrent.futures`` package added in Python 3.2 -- also available for Python 2.7 as the ``futures`` package in PyPI. That package makes threads almost trivial to use for many use cases. It also supports processes, bypassing the GIL and leveraging available CPU cores for compute-intensive tasks.









Browsing the docs for the `68 built-in functions <https://docs.python.org/3/library/functions.html>`_ is a good way to improve your Python fluency. Functions like ``enumerate`` and ``zip`` are designed to aid ``for`` loops, while others like ``all``, ``any`` and ``sum`` make explicit loops unnecessary. What these functions do is not rocket science, but your program will be harder to read if you code by hand the logic provided by them. They are built-in because they solve common coding problems.

Other built-ins exist to provide functionality that require low-level services provided by the Python runtime, like `print` and `memoryview`. And of course, there are the built-in types. Take a look at all the `methods and operators <https://docs.python.org/3/library/stdtypes.html#types-set>`_ supported by ``set``: they can simplify a lot of program logic. That's no accident -- set theory and  logic are closely related fields.

#X Improving communications


Now suppose you want to make a list with the vowels that appear in a string. Here's one way to do it:

::

    s = 'Hello'
    vowels = set('aeiou')
    found = []
    for c in s:
        if c.lower() in vowels:
            found.append(c)

That's not as awkward as the first ``while`` example, but it's not as direct as this:

::

    s = 'Hello'
    vowels = set('aeiou')
    found = [c for c in s if c.lower() in vowels]

If you are not used to the list comprehension syntax, you're likely to find the ``for`` loop solution more readable. But if you are working with Python on a regular basis, you really should take the time to get comfortable with list comprehensions and other constructs that use similar syntax, like generator expressions, ``dict`` comprehensions and ``set`` comprehensions. Not only are they shorter and faster than the equivalent code using a plain ``for`` loop, they also convey the intent much better. A ``for`` loop may be doing any number of things, but a list comprehension is designed to do one thing only: to build a list. As soon as I spot a list comprehension, I know the code is building a new list object, not changing an existing list in-place, nor doing something else for the sake of side effects.

I have seen code that uses list comprehensions just for the side effects, collapsing what should be a ``for`` loop into a "clever" one-liner. If code was only ever read by computers we'd still be writing numeric op codes by hand. Grace Hopper wrote the first compiler to make it easier for humans to read and write code. If you abuse a list comprehension to collapse a loop and not to build a list, the computer will do your bidding, but the next human reader of that code will waste time deciphering your cleverness.

Writing idiomatic code is not about using language-specific features everywhere, it's about using them when they make sense and make your intent clear. There are no hard and fast rules about clear communications, but knowing your audience is key. 

We are really talking about human communications, not computer science. Being fluent in a language also implies being a polyglot within that language: choosing appropriate idioms depending on the social context. This applies to computer languages as well. 

If you're using Python to teach algorithmic thinking, it may be a good idea to delay the use of list comprehensions on a first course. I also have serious doubts about the wisdom of "objects first" approaches to teaching programming. Introducing object notation and the idea of changing state through methods seems wise, so students can leverage libraries to build interesting programs. But having them build classes and tackle inheritance issues on a first programming course are distractions from algorithmic thinking.

On the other hand, professional development teams should strive to write idiomatic code because it's more effective to spread the word about best practices than it is to waste time, over and over again, understanding and debugging all the ways different people decide to code something that has a standard solution. "There should be one -- and preferably only one -- obvious way to do it." wrote Tim Peters in the Zen of Python. A list comprehension is the obvious way to build a list by selecting items from an iterable.

Among people who make a living coding in Python, learning to write idiomatic code is not just a matter of style. It makes economic sense, by improving communications. That's why every profession has a specialized jargon: so that improvised descriptions can be replaced by precise terms with standard meanings. Design patterns are cataloged and named for the same reason.

Idiomatic code is also about standard patterns, just on much a smaller scale. Idioms can ease communication many times every day, so they can have a bigger impact on productivity than larger architectural patterns.


    **Idiomatic Python: it's about communication** by Luciano Ramalho is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License`_.

.. _Creative Commons Attribution-ShareAlike 4.0 International License: http://creativecommons.org/licenses/by-sa/4.0/

.. raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Python tuples: immutable but potentially changing</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/fluentpython/orablog/blob/master/changing-tuples.rst" property="cc:attributionName" rel="cc:attributionURL">Luciano Ramalho</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
