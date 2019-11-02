# The method that prints all
# possible integers of length k.
# It is mainly a wrapper over
# recursive function generateAllKLengthRec()
total_queries = []


def generate(set, k):
    n = len(set)
    generateHelper(set, "", n, k)


# The main recursive method
# to print all possible
# strings of length k
def generateHelper(set, prefix, n, k):
    # Base case: k is 0,
    # print prefix
    if (k == 0):
        total_queries.append(int(prefix))
        print(prefix)
        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased, because
        # we have added a new character
        generateHelper(set, newPrefix, n, k - 1)

#tests
if __name__ == "__main__":
    generate([str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9)], 3)