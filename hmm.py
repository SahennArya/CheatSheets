import numpy as np

#Sahenn Arya - markov chain

#creating the starting states in a dictionary
states = {
    0 : "StateA",
    1 : "StateB",
    2 : "StateC"
}

#transition probability matrix
A = np.array([
    [0.18, 0.73, 0.09],
    [0.12, 0.10, 0.78],
    [0.58, 0.09, 0.33]
])

#simulating a random walk with n steps
#first we set the starting state to be any of the states from our dictionary. Then we set the previous state to be the starting state since there are no previous steps.
n = 15
startState = 0
print("\nrandom walk with",n,"steps")
print(states[startState], "-->", end=" ")
prevState = startState

#while there are steps remaining, the current state will be a random choice between the states, using the probabilities given in the transition matrix A.
#the new previous state will be the current state
while n-1:
    currState = np.random.choice([0,1,2], p=A[prevState])
    print(states[currState], "-->", end=" ")
    prevState = currState
    n-=1
print("\nend of walk")

#finding the stationary distribution of the markov chain
#using repeated matrix multiplication:
# Pij(n) = A^(n) ij - probability of reaching state j from state i after n steps can be found from ith row and jth column of nth order transition matrix
#can also be done using monte carlo and eigen vector but will give the same result

steps = 10**3
A_n = A

i = 0
while i<steps:
    A_n = np.matmul(A_n,A)
    i +=1
print("\nA^",steps, "=" , A_n,"\n")
print("π = ", A_n[0], "\n")

#starting at any state, the probability that you will get to state 0, 1, 2 = π[0], π[1], π[2] respectively