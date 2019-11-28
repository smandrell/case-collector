# from itertools import product

marin_query_set = [str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9)]


def generate(query_length):
    return product(marin_query_set, repeat=query_length)


def product(*query_set, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in query_set] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return ["%" + "".join(tup) + "%" for tup in result]

print(generate(3))

# num_possible_query_chars = len(marin_query_set)
# generate_helper(marin_query_set, "", num_possible_query_chars, query_length)
# return total_queries


# The main recursive method to print all possible strings of length 'query_length'
# def generate_helper(query_set, prefix, num_possible_query_chars, query_length):
#     # Base case: query_length is 0,
#     # print prefix
#     if query_length == 0:
#         total_queries.append("%" + prefix + "%")
#         if len(total_queries) == 1000:
#             print(total_queries)
#         return total_queries
#
#     # One by one add all characters from 'query_set'
#     # and recursively call for 'query_length' equals to 'query_length - 1'
#     for i in range(num_possible_query_chars):
#         # Next character of input added
#         new_prefix = prefix + query_set[i]
#
#         # k is decreased, because
#         # we have added a new character
#         generate_helper(query_set, new_prefix, num_possible_query_chars, query_length - 1)


# tests
# def run_query_generator():
#     generate(character_set, 3)
#     return total_queries
