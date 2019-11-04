'''

This is pseudocode for generating queries in the form of a string that
will then be passed on to our scrapy class to scrape data from a web form.

Structure:

    Queries should be passed on in the form of a string.
    For each website, assuming there is a search form, and assuming we can search by
    a case ID, we want to generate all possible queries to search for all possible results.

        Optimizations -
            1. Figure out what the minimum length of a query should be such that at it returns
            results (the search query term is not too broad, some sites don't return if query is too broad).
            2. Optional step: determine what queries will not return anything (example: 111 is too "broad"
            on some sites).

Code:

findMinimumLength()

    This function (returns type int) the minimum length we can use to search for queries.
    Example: On Santa Clara's search form for Case ID, the query "%1", "%12", are too broad and
    will not return results, as result size is too large. But "%123" will work, so we decide
    that our minimum length of query is 3.

    Considerations:
        Problem: some queries of size n do not work. For example, if n = 3 returns results,
            and we try "%111", then the query is deemed by the search form as too broad. Keep these edge cases
            in mind.
        Solution:
            Even if "%111" does not work, all possible queries of size n = 3 should still cover queries that involve
            "..111.." in the query. For example, in this situation, we assume a query would then be at least size 4,
            so then any other query would cover "..111.." such as "2111" (our query generator would test for "%211" and
            results would be returned.

generateQueries()

    This function is where we generate all queries to search for in the search form.

    #results of type stringArray of all possible queries
    #minQueryLength of type int

    minQueryLength = findMinimumLength()
    results = generateQueries
    return results
'''