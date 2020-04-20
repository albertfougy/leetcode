# Intuition and Algorithm

# Let's try to simulate giving change to each customer buying lemonade. 
# Initially, we start with no five dollar bills, and no ten dollar bills.

    # • If a customer brings a ＄5 bill, then we take it.

    # • If a customer brings a ＄10 bill, we must return a five dollar bill. 
    # If we don't have a five dollar bill, the answer is False, 
    # since we can't make correct change.

    # • If a customer brings a ＄20 bill, we must return ＄15.

        # If we have a ＄10 and a ＄5, then we always prefer giving change in that, 
        # because it is strictly worse for making change than three ＄5 bills.

        # Otherwise, if we have three ＄5 bills, then we'll give that.

        # Otherwise, we won't be able to give ＄15 in change, and the answer is False.

class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True