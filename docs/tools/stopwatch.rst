Stopwatch
===========

The stopwatch Tools function, allows the user to create many stopwatch as needed.

The function can be called with associating a variable to the function:

``stopwatch1 = stopwatch.start()``

and can be stopped, with the time occured, printed in the console, using:

``stopwatch.stop(stopwatch1)``

.. code-block:: python

    class stopwatch:
        "Create as many stopwatch as you need."
        def start():
            "Start a stopwatch. \nNote: The chronometer needs to be saved into a variable."
            import time
            return time.time()

        def stop(startTimer):
            "Stop a given chronometer, and prints out how much it took."
            import time
            elapsed = time.time() - startTimer
            hours, rem = divmod(elapsed, 3600)
            minutes, seconds = divmod(rem, 60)
            print(f"Execution time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:05.3f}")
            return elapsed

Note: The values printed out are automatically converted in a more readable size. 
But if you want to see all the time occured in the ``stopChronometer`` function, change the following line of code: 
``print(f"Execution time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:05.3f}")`` to: ``print(f"Execution time: {elapsed})``