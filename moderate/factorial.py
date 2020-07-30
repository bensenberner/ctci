"""
Write an algorithm that computes the number of trailing zeros in a factorial.

A factorial, n! is
n * (n-1) * (n-2) * ... * 2 * 1

If you were to find the prime factors within all those n numbers, then the number of trailing zeros
is equal to min(# of 2s in the prime factors, # of 5s).
For example:
10! contains
10, 9, 8, 7, 6, 5, 4, 3, 2, 1
if I take all the prime factors of these I get
5, 2, 3, 3, 2, 2, 2, 7, 3, 2, 5, 2, 2, 3, 2
which is
7, 5^2, 3^4, 2^8

min(2, 8) (the number of 5s and 2s respectively) is 2, so we would expect there to be 2 trailing zeros

sure enough https://www.wolframalpha.com/input/?i=10%21
10! = 3628800

Naive Approach:
go through every number
find its prime factorization
increment a 2 and a 5 counter
then take the min

how long does it take to factor a number?

naive runtime:
take the number, start dividing it by 2 until it doesn't give a remainder of 0. then 3. keep incrementing divisors until the number is 1.
assuming it is a power of 2, you could ostensibly divide it log(n) times before you reach 1. but you might have to try every number
between 2 and n before you've divided it down to 1. So...let's upper bound at n * log(n).

Thus, if you have to factor every number, then it would take n^2 * log(n) (since there are n numbers).
This is bad! How can we speed this up?

well...using the sieve of erasthosthenes, we can compute all the primes from 1 up til sqrt(n). (we know that know prime larger than sqrt(n) can divide n).

now our runtime is n^2 * log(sqrt(n))...but the log was never the problem.

Okay, this is kinda dumb. It's definitely deterministic...how many 5s and 2s are within a number.

5 count:
0
0
0
0
1
1
1
1
1
2

following that pattern, you'd just do
num_fives = (n - (n % 5)) / 5
num_twos = (n - (n % 2)) / 2
return min(num_fives, num_twos)

but wait...once you hit 25, you would have an EXTRA 5.
okay. I got it. I just need to find the nearest power of 5 (rounded down).
maybe I should use logs?

okay so let's take the case of 126
it's got
5, 25, 125
which contain 1, 2, and 3 fives respectively.
so I would want to see "what is the power to which I raise 5 to get to 126?"
and it is a little bit above 3.
So then I say "okay, then I have to sum([1, 2, 3]) to catch all these "EXTRA" 5s.
But of course, I included 5 originally, so I gotta subtract 1.
"""


def count_trailing_zeros(n):
    """
    first, count the number of numbers that contain at least 1 "5"s which are present in the expansion of n!
    then count the number of numbers that contain at least 2 "5"s. We have previously counted some of them, of course,
    but in the second iteration of the loop we are including the "second" 5 that they contained.
    And so on for the third.
    The loop should run, at most, log_5(n) times.
    """
    count = 0
    num = n
    while num > 1:
        num = int((num - (num % 5)) / 5)
        count += num
    return count
