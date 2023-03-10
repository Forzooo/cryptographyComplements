Random Cypher
=============

This cypher is randomly generated and is written in a .txt file in the same folder where is your Python script.

.. code-block:: python

    def randomCypher():
        "This function generates a cypher and randomize the elements inside it."
        import string, random
        elements = string.ascii_letters + string.digits + string.punctuation + "àèéìòù" + " "
        cypher = {elements[i]: None for i in range(len(elements))}

        already_sorted = []
        element_sorted = None

        for i in cypher.keys():
            while True:
                sort = random.randint(0, len(elements) -1)
                if sort in already_sorted:
                    continue
                else:
                    break

            already_sorted.append(sort)
            element_sorted = elements[sort]

            cypher[i] = element_sorted

        writeCypher(cypher)
        return cypher

Note: The generated cypher is written in a .txt file in the same folder where your Python script is located.