def tallyvote(cats, dogs, species, idx, against=False):
    species_arr = cats if species == "C" else dogs
    vote_amount = -1 if against else 1
    species_arr[idx-1] += vote_amount

def solve(c, d, v, votes):
    # TODO: use (one/two) big hashmap instead?
    cats = [0 for x in range(c)]
    dogs = [0 for x in range(d)]
    for vote in votes:
        votefor, voteagainst = vote
        # tally vote for
        species, idx = votefor[0], int(votefor[1:])
        tallyvote(cats, dogs, species, idx, against=False)
        # tally vote against
        species, idx = voteagainst[0], int(voteagainst[1:])
        tallyvote(cats, dogs, species, idx, against=True)
    print(cats, dogs)

if __name__ == "__main__":
    INPUT_FILE = 'inputcatsdogs.txt'
    with open(INPUT_FILE, 'r') as f:
        num_testcases = int(f.readline())
        for testcase in range(num_testcases):
            c, d, v = [int(x) for x in f.readline().split()]
            votes = [tuple(f.readline().split()) for voter in range(v)]
            print("solving")
            solve(c, d, v, votes)
