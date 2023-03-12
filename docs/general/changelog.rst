Changelog
=========
The version of the documentation specifies to what version is updated the documentation on the version of the library.
Also, it can happen that more than one release of the library can have the same version.

Library - Version 0.1.7 (12/03/2023)
------------------------------------
* Removed a phrase in ``changelog``
* Corrected a error in ``changelog``


Library - Version 0.1.7 (12/03/2023)
------------------------------------
* Completed the write of library versions previous of version 0.1.3

Documentation - Version 0.1.7 (12/03/2023)
------------------------------------------
* Updated the ``stopwatch`` section in ``tools`` to match with the changes of library version 0.1.7
* Updated the code in ``isEven`` section to match with the changes of library version 0.1.7
* Updated the code in ``isOdd`` section to match with the changes of library version 0.1.7
* Updated the code in ``Euler Totient Primality Test`` section to match with the changes of library version 0.1.6 and 0.1.7

Library - Version 0.1.7 (12/03/2023)
------------------------------------
* Removed all the useless prints statements of the ``boolean tools`` (isOdd, ...), you can verify from the return (True or False), but they will no longer be displayed
* Removed the print statements from ``Euler Totient Primality Test``, you can verify from the return (True or False), but they will no longer be displayed
* Changed the syntax of ``chronometer`` function in ``tools``
* Improvements to the description of ``stopwatch.start`` function

.. warning::
    If you update from a previous version, you have to change the name of the stopwatch functions

Documentation - Version 0.1.5 (12/03/2023)
------------------------------------------
* Improvements to ``changelog`` description

Library - Version 0.1.6 (12/03/2023)
------------------------------------
* Fixed bug, where from ``primalityTests`` you could import ``Euler Totient Function`` generating a ``Import Error``
* Improvements to ``Euler Totient Primality Test``, this feature is for large numbers, that now are being skipped if they can't be prime numbers, that avoids the time that occurs to calculate phi
* Fixed bug, where in ``tools``: ``isEven`` was returning ``True`` even if the numbers entered were odds
* Fixed bug, where in ``tools``: ``isOdd`` was returning ``True`` even if the numbers entered were evens

Documentation - Version 0.1.5 (12/03/2023)
------------------------------------------
* Fixed error in ``changelog``: ``Library - Version 0.1.4``
* Added new section ``Primality Tests``
* Added to ``Primality Tests``: ``Euler Totient Primality Test``
* Fixed errors in ``changelog``: ``Documentation - Version 0.1.2`` and ``Library - Version 0.1.3``
* Fixed indentation error in ``changelog``: ``Library - Version 0.1.4``
* Improvements to the description of ``changelog``

Library - Version 0.1.5 (12/03/2023)
------------------------------------
* Created ``primalityTests``
* Added to ``primalityTests``: ``EulerTotientPrimalityTest``

Library - Version 0.1.4 (11/03/2023)
------------------------------------
* Changed the name of ``functions`` section to ``mathFunctions`` to match with the name that can be found on the documentation.
* Fixed error where the python files: ``utility``, ``complex`` where still available when they have changed to ``tools``, ``mathFunctions``

.. warning::
    If you update from a previous version, you have to change the name of the functions written above.

Documentation - Version 0.1.3 (11/03/2023)
------------------------------------------
* General improvements
* Added to ``Forzo`` in ``Library Contributors``: ``Developer, Debugger`` roles
* Changed ``functions`` to ``mathFunctions``
* Improvements to description of Math Functions section

Documentation - Version 0.1.3 (11/03/2023)
------------------------------------------
* Fixed bug, where the theme hasn't changed. (`Issue #4 <https://github.com/Forzooo/cryptographyComplements/issues/4>`_ ,closed as resolved)
* Changed ``Library Developers`` to ``Library Contributors`` 
* Changed ``Documentation Writers`` to ``Documentation Contributors``
* Added ``pradyunsg`` to ``Documentation Contributors`` as ``Theme provider`` role


Documentation - Version 0.1.3 (10/03/2023)
------------------------------------------
* Changed the theme of documentation from ``Read The Docs`` to ``furo``.
* Added a warning to ``Library - Version 0.1.3``

Library - Version 0.1.3 (10/03/2023)
-------------------------------------
* Changed the name of ``utility`` section to ``tools`` to match with the name that can be found on the documentation.
* Changed the name of ``complex`` section to ``functions`` to match with the name that can be found on the documentation.

.. warning::
    If you update from a previous version, you have to change the name of the functions written above.


Documentation - Version 0.1.2 (10/03/2023)
-------------------------------------------
* Writing of the documentation has been completed, and it matches with the latest version available of the library.
* Set the theme of the documentation to ``Read The Docs theme`` from ``alabaster``.

Library - Version 0.1.2 (02/03/2023)
------------------------------------
* Added to ``complex`` section: ``Extended Euclidean Algorithm``
* Defined to int the parameters of ``Euler Totient Function``, ``Euclidean Algorithm``, ``Extended Euclidean Algorithm``, ``Base Discrete Logarithm``

Library - Version 0.1.1 (02/03/2023)
------------------------------------
* Added to ``complex`` section: ``Euclidean Algorithm``

Library - Version 0.10 (28/02/2023)
-----------------------------------
* Changed ``Discrete Logarithm`` to ``Base Discrete Logarithm``
* Minor improvements to ``Base Discrete Logarithm``

Library - Version 0.0.10 (27/02/2023)
-------------------------------------
* Improvements to cypher writing into a text file
* Improvements to syntax of ``isOdd`` and ``isEven``
* Improvements to syntax of ``isNumber``

Library - Version 0.0.9 (27/02/2023)
------------------------------------
* Modifies to print statement of ``Discrete Logarithm``
* Created ``startChronometer`` and ``stopChronometer`` functions and added to ``utility``

Library - Version 0.0.8 (26/02/2023)
------------------------------------
* Modified ``congruence`` and ``modulo`` to constants in ``Discrete Logarithm``

Library - Version 0.0.7 (26/02/2023)
------------------------------------
* Created ``Caesar Cypher`` and added to ``cyphers``

Library - Version 0.0.6 (26/02/2023)
------------------------------------
* Created ``Random Cypher`` and added to ``cyphers``
* Created ``write cypher`` function and added to ``cyphers``

Library - Version 0.0.5 (26/02/2023)
------------------------------------
* Set ``result = number``, of ``Euler Totient`` function, to ``result = int(number)``

Library - Version 0.0.4 (26/02/2023)
------------------------------------
* Improvements to ``Discrete Logarithm`` description
* Created ``isNumber`` function and added to ``utility``

Library - Version 0.0.3 (26/02/2023)
------------------------------------
* Created ``Discrete Logarithm`` function and added to ``complex``

Library - Version 0.0.2 (26/02/2023)
------------------------------------
* Changed ``number validation`` to ``utility``
* Created ``complex``
* Created ``Euler Totient Function`` and added to ``complex``
* Added description to ``isOdd`` and ``isEven`` functions

Library - Version 0.0.1 (25/02/2023)
------------------------------------
* Created ``number validation``
* Created ``isOdd`` and ``isEven`` functions and added to ``numberValidation``