# Corporate setting: you have a list of employee votes represented as integers
# These integers actually represent the IDs of your fellow employees. 
# And yes, people can indeed vote for themselves.
# An employee gets elevated to the exclusive board member position only if they 
# bag at least n / 3 votes, with n being the total number of votes. 

# Task: find out the ID of this popular employee. If no one hits the vote mark, return -1.
# If multiple employees received at least n / 3 votes, return any of them!

# The votes are delivered to you in list format. As an illustration, [1, 2, 3, 3, 3]
# means employees 1 and 2 voted for themselves, and employee 3 received three votes. 
# Hang tight-there can be edge cases, such as no votes or everybody voting for themselves.

# Your end goal is to return the lucky candidate's ID if they secure a seat on the board. 
# If no one qualifies, return -1.



from collections import defaultdict

def elect_board_member(votes):
    # implement this
    n = len(votes)
    majority = n/3
    winner = -1
    voted_candidates = defaultdict(int)
    if n != 0:
        for vote in votes:
            if vote in voted_candidates:
                voted_candidates[vote] = voted_candidates[vote] + 1
            else:
                voted_candidates[vote] = 1
        sorted_voted_candidates = sorted(voted_candidates.items(), key= lambda  x: x[1], reverse=True)
        c1,v1 = sorted_voted_candidates[0]
        if float(v1) >= majority:
            winner = c1
    return winner
    

print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1
