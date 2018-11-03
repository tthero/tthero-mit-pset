###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # List of lists
    result = []

    # Duplicated dict
    cows_list = cows.copy()

    # Not sure if it is appropriate or not,
    # Remove all weights which are larger than limit
    temp = []
    for cow, weight in cows_list.items():
        if weight > limit:
            temp.append(cow)
    for k in temp:
        del cows_list[k]

    temp = []
    space = limit
    while True:
        # Just to initialise a max value
        try:
            # Initialise the diff to the largest value found
            diff = max(cows_list.values()) + limit
        except:
            # List is empty, get the result before breaking
            result.append(temp)
            break

        # completed => True,
        # 1) Not enough space for every single cow (space - weight < 0 for each cow)
        # 2) No more cows?
        completed = True
        for cow, weight in cows_list.items():
            if space - weight >= 0:
                completed = False
                # Get the cow with maximum weight
                if space - weight < diff:
                    diff = space - weight
                    biggest_cow = cow

        # If completed => False, more cows can still fit in
        if not completed:
            space -= cows_list[biggest_cow]

            temp.append(biggest_cow)

            del cows_list[biggest_cow]
        # Else, no more space, reset the space and temp to get another iteration
        else:
            result.append(temp)
            temp = []
            space = limit

    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result = []

    cows_list = cows.copy()

    for item in get_partitions(cows_list.keys()):
        eligible = True
        for trip in item:
            weight = sum([cows_list[cow] for cow in trip])
            if weight > limit:
                eligible = False

        if eligible:
            result.append(item)

    result = sorted(result, key=len)

    return result[0]


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

start = time.time()
print(greedy_cow_transport(cows, limit))
end = time.time()
print("Greedy cow algorithm takes {:0.3} seconds.".format(end - start))

start = time.time()
print(brute_force_cow_transport(cows, limit))
end = time.time()
print("Brute force cow algorithm takes {:0.3} seconds.".format(end - start))

