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

for j in range(1):
    counts = [0] * 11
    totals = [0] * 11
    total = 100000
    for i in range(total):
        deck = pydealer.Deck()
        
        deck.decks_used = 2
        deck.shuffle()
        hand = "".join([i.value[0] for i in deck.deal(2)])
        init = value(hand[0])
        while value(hand) < 17:
            hand += deck.deal(1)[0].value[0]
        if value(hand) > 21:
            counts[init] += 1
        totals[init] +=1

        
    print(sum(counts) / total)
    counts[10] = counts[10] / 4
    print(counts)
    print(totals)
    print([counts[i] / totals[i] for i in range(11) if totals[i] != 0])
    
