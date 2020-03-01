import pandas as pd

# Because the Geckil and Anderson way of representing payoff matrices was silly.

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

payoff = {'P2_Confess': [[X1, Y1], [X2, Y2]], 'P2_Deny': [[X3, Y3], [X4, Y4]]}
payoff = pd.DataFrame(payoff, index=['P1_Confess', 'P1_Deny'])

# ---------
# Find Player 2 dominant strategy, if one exists.

# Get payoffs for players 1 and 2 if player 1 confesses.
p1_confess_payoffs = payoff.loc["P1_Confess", :]
# Format these payoffs as a dataframe, where each element is the payoff for the player (column) given that player 2 takes a certain action (row).
p1_confess_payoffs = pd.DataFrame(p1_confess_payoffs.values.tolist(), index=p1_confess_payoffs.index, columns=['P1', 'P2'])

# Among player 2 payoffs, find the maximum and return the row (action) that this corresponds to.
p2_strat_p1_conf = p1_confess_payoffs.loc[:, 'P2'].idxmax()

# Repeat above for situation where player 1 denies.
p1_deny_payoffs = payoff.loc["P1_Deny", :]
p1_deny_payoffs = pd.DataFrame(p1_deny_payoffs.values.tolist(), index=p1_deny_payoffs.index, columns=['P1', 'P2'])

p2_strat_p1_deny = p1_deny_payoffs.loc[:, 'P2'].idxmax()

# If P2's strategy is the same regardless of whether P1 confesses or denies, we have a P2 dominant strategy.
p2_dom_strat = None
if p2_strat_p1_conf == p2_strat_p1_deny:
    p2_dom_strat = p2_strat_p1_conf
else:
    print("P2 does not have a dominant strategy.")

# ---------
# Find Player 1 dominant strategy, if one exists.

# Get payoffs for players 1 and 2 if player 2 confesses.
p2_confess_payoffs = payoff.loc[:, "P2_Confess"]
# Format these payoffs as a dataframe, where each element is the payoff for the player (column) given that player 1 takes a certain action (row).
p2_confess_payoffs = pd.DataFrame(p2_confess_payoffs.values.tolist(), index=p2_confess_payoffs.index, columns=['P1', 'P2'])

# Among player 1 payoffs, find the maximum and return the row (action) that this corresponds to.
p1_strat_p2_conf = p2_confess_payoffs.loc[:, 'P1'].idxmax()

# Repeat above for situation where player 2 denies.
p2_deny_payoffs = payoff.loc[:, "P2_Deny"]
p2_deny_payoffs = pd.DataFrame(p2_deny_payoffs.values.tolist(), index=p2_deny_payoffs.index, columns=['P1', 'P2'])

p1_strat_p2_deny = p2_deny_payoffs.loc[:, 'P1'].idxmax()

# If P1's strategy is the same regardless of whether P1 confesses or denies, we have a P2 dominant strategy.
p1_dom_strat = None
if p1_strat_p2_conf == p1_strat_p2_deny:
    p1_dom_strat = p1_strat_p2_conf
else:
    print("P1 does not have a dominant strategy.")

# ---------
# Find dominant strategy equilibrium, if one exists.

if p1_dom_strat is None or p2_dom_strat is None:
    print("No dominant strategy equilibrium.")
else:
    print("Dominant strategy equilibrium is (" + p1_dom_strat + ", " + p2_dom_strat + ")")
