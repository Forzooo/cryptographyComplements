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
    return(cypher)

def writeCypher(cypher):
    cypher = str(cypher)
    "This function writes a cypher, from a one executed, into a text file."
    with open("cypher.txt","w") as file:
        file.write(cypher)