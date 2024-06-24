## Random module offers methods to simulate non-deterministic behaviour. 
# Choose random number of item from a list 

## randint() from range of intergers
# random.choice() provides a unifrom selection of a ranom element in a sequence.

# Returns a random integer N in a given range, such that start <= N <= end
# random.randint(start, end)
r1 = random.randint(0, 10)  
print(r1) # Random integer where 0 <= r1 <= 10

# Prints a random element from a sequence
seq = ["a", "b", "c", "d", "e"]
r2 = random.choice(seq)
print(r2) # Random element in the sequence

