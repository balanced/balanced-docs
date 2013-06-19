README
==========

Create FAQ items in the `General Support` => `General FAQs` directory. The FAQ file structure should adhere to the following format:

      ---

      layout: faq
      author: Donnie Brasco
      title: A super commonly asked support question here?
      category: fees
      tags:
      - balanced
      - payments
      - faq
      - fees

      ---

      Question body goes here. You may write markdown in the body. See [Darling Fireball] (http://daringfireball.net/projects/markdown/) for the full spec.

Save the filename as a **slugged** format of the title ending with the file extension `.md`. I.E. convert all space to dashes, and remove special characters (question marks `?` and periods `.` are ok). Prepend a number to the FAQ item as well, simply the next number in the sequence *(i.e. 045)*.

Example:

       045-A-super-commonly-asked-support-question-here?.md

**For a FAQ item to show up in the help section on the [website](https://www.balancedpayments.com/help), there must be a `category` attribute on the FAQ item.** Which also means, if you don't want a FAQ item to show up on the public help page, simply omit the category.

Example:

      category: fees


Current list of categories
--------------------------

+ api
+ payouts
+ signup
+ chargebacks
+ processing
+ fees
+ security
+ fraud
+ data
+ legal
+ marketing
+ end_user

Category are lazy created, so feel free to create a new category for a FAQ item as needed.

**Last modified:** *06/19/2013 04:10pm by Justin Keller*