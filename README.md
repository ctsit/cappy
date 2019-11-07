Cappy
=====

The REDCap API library that you build yourself.

Ideology
--------

A module should do one thing and do it well. Cappy calls the REDCap API. It
does not rate limit, it does not tell you how to organize the data you get
back, it does not handle errors nor declare any new exception types.


Usage
-----

The REDCap API requires a token and an endpoint. Also, Cappy uses a version file
that specifies the API calls you want to support. You pass all three of these
into the API constructor to get an instance of the API. This instance has
methods corresponding to the definitions in the JSON file.

Any API call that pushes data takes the data object as the first parameter.
This would be calls like `import_record` and the like. Any [iterable][] thing
other than data is passed by a keyword parameter. More information can be found
in the docstring of `cap.py`.

Happy REDCapping!

[iterable]: https://docs.python.org/3/glossary.html#term-iterable

