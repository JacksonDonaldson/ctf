import pydealer

def value(hand):
    total = 0
    for c in hand:
        if c in "1JQK":
            total+=10
        elif c == "A":
            total += 1
        else:
            total += int(c)
    return total

def getTrueCount(playerHand, otherHands):
    count = 0
    for c in playerHand + "".join(otherHands):
        if c in "23456":
            count +=1
        elif c in "798":
            pass
        else:
            count -=1
    return count / 2

def tryR(rules, dealerHand, playerHand, otherHands):
    actualDealerValue = value(dealerHand[0])
    actualPlayerValue = value(playerHand)
    count = getTrueCount(playerHand, otherHands)

    if actualDealerValue == 1:
        actualDealerValue = 11

    
    for rule in rules:
        dealerValue, playerValue, hard, negateCount, onlyCount = rule

        if not hard and "A" in playerHand and actualPlayerValue + 10 <= 21:
            if dealerValue == actualDealerValue and playerValue+10 == actualPlayerValue:
                if onlyCount <= count <= negateCount:
                    return True
                
        elif hard:
            if dealerValue == actualDealerValue and playerValue == actualPlayerValue:
                if onlyCount <= count <= negateCount:
                    return True
    return False

def match(rules, dealerHand, playerHand, otherHands):
    dealerValue = value(dealerHand[0])
    playerValue = value(playerHand)
    count = getTrueCount(playerHand, otherHands)
    

    if dealerValue == 1:
        dealerValue = 11

    if "A" in playerHand and 20 <= (playerValue + 10) <=21:
        #print(playerHand)
        return False


    if playerValue < 12:
        return True

    if playerValue >= 17:
        return False
    
    if dealerValue < 8:
        return False

    if count < -1 and playerValue <15:
        return True
    return playerValue < 12

    if count >= 1 and (dealerValue == 9 or dealerValue == 10):
        return False
    
    if count >= 1 and playerValue >= 16:
        return False
    if count >= 2:
        return False

    

    for r in rules:
        dealerV, playerV = r
        if dealerValue == dealerV and playerValue == playerV:
            return True
    return False


def getWinOdds(rules):
    rounds = 10000
    wins = 0
    
    for _ in range(rounds):
        deck = pydealer.Deck()
        deck.decks_used = 2
        deck.shuffle()
        dealerHand = "".join([i.value[0] for i in deck.deal(2)])
        others = "".join([i.value[0] for i in deck.deal(10)])
        playerHand = "".join([i.value[0] for i in deck.deal(2)])

        

        while tryR(rules, dealerHand, playerHand, others):
            playerHand += deck.deal(1)[0].value[0]

        if value(playerHand) > 21:
            continue

        dvalue = value(dealerHand)
        if("A" in dealerHand and 18<= dvalue + 10<=21):
            dvalue +=10
        while dvalue < 18:
            dealerHand += deck.deal(1)[0].value[0]
            dvalue = value(dealerHand)
            if("A" in dealerHand and 18<= dvalue + 10<=21):
                dvalue +=10
        vhand = value(playerHand)
        if "A" in playerHand and vhand + 10 <= 21:
            vhand += 10
        
        if dvalue > 21 or vhand > dvalue:
            wins+=1
    return wins / rounds

def evaluateGeneration(generation):
    result = []
    for i in range(len(generation)):
        result.append((i, getWinOdds(generation[i])))
    return result


#genetic algorithm:
#1. generate 100 random sets of rules
#2. run fitness test on all, take top 50
#3. combine randomly to get 90 new sets (mutate occasionally)
#4. randomly generate 10 new rules
#5. repeat...?

import random
def generateRandomRule():
    dealerValue = random.randint(2, 11)
    playerValue = random.randint(2, 21)
    hard = random.randint(1, 5) > 1
    negateCount = random.randint(-5, 5)
    onlyCount = random.randint(-5, negateCount)
    return (dealerValue, playerValue, hard, negateCount, onlyCount)

currentGeneration = []
for i in range(150):
    currentGeneration.append(generateRandomRule())

f = [(10, 5, True, -4, -5), (7, 20, False, -4, -5), (5, 19, False, 1, -4), (2, 17, True, -3, -3), (10, 13, False, 0, -1), (11, 7, True, -2, -5), (10, 15, False, 5, 0), (6, 5, True, -5, -5), (4, 7, True, 1, 0), (5, 7, False, 1, -1), (5, 12, False, -5, -5), (2, 14, True, 3, -2), (10, 7, True, -1, -2), (6, 2, True, 3, -1), (6, 21, True, 3, 1), (3, 13, True, 5, -2), (10, 21, True, -3, -4), (3, 3, True, 4, -4), (10, 20, True, 0, -4), (6, 19, True, 3, 0), (11, 19, True, 2, -3), (11, 19, True, 1, -2), (9, 13, True, 5, 0), (9, 4, True, -4, -5), (2, 7, True, -2, -5), (8, 3, True, -3, -4), (10, 13, True, 1, -4), (6, 17, True, 1, 1), (3, 3, True, -4, -4), (3, 13, False, -4, -5), (5, 5, False, 1, 0), (2, 7, True, -4, -5), (6, 17, True, 3, 1), (3, 14, True, 3, 1), (11, 2, True, 0, -2), (3, 21, True, -3, -5), (8, 5, True, 5, -3), (10, 12, True, -4, -4), (11, 14, True, -3, -4), (8, 14, True, 5, 0), (4, 17, True, 1, -4), (9, 10, True, -4, -5), (7, 9, True, 3, -4), (9, 20, True, -5, -5), (9, 6, True, -5, -5), (4, 10, True, 5, 3), (11, 2, True, 0, -5), (5, 14, True, -5, -5), (11, 12, True, 4, 4), (9, 6, True, 4, -3), (9, 7, False, 4, -3), (4, 13, True, -5, -5), (6, 4, True, 0, -3), (6, 12, False, -5, -5), (4, 2, False, 2, -2), (6, 3, False, 2, 1), (10, 19, True, 5, 1), (8, 3, True, 5, -4), (4, 19, True, -3, -3), (6, 17, True, 3, -1), (7, 5, True, 0, -3), (11, 10, False, 3, -3), (7, 15, True, 4, -3), (5, 4, True, 3, 1), (9, 17, True, -3, -5), (3, 2, False, 1, -5), (11, 17, True, 0, -1), (9, 3, True, -2, -4), (5, 9, True, 4, 3), (8, 4, False, -2, -2), (11, 2, False, -1, -1), (4, 16, True, 4, 2), (6, 12, False, 3, 2), (6, 3, True, 2, -4), (7, 13, True, 1, -1), (6, 8, True, -3, -4), (7, 12, True, -4, -4), (9, 4, True, -3, -5), (2, 15, True, 4, -4), (10, 2, False, 4, 1), (7, 17, True, 2, -5), (4, 10, True, 1, -5), (9, 19, True, 2, -4), (5, 17, True, -5, -5), (2, 18, True, 0, 0), (3, 19, True, 0, -1), (4, 20, True, 5, -1), (5, 21, True, 5, -5), (8, 5, True, 3, -5), (6, 16, True, -3, -5), (8, 6, True, -2, -5), (5, 5, True, -3, -5), (11, 21, True, -2, -3), (2, 14, False, -4, -4), (10, 11, True, 2, -3), (11, 9, True, -3, -3), (2, 5, True, -3, -3), (4, 2, True, 4, 2), (7, 10, False, 2, -3), (7, 10, True, -1, -3), (7, 7, True, 2, -4), (4, 3, False, -5, -5), (3, 15, True, -1, -5), (2, 15, True, -4, -5), (11, 2, False, -4, -4), (5, 9, True, 4, 0), (8, 19, True, -4, -5), (10, 16, True, 4, -3), (5, 10, True, 0, -4), (3, 5, True, 3, 2), (4, 19, True, -1, -3), (8, 9, True, 3, 2), (7, 12, True, 4, -3), (7, 20, True, 3, -4), (11, 18, True, 1, -2), (5, 13, False, -4, -4), (10, 8, True, -2, -3), (11, 9, True, -4, -4), (4, 8, True, 4, 4), (4, 16, False, -1, -5), (7, 3, True, 3, 3), (3, 21, True, 2, 2), (8, 15, True, -5, -5), (9, 10, True, 2, -3), (4, 16, True, -4, -5), (6, 17, True, -1, -4), (9, 18, False, -2, -5), (11, 15, False, -1, -1), (11, 14, True, 0, -3), (6, 7, False, 2, -2), (8, 6, True, 5, -3), (7, 11, True, 4, -3), (11, 9, True, 2, -2), (2, 12, True, 5, -5), (2, 6, True, 2, -1), (4, 4, True, -5, -5), (7, 13, False, 0, -3), (8, 4, True, 2, -4), (2, 19, False, -5, -5), (4, 3, True, 4, -5), (5, 11, True, 1, -4), (5, 8, False, 3, -3), (8, 7, True, 2, -1), (4, 8, True, 4, 3), (7, 2, True, 4, -5), (3, 7, True, -4, -4), (2, 17, True, -1, -5), (8, 6, True, -4, -4), (4, 15, True, -3, -5), (3, 20, True, 2, 1), (7, 7, False, -5, -5), (4, 8, True, 3, -2), (4, 4, False, 0, -4), (8, 6, True, -1, -3), (4, 4, False, -5, -5), (3, 2, True, 2, -4), (2, 13, True, -3, -4), (6, 8, True, -5, -5), (7, 5, False, -3, -4), (2, 12, False, 4, 3), (4, 5, True, -1, -3), (4, 19, False, -4, -5), (3, 3, True, -3, -3), (6, 9, False, 4, -4), (3, 21, True, 0, -5), (6, 7, True, 3, -5), (10, 7, True, 4, 0), (7, 19, True, -4, -4), (9, 17, True, -3, -5), (10, 17, True, 1, -3), (9, 15, False, -4, -4), (10, 21, True, 2, -5), (6, 5, True, -2, -2), (11, 21, True, -2, -5), (3, 6, True, -2, -4), (6, 13, True, -4, -5), (8, 21, True, -3, -3), (3, 5, True, 1, -5), (9, 5, False, 4, 2), (4, 4, True, 3, -3), (11, 10, True, 5, -4), (2, 4, True, 2, 2), (11, 7, True, -5, -5), (8, 6, True, -2, -5), (8, 11, True, -1, -5), (8, 3, True, -1, -5), (7, 15, True, -5, -5), (8, 13, True, 1, -5), (11, 8, True, 4, -1), (6, 2, True, 5, 1), (9, 17, True, 3, 2), (5, 3, True, -4, -4), (10, 5, True, -5, -5), (9, 5, True, -2, -4), (4, 3, True, 3, 2), (4, 8, True, 2, 1), (5, 21, True, 4, -2), (2, 17, True, -4, -5), (2, 7, True, 5, 0), (11, 12, True, 4, 3), (3, 17, True, -2, -3), (8, 13, True, -1, -2), (7, 19, True, -2, -2), (8, 13, True, -4, -5), (4, 7, True, 2, 2), (5, 4, True, 3, -3), (11, 6, True, -5, -5), (4, 7, True, -4, -4), (11, 13, True, -1, -4), (7, 16, True, -3, -5), (3, 9, True, -2, -3), (6, 11, True, 5, 4), (10, 9, True, 4, 1), (8, 2, True, 3, -2), (3, 17, True, -4, -4), (5, 14, True, 3, -1), (6, 20, False, 2, -3), (5, 8, True, 5, 2), (2, 6, True, -5, -5), (8, 15, True, -4, -5), (4, 12, False, 5, -1), (6, 8, False, -2, -5), (5, 11, True, 4, 2), (6, 19, True, 0, -3), (10, 9, True, 5, -4), (2, 5, True, -4, -5), (11, 2, True, 0, 0), (7, 5, True, 3, 1), (3, 5, True, 1, 0), (2, 3, False, 3, -2), (9, 17, True, -3, -5), (4, 5, True, 1, -3), (3, 17, False, 0, -3), (3, 16, False, 4, -2), (3, 5, True, 4, -3), (6, 21, True, 1, 1), (8, 12, True, 3, 3), (5, 3, True, 1, 1), (10, 7, True, 2, -1), (5, 21, True, -4, -4), (4, 4, False, 1, -5), (4, 21, True, 3, -2), (6, 8, True, -5, -5), (8, 5, True, 2, -4), (5, 10, True, -3, -3), (9, 12, True, 0, -1), (6, 8, True, 1, -2), (3, 5, True, 5, -3), (3, 21, True, -2, -5), (5, 6, True, 0, -5), (4, 20, True, 4, 1), (7, 11, True, -3, -5), (2, 11, True, -2, -4), (9, 8, False, 3, -5), (2, 3, True, 4, -1), (6, 4, True, -3, -4), (11, 9, True, -3, -5), (6, 16, True, -2, -4), (8, 19, True, 4, -4), (6, 10, True, 0, 0), (11, 15, True, 2, -2), (8, 6, True, -2, -4), (9, 19, True, -5, -5), (5, 11, True, -3, -5), (2, 13, True, -2, -4), (4, 11, False, -3, -5), (5, 14, False, 5, 3), (11, 11, True, -1, -4), (5, 11, True, -2, -2), (11, 20, True, -1, -1), (11, 7, True, -4, -4), (6, 10, False, -4, -5), (3, 16, True, 4, -3), (6, 17, True, -5, -5), (7, 12, True, 2, -2), (3, 9, False, 4, -5), (7, 4, True, -4, -5), (3, 20, True, -1, -2), (2, 10, True, 1, -3), (2, 12, True, 1, -1), (8, 14, False, -5, -5), (6, 4, True, 5, -2), (3, 6, True, 4, 3), (6, 13, True, -2, -2), (11, 21, False, -3, -5), (5, 11, True, 0, -3), (4, 8, True, 2, -4), (9, 11, False, -5, -5), (7, 10, True, 4, 0), (4, 7, True, 1, -1), (9, 9, False, -3, -5), (6, 16, True, 5, 2), (4, 16, True, 2, -2), (4, 19, False, 5, 5), (10, 6, False, 0, -5), (8, 21, False, -3, -3), (5, 5, True, -5, -5), (5, 3, False, -3, -4), (10, 13, False, 3, 2), (8, 6, True, 3, -2), (11, 2, True, 5, -2), (9, 7, True, -5, -5), (4, 8, False, -5, -5), (3, 19, True, 3, -2), (9, 12, True, -4, -5), (4, 2, True, 0, -5), (3, 4, True, 4, -1), (9, 7, False, -1, -2), (3, 7, False, 2, -5), (11, 11, True, 2, -4), (8, 8, False, -5, -5), (11, 14, False, 1, -1), (8, 15, True, -3, -4), (5, 4, True, -2, -4), (6, 7, True, 0, -1), (9, 8, True, 3, -5), (7, 2, True, 4, -1), (7, 3, False, 5, 4), (2, 8, False, -2, -5), (6, 4, True, 2, -5), (10, 4, False, -3, -3), (8, 13, False, 1, -3), (10, 15, True, -5, -5), (6, 8, True, 3, -2), (2, 13, True, 1, 1), (2, 13, True, -4, -4), (7, 2, True, -4, -5), (3, 17, True, -4, -5), (11, 9, False, 0, -4), (9, 3, True, -2, -2), (7, 21, True, -3, -4), (10, 2, True, -3, -3), (9, 6, True, 2, 2), (8, 5, True, 2, -2), (11, 13, True, -3, -5), (9, 2, True, 5, -3), (8, 7, True, 4, -3), (9, 18, True, 5, 3), (10, 17, False, 5, 5), (6, 11, True, 5, 0), (9, 9, True, -4, -5), (11, 11, False, 0, -2), (9, 10, False, -5, -5), (4, 12, True, 5, -2), (11, 7, True, 5, -3), (7, 18, False, 3, -2), (10, 4, True, 4, -3), (10, 11, True, -2, -3), (5, 4, True, 3, -3), (4, 8, True, -2, -2), (8, 7, True, 0, -2), (6, 5, True, -3, -3), (11, 11, True, 1, 0), (9, 2, False, -3, -3), (5, 17, True, 1, 1), (5, 11, True, 3, -5), (2, 19, True, 4, -3), (2, 10, True, -2, -3), (8, 12, True, -1, -3), (7, 17, False, 3, 0), (6, 7, False, 0, -2), (4, 13, False, 1, -5), (8, 7, True, 3, -3), (5, 2, True, 3, -2), (2, 8, True, -5, -5), (4, 6, True, -5, -5), (6, 18, False, 5, -5), (9, 3, True, 4, 4), (4, 18, True, 4, -1), (9, 8, True, -4, -5), (8, 13, True, -4, -4), (9, 14, True, -5, -5), (7, 20, True, -5, -5), (5, 17, True, 3, 1), (9, 21, True, -5, -5), (6, 8, False, 1, -4), (7, 8, True, -5, -5), (11, 21, True, 4, 3), (5, 11, True, -5, -5), (8, 21, True, -3, -4), (7, 12, True, -4, -4), (10, 12, True, -2, -3), (4, 20, True, -4, -4), (5, 14, True, -3, -5), (6, 5, True, 2, -5), (4, 15, True, -2, -4), (4, 9, True, 3, -3), (11, 9, True, 0, 0), (3, 21, True, 1, -4), (6, 21, True, 1, -3), (5, 4, True, 4, -1), (6, 18, True, -1, -5), (5, 14, True, -1, -5), (6, 14, True, -4, -4), (11, 8, True, 1, 0), (5, 13, False, -2, -3), (10, 19, False, 1, 0), (7, 19, False, 0, -3), (8, 10, True, -5, -5), (4, 20, True, 2, -4), (9, 18, False, 3, -4), (9, 11, True, -4, -4), (10, 20, False, -2, -3), (7, 21, True, -3, -5), (3, 5, True, -1, -1), (8, 14, True, 4, 0), (10, 3, True, -4, -4), (4, 14, True, 4, -4), (9, 6, True, -1, -1), (7, 4, True, 4, -1), (2, 10, True, 5, -1), (9, 14, True, -4, -5), (4, 16, True, 4, 4), (7, 20, True, 0, -3), (4, 5, True, -1, -3), (10, 21, False, -5, -5), (6, 6, True, -2, -2), (3, 21, False, 3, -5), (4, 8, False, 0, -5), (7, 17, False, -3, -3), (5, 12, False, 2, -3), (7, 17, True, 5, -1), (9, 7, False, 5, 3), (7, 21, True, -5, -5), (2, 21, True, 4, 1), (6, 19, True, -1, -1), (10, 3, True, 0, -2), (4, 7, True, -1, -4), (4, 5, True, -4, -5), (7, 15, True, -2, -2), (11, 10, True, 5, -4), (8, 19, True, -1, -5), (11, 12, True, 0, -3), (7, 19, False, -1, -4), (2, 16, False, -4, -4), (5, 7, False, -5, -5), (10, 2, True, 2, -2), (7, 8, True, 0, -3), (9, 12, True, -4, -5), (2, 12, False, 3, -3), (11, 3, False, 5, 2), (8, 6, True, -2, -3), (6, 19, False, 0, -5), (6, 21, True, 2, -2), (7, 15, True, 5, -4), (8, 13, True, 1, 1), (4, 14, True, -3, -4), (11, 10, True, 2, 1), (6, 15, True, 4, 4), (6, 15, True, 2, -3), (5, 18, False, -2, -2), (4, 11, False, 2, 2), (2, 4, True, 0, -3), (10, 4, True, 2, -1), (8, 4, True, -5, -5), (10, 12, False, -1, -3), (10, 2, False, 3, 0), (11, 12, True, 0, 0), (9, 11, True, 0, -1), (8, 18, True, 2, 2), (8, 10, True, -2, -4), (2, 11, True, -2, -3), (9, 12, True, 5, 5), (3, 12, True, 1, 1), (11, 13, False, 0, -5), (4, 13, True, 4, 0), (4, 14, True, -5, -5), (4, 16, True, -2, -3), (8, 17, True, 4, 2), (10, 4, True, -5, -5), (8, 9, False, -3, -3), (11, 4, True, -3, -3), (3, 18, True, -3, -3), (8, 20, True, 2, 1), (8, 9, True, 1, 0), (2, 8, True, 4, 1), (2, 9, False, 1, -2), (7, 11, True, -1, -1), (2, 3, True, -3, -4), (4, 3, True, -4, -5), (11, 14, True, 0, -2), (11, 19, False, -3, -3), (10, 12, True, -3, -4), (7, 20, True, 3, 1), (2, 17, True, 0, 0), (7, 11, True, -4, -4), (11, 11, True, 3, -1), (7, 8, True, 5, -4), (4, 4, True, -4, -4), (4, 6, True, 3, -5), (6, 10, True, 5, 3), (11, 5, True, 1, -1), (8, 5, True, 5, -5), (4, 8, True, 4, 1), (6, 17, True, 3, -2), (2, 9, False, 3, -2), (3, 16, True, 2, -1), (10, 4, False, -4, -4), (2, 10, True, -1, -4), (9, 6, True, -3, -4)]
newf = [(7, 17, False, -3, -3), (4, 8, False, -5, -5), (10, 3, True, -4, -4), (8, 9, False, -3, -3), (8, 19, True, -1, -5), (4, 13, False, 1, -5), (8, 7, True, 3, -3), (5, 14, False, 5, 3), (2, 9, False, 3, -2), (7, 17, True, 2, -5), (8, 15, True, -5, -5), (11, 2, True, 0, 0), (8, 8, False, -5, -5), (3, 3, True, -4, -4), (8, 5, True, 5, -3), (10, 15, False, 5, 0), (8, 11, True, -1, -5), (7, 11, True, -1, -1), (4, 8, True, 2, 1), (6, 4, True, 2, -5), (9, 3, True, -2, -4), (10, 5, True, -5, -5), (10, 21, False, -5, -5), (11, 8, True, 1, 0), (6, 8, True, 1, -2), (9, 7, False, -1, -2), (6, 7, False, 2, -2), (3, 17, False, 0, -3), (11, 9, True, -3, -3), (5, 13, False, -4, -4), (6, 13, True, -4, -5), (9, 3, True, -2, -2), (6, 19, True, 0, -3), (7, 16, True, -3, -5), (9, 6, True, 4, -3), (8, 15, True, -3, -4), (4, 6, True, 3, -5), (7, 8, True, -5, -5), (4, 4, True, 3, -3), (2, 6, True, 2, -1), (6, 3, False, 2, 1), (4, 6, True, -5, -5), (2, 8, True, 4, 1), (5, 3, False, -3, -4), (4, 20, True, 5, -1), (5, 3, True, -4, -4), (6, 20, False, 2, -3), (10, 13, False, 3, 2), (8, 5, True, 2, -4), (2, 3, False, 3, -2), (5, 3, True, 1, 1), (3, 5, True, 5, -3), (7, 18, False, 3, -2), (9, 19, True, 2, -4), (9, 3, True, 4, 4), (4, 8, True, 4, 1), (4, 7, True, 1, -1), (3, 4, True, 4, -1), (4, 16, False, -1, -5), (8, 3, True, -1, -5), (9, 21, True, -5, -5), (6, 21, True, 1, -3), (5, 4, True, -2, -4), (8, 19, True, 4, -4), (4, 7, True, 1, 0), (7, 12, True, -4, -4), (4, 3, True, 4, -5), (4, 14, True, 4, -4), (6, 8, False, 1, -4), (7, 10, False, 2, -3), (6, 4, True, -3, -4), (9, 18, False, -2, -5), (11, 2, True, 5, -2), (5, 10, True, -3, -3), (10, 2, True, -3, -3), (2, 15, True, 4, -4), (2, 4, True, 2, 2), (7, 4, True, 4, -1), (10, 7, True, 4, 0), (6, 19, True, 3, 0), (6, 16, True, 5, 2), (6, 18, True, -1, -5), (11, 14, True, -3, -4), (9, 18, True, 5, 3), (6, 5, True, -2, -2), (10, 9, True, 4, 1), (4, 4, False, 1, -5), (8, 2, True, 3, -2), (9, 18, False, 3, -4), (11, 10, True, 5, -4), (8, 21, False, -3, -3), (10, 19, True, 5, 1), (11, 7, True, -5, -5), (11, 19, True, 1, -2), (2, 11, True, -2, -3), (6, 5, True, 2, -5), (10, 16, True, 4, -3), (4, 12, False, 5, -1), (8, 5, True, 5, -5), (3, 2, True, 2, -4)]

newerf = [(3, 19, True, -1, -2), (9, 13, True, -4, -5), (3, 8, True, 2, 1), (5, 13, False, -3, -3), (4, 17, False, -4, -4), (4, 21, True, 1, -1), (9, 13, True, 4, 0), (9, 17, True, -4, -5), (10, 10, True, 4, -4), (9, 7, True, -3, -4), (7, 17, False, -3, -3), (5, 15, False, 5, 3), (2, 21, True, -5, -5), (3, 13, True, 1, -4), (6, 5, True, 5, 3), (4, 21, True, -1, -1), (3, 6, False, 4, 0), (8, 9, True, -2, -4), (3, 16, True, 1, 1), (8, 4, False, 0, -4), (10, 9, True, -2, -5), (7, 5, True, 1, -1), (6, 11, True, 4, 4), (8, 5, False, 0, -1), (3, 15, True, -1, -1), (4, 9, True, 2, -1), (6, 21, False, -3, -4), (8, 14, True, 0, -4), (9, 5, True, 3, 2), (9, 16, False, 5, 2), (11, 19, True, -1, -5), (11, 12, True, 5, 2), (6, 14, True, -4, -5), (6, 13, True, -5, -5), (7, 3, True, -3, -3), (3, 11, True, -1, -3), (4, 13, True, 4, -3), (5, 3, True, 1, -4), (5, 4, True, -5, -5), (8, 3, True, -5, -5), (3, 21, False, 4, 1), (8, 2, True, 5, 4), (9, 21, True, 2, -2), (4, 15, False, -5, -5), (9, 19, True, 5, -2), (10, 13, True, -5, -5), (7, 15, True, 0, 0), (11, 3, True, 1, -5), (11, 19, False, 4, -3), (5, 9, True, -5, -5), (2, 13, True, -3, -3), (2, 14, True, -5, -5), (5, 16, True, 3, 0), (5, 10, False, -2, -2), (7, 7, True, 1, 1), (3, 11, True, 4, 2), (11, 4, True, -4, -5), (9, 7, True, 1, -3), (11, 12, True, 0, 0), (6, 10, True, -5, -5), (5, 19, True, 0, 0), (3, 16, True, -4, -5), (6, 10, True, -3, -5), (7, 6, False, -4, -5), (10, 2, False, 3, 0), (11, 3, True, 3, -5), (3, 19, False, 3, -1), (3, 12, True, -2, -5), (6, 18, True, -3, -4), (8, 21, True, 4, -2), (4, 2, True, -1, -1), (4, 3, True, 1, 1), (10, 20, False, -5, -5), (8, 3, True, -3, -4), (10, 8, True, -4, -5), (5, 3, True, 3, -2), (11, 17, True, -2, -2), (2, 15, True, 5, 5), (4, 14, False, -5, -5), (9, 12, True, -2, -5), (11, 7, True, 5, 5), (5, 2, True, -1, -2), (2, 16, True, 3, 2), (5, 13, False, -4, -4), (5, 8, True, 4, -4), (6, 4, True, 3, 1), (5, 10, True, -5, -5), (10, 17, True, -5, -5), (7, 16, True, 3, 2), (8, 3, True, -2, -3), (10, 11, True, 4, 3), (3, 3, False, -1, -2), (4, 3, True, 2, -3), (9, 17, True, -5, -5), (7, 19, True, 1, 0), (5, 11, True, 4, -1), (10, 17, True, 1, -3), (7, 2, False, -1, -2), (6, 11, True, -2, -5), (11, 9, True, 0, -4)]


print(getWinOdds(newerf))
while True:
    vals = evaluateGeneration(currentGeneration)
    vals.sort(key = lambda x: -x[1])
    print(vals)
    

    currentGeneration = [currentGeneration[i[0]] for i in vals]
    currentGeneration = currentGeneration[:100]
    for i in range(50):
        currentGeneration.append(generateRandomRule())
    
    

    
    
odds = getWinOdds("")
print(odds)

