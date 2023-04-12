import socket
import time



def value(hand):
    total = 0
    for c in hand:
        if c in "TJQK":
            total+=10
        elif c == "A":
            total += 1
        else:
            total += int(c)
    return total

def decodeLine(h):
    temp = "".join([i for i in h if i in "123456789JQKA"])
            
    temp = temp.replace("1", "T")

    return temp

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

def hit(playerHand, otherHands):
    
    count = getTrueCount(playerHand, otherHands)
    dealer = otherHands[0]
    dealer = value(dealer)
    if dealer == 1:
        dealer = 11
        
    total = value(playerHand)
    if "A" in playerHand and 20<=total + 10<=21:
        return False
    
    if total < 12:
        return True
    if total > 17:
        return False
    
    if dealer < 8:
        return False

    if count >= 1 and (dealer == 9 or dealer == 10):
        return False
    
    if dealer == 9 or dealer == 10:
        return total == 12

    if count >= 1 and total >= 16:
        return False
    if count >= 2:
        return False
    
    return total < 17
    

    #soft count
    if ("A" in playerHand) and total < 11:

        
        
        if total == 8 and dealer < 9:
            return False
        return True

    #hard count
    #deviations
    if total == 16:
        if dealer == 9 and count >= 4:
            return False
        if dealer == 10 and count >0:
            return False
        if dealer == 11 and count >= 3:
            return False
    if total == 15:
        if dealer == 10 and count >=4:
            return False
        if dealer == 11 and count >= 5:
            return False

    if total == 13:
        if dealer == 2 and count <= -1:
            return False

    if total == 12:
        if dealer == 2 and count >= 3:
            return True
        if dealer == 3 and count >=2:
            return True
        if dealer == 4 and count <0:
            return False
    
    if total == 10:
        if dealer == 10 and count >=4:
            return False
        if dealer == 11 and count >= 3:
            return False

    if total == 9:
        if dealer == 2 and count >=1:
            return False
        if dealer == 7 and count >= 3:
            return False
    if total == 8:
        if dealer == 6 and count >= 2:
            return False
    
    if value(playerHand) >= 17:
        return False
    
    if (dealer < 7) and value(playerHand) > 12:
        return False

    if total == 12 and 4<=dealer <=6:
        return False
    
    return True



def playRound(s, nextCards):
    nextCards = nextCards[nextCards.rindex("Dealer's hand"):]
        
    #print(nextCards)
    nextCards = nextCards.split("\n")
    hands = []
    for i in nextCards:
        if i!="" and (":" in i or i[0] == "│"):
            hands.append(i)

    nextHands = []
    hand = []
    for h in hands[1:]:
        if ":" in h:
            nextHands.append(hand)
            hand = []
            continue
        
        temp = decodeLine(h)
        if temp != "":
            hand = temp
    failed = False
    if len(nextHands) != 5:
        print(nextHands)
        print(nextCards)
        failed = True
    
    playerHand = hand

    #print(playerHand)
    while not failed and hit(playerHand, nextHands):
        
        s.send(b"hit\n")
        time.sleep(.04)
        f = s.recv(50240)
        try:
            ins = f.decode("utf-8")
        except:
            print("failed", f)
        #print(ins)
        
        if "Dealer's hand" in ins:
            nextCards = ins
            break

        for h in ins.split("\n"):
            line = decodeLine(h)
            if line != "":
                #print(playerHand, line, h)
                playerHand = line
        
    else:
        
        s.send(b"stand\n")
        time.sleep(.04)
        ins = s.recv(50240).decode("utf-8")
        nextCards = ins
    return nextCards

            
def run(s, n, nextCards):
    print("messing with ace ordered percentile converted gto counting")
    
    percent = 0
    result = nextCards
    for i in range(n):
        if(i % 250 == 0):
            print(i)
        nextCards = playRound(s, nextCards)
        result += nextCards
        
    percent = 0

    a = 0
    while True:
        end = result.rindex("win percentage")
        percent = float(result[end + 18: result.index("%",end)])
        if(True or percent > 52):
            print("!!!!!!!!!!!!!")
            print(result[end -500: end + 500])
            print()
            print(result)
            nextCards = playRound(s, nextCards)
            result += nextCards
            end = result.rindex("win percentage")
            percent = float(result[end + 18: result.index("%",end)])
            print("!!!!!!!!!!!!!")
            print(result[end -500: end + 500])
            print()
            print(result)
            
            quit()
        #if a % 100 == 0:
            #print(a)
            #print(result[end -500: end + 500])
        nextCards = playRound(s, nextCards)
        result += nextCards
        a+=1
        
    return (s, result, nextCards)


while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(("blackjack.misc.ctf.umasscybersec.org", 2207))

        intro = s.recv(1024)
        #print(intro.decode())
        s.send(b"ready\n")
        time.sleep(.1)
        nextCards = s.recv(50240).decode("utf-8")

        s = run(s, 10000, nextCards)
    except:
        pass
    

