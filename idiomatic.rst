Idiomatic Python: it's about communication
==========================================

by Luciano Ramalho, author of `Fluent Python <http://shop.oreilly.com/product/0636920032519.do>`_

    Here’s the plan: when someone uses a feature you don’t understand, simply shoot them. This is easier than learning something new, and before too long the only living coders will be writing in an easily understood, tiny subset of Python 0.9.6 <wink>.

    *Tim Peters, legendary Python core developer and author of* The Zen of Python.

It's very easy to become productive in Python, but to really reap all the benefits of this very expressive language it's worthwhile to become really fluent in it. Many of Python's best shortcuts are not special cases but actually leverage powerful abstractions that apply across the board. Learning and applying those idioms will make your code shorter, faster and easier to understend by other Pythonistas.

Iteration is one area of Python that's ripe with powerful idioms. Here is a non-idiomaitc snippet to output a string vertically:

::

    s = 'Hello'
    i = 0
    while i < len(s):
        print(s[i])
        i += 1


That works, but it's "unpythonic". It's not just a matter of style. The real issue is readability. This is way more readable:

::

    s = 'Hello'
    for c in s:
        print(c)


Using ``while`` in the first example not only makes it more verbose, it also hides the intent of the loop. If a loop is intended to iterate over items in a sequence (or any iterable), using ``for`` makes that intent clear. The ``while`` form should be used when the repetition is not tied to sequential iteration but depends on other termination logic.

Handling indexes directly is often a "code smell" in Python -- a sign that code may be improved. Sometimes you do need a numeric index besides the current item on each iteration. That's why the ``enumerate`` built-in generator function exists. Here's how it's used:

::

    s = 'Hello'
    for i, c in enumerate(s):
        print(i, '->', c)

Together with tuple unpacking, the ``enumerate`` `generator function <https://docs.python.org/3/library/functions.html#enumerate>`_ provides an elegant solution to retrieving indexes and items from any iterable -- while avoiding common off-by-one bugs when manually incrementing indexes. By the way, ``enumerate`` takes an optional ``start`` argument to initialize the index counter -- handy when you need the item numbering to start at 1, instead of 0.

Knowing all `68 built-in functions <https://docs.python.org/3/library/functions.html>`_ is a good way to improve your Python fluency. Functions like ``enumerate`` and ``zip`` are designed to aid ``for`` loops, while others like ``all``, ``any`` and ``sum`` make explicit loops unnecessary. What these functions do is not rocket science, but your program will be harder to read if you code by hand the logic provided by them. They are built-in because they solve common coding problems.

Other built-ins exist to provide functionality that require low-level services provided by the Python runtime, like `print` and `memoryview`. And of course, there are the built-in types. Take a look at all the `methods and operators <https://docs.python.org/3/library/stdtypes.html#types-set>`_ supported by ``set``: they can simplify a lot of program logic. That's no accident -- set theory and  logic are closely related fields.

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
