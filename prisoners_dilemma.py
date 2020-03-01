import pandas as pd

# Enter prisoner 1's payoffs.
#X1 = input("Enter a value for X1: ")
#X2 = input("Enter a value for X2: ")
#X3 = input("Enter a value for X3: ")
#X4 = input("Enter a value for X4: ")
X1 = 2
X2 = -1
X3 = 4
X4 = 3

# Enter prisoner 2's payoffs.
#Y1 = input("Enter a value for Y1: ")
#Y2 = input("Enter a value for Y2: ")
#Y3 = input("Enter a value for Y3: ")
#Y4 = input("Enter a value for Y4: ")
Y1 = 2
Y2 = 4
Y3 = -1
Y4 = 3

# -----

# Prisoner 1's payoff matrix:
Prisoner1 = pd.DataFrame({'P2_Confess': [X1, X2], 'P2_Deny': [X3, X4]})

# Find maximum payoff for each Player 2 strategy.
A1 = max(Prisoner1.loc[:, 'P2_Confess'])
A2 = max(Prisoner1.loc[:, 'P2_Deny'])

# Find dominant strategy for player 1.
P1_DS = None
if A1 == Prisoner1.iloc[0, 0] and A2 == Prisoner1.iloc[0, 1]:
    P1_DS = "confess"
    print("Prisoner 1's dominant strategy is to confess.")
elif A1 == Prisoner1.iloc[1, 0] and A2 == Prisoner1.iloc[1, 1]:
    P1_DS = "deny"
    print("Prisoner 1's dominant strategy is to deny.")
else:
    print("Prisoner 1 has no dominant strategy.")

# -----

# Prisoner 2's payoff matrix:
Prisoner2 = pd.DataFrame({'P1_Confess': [Y1, Y3], 'P1_Deny': [Y2, Y4]})

# Find maximum payoff for each Player 2 strategy.
B1 = max(Prisoner2.loc[:, 'P1_Confess'])
B2 = max(Prisoner2.loc[:, 'P1_Deny'])

# Find dominant strategy for player 2.
P2_DS = None
if B1 == Prisoner2.iloc[0, 0] and B2 == Prisoner2.iloc[0, 1]:
    P2_DS = "confess"
    print("Prisoner 2's dominant strategy is to confess.")
elif B1 == Prisoner2.iloc[1, 0] and B2 == Prisoner2.iloc[1, 1]:
    P2_DS = "deny"
    print("Prisoner 2's dominant strategy is to deny.")
else:
    print("Prisoner 2 has no dominant strategy.")

# -----
if P1_DS is not None and P2_DS is not None:
    print("Dominant strategy equilibrium is (" + P1_DS + ", " + P2_DS + ")")
else:
    print("There is no dominant strategy equilibrium for this game.")
