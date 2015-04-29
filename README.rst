Dojo Task Generator
===================

Generating new tasks for the London Python Code Dojo can be an onerous process.
Often suggestions are silly, incomprehensible, too complicated given the
amount of time we have in the dojo and/or obscure. It's also important to make
such tasks fun.

One of the regular suggestions for a task for the dojo to solve is a dojo
task generator. It's a joke among regular attendees.

However, I've decided to bite the bullet and this small Python script will
generate dojo ideas based upon programming exercises listed on the website
http://programmingpraxis.com/.

How Does it Work?
-----------------

Put simply, it's a scraper that first downloads all the exercises and then
suggests one of them.

Usage
-----

Remeber to install the requirements::

    $ pip install -r requirements.txt

It's a simple Python script, so run it like this::

    $ python taskgen.py

If it's the first time you've run the script it will scrape the exercises and
store them to a local ``tasks.json`` file. It will then output a suggested task.
If you wish to refresh the task cache use the ``refresh`` argument::

    $ python taskgen.py refresh

That's it!

Many thanks to ProgrammingPraxis for being such a wonderful source of
programming exercises.

Example Output
--------------

```
Modular Factorial

December 13, 2013 - http://programmingpraxis.com/2013/12/13/modular-factorial/


This question appears from time to time as an interview question or on the
coding-challenge web sites.

> Write a function that calculates _ n! _ (mod _ p _ ) when _ p _ is prime.
Then extend the function to calculate _ n! _ (mod _ m _ ) when _ m _ is not
prime. Can you calculate the factorials using fewer than _ n _ −1 modular
multiplications?

For instance, 1000000! (mod 1001001779) is 744950559.

Your task is to write the indicated functions. When you are finished, you are
welcome to [ read ](/2013/12/13/modular-factorial/2/) or [ run
](http://programmingpraxis.codepad.org/HZwVjALJ) a suggested solution, or to
post your own solution or discuss the exercise in the comments below.

Pages: [ 1 ](http://programmingpraxis.com/2013/12/13/modular-factorial/) [ 2
](http://programmingpraxis.com/2013/12/13/modular-factorial/2/)
```
