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

It's a simply Python script::

    $ taskgen.py

If it's the first time you've run the script it will scrape the exercises and
store them to a local `tasks.json` file. It will then output a suggested task.
If you wish to refresh the task cache use the `refresh` argument::

    $ taskgen.py refresh

That's it!

Many thanks to ProgrammingPraxis for being such a wonderful source of
programming exercises.
