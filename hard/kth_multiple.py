import heapq


def kth_multiple(k: int) -> int:
    """
    Find the kth number such that the only prime factors are 3, 5, 7. Note that 3, 5, AND 7 do not all have to be factors.
    For example, first multiples are 1, 3, 5, 7, 9, 15, 21, 25, 27
    -----------
    To find the kth smallest 357-multiple, we could find all the (k-1) multiples, and then attempt to multiply all of them
    by (3, 5, 7) separately, and then find the min of all those multiplications. But that would definitely be overlapping work!
    """
    primes = [3, 5, 7]
    # keeps track of multiples we've already seen so that we don't re-add multiples to the heap. Size will become O(k)
    already_seen_multiples = {1}

    # Lets us determine the next largest multiple after curr_number in O(1) time. log(k) time to add, and add to it k times max.
    next_multiple_heap = [1]

    # keeps track of how many multiples we've created so far
    count = 0

    # current multiple
    curr_number = None
    while count < k:
        curr_number = heapq.heappop(next_multiple_heap)
        for prime in primes:
            new_multiple = prime * curr_number
            if new_multiple not in already_seen_multiples:
                heapq.heappush(next_multiple_heap, new_multiple)
                already_seen_multiples.add(new_multiple)
        count += 1
    if curr_number is None:
        raise ValueError("Should never be none after the loop")
    return curr_number
