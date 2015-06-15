Idiomatic Python: it's about communication
==========================================

by Luciano Ramalho, author of `Fluent Python`_

    Here’s the plan: when someone uses a feature you don’t understand, simply shoot them. This is easier than learning something new, and before too long the only living coders will be writing in an easily understood, tiny subset of Python 0.9.6 <wink>.

    *Tim Peters, legendary Python core developer and author of* The Zen of Python.


Here is a snippet to output a string vertically:

::

    s = 'Hello'
    i = 0
    while i < len(s):
        print(s[i])
        i += 1


That works, but is not "Pythonic". It's not just a matter of style or cleverness. The real issue is readability. This is more readable:

::

    s = 'Hello'
    for c in s:
        print(c)


Using ``while`` in the first example not only makes it more verbose, it also hides the intent of the loop. If a loop is intended to iterate over items in a sequence (or any iterable), using ``for`` makes that intent clear. 

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

If you are not used to the list comprehension syntax, you're likely to find the ``for`` loop solution more readable. But if you are working with Python on a regular basis, you really should take the time to get comfortable with list comprehensions and other constructs that use similar syntax, like generator expressions, ``dict`` comprehensions and ``set`` comprehensions. Not only are they shorter and faster than the equivalent code using a plain ``for`` loop, they also communicate the intent much better. A ``for`` loop may be doing any number of things, but a list comprehension is designed to do one thing only: to build a list. As soon as I spot a list comprehension, I know the code is building a new list object, not changing an existing list in-place, nor doing something else for the sake of side effects.

I have seen code that uses list comprehensions just for the side effects, collapsing what should be a ``for`` loop into a "clever" one-liner. If code was only ever read by computers we'd still be writing numeric op codes by hand. Grace Hopper wrote the first compiler to make it easier for humans to write code, and reading is a pre-requisite to writing. If you are abusing a list comprehension to collapse a loop and not to build a list, the computer will do your bidding, but the next human reader of that code will waste time deciphering your cleverness.

Writing idiomatic code is not about using language-specific features everywhere, it's about using them when they make sense and make your intent clear. There are no hard and fast rules about clear communications, but knowing your audience is key. 

We are really talking about human communications, not computer science. Being fluent in a language also implies being a polyglot within that language: choosing appropriate idioms depending on the social context. This applies to computer languages as well. 

If you're using Python to teach algorithmic thinking, it may be a good idea to delay the use of list comprehensions on a first course. I also have serious doubts about the wisdom of "objects first" approaches to teaching programming. Introducing object notation and the idea of changing state through methods seems wise, so students can leverage libraries to build interesting programs. But having them build classes and tackle inheritance issues on a first programming course are distractions from algorithmic thinking.

On the other hand, professional development teams should strive to write idiomatic code because it's more effective to spread the word about best practices than it is to waste time, over and over again, understanding and debugging all the ways different people decide to code something that has a standard solution. "There should be one -- and preferably only one -- obvious way to do it." wrote Tim Peters in the Zen of Python. A list comprehension is the obvious way to build a list by selecting items from an iterable.

Among people who make a living coding in Python, learning to write idiomatic code is not just a matter of style. It makes economic sense, by improving communications. That's why every profession has a specialized jargon: so that improvised descriptions can be replaced by precise terms with standard meanings. Design patterns are cataloged and named for the same reason.

Idiomatic code is also about standard patterns, just on much a smaller scale. Idioms can ease communication many times every day, so they can have a bigger impact on productivity than larger architectural patterns.


    **Idiomatic Python: it's about communication** by Luciano Ramalho is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License`_.

.. _Fluent Python: http://shop.oreilly.com/product/0636920032519.do
.. _Creative Commons Attribution-ShareAlike 4.0 International License: http://creativecommons.org/licenses/by-sa/4.0/

.. raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Python tuples: immutable but potentially changing</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/fluentpython/orablog/blob/master/changing-tuples.rst" property="cc:attributionName" rel="cc:attributionURL">Luciano Ramalho</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
