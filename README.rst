============
 ErrorEmail
============

..
   .. image:: https://badge.fury.io/py/erroremail.png
       :target: http://badge.fury.io/py/erroremail

   .. image:: https://travis-ci.org/ionrock/erroremail.png?branch=master
	   :target: https://travis-ci.org/ionrock/erroremail

   .. image:: https://pypip.in/d/erroremail/badge.png
	   :target: https://pypi.python.org/pypi/erroremail


Send an error email when an you get an exception.

* Free software: BSD license
* Documentation: See Below

What does it do?
================

Here is how it works: ::

  with ErrorEmail(email_config):
      do_stuff()

If `do_stuff` raises an exception, it will send an email with the
traceback. That's it.


Configuration
=============

The ErrorEmail context manager accepts a configuration dictionary that
defines the To, From and SMTP server information. Here is an example: ::

  {
    'SERVER': 'smtp.myhost.com',
    'PORT': 25,
    'TO': ['foo@bar.com', 'baz@bar.com'],
    'FROM': 'erroremailer@myhost.com',
  }


ErrorEmail doesn't have robust email support at the moment. I'm happy
to accept pull requests!
