import socket
import time



def value(hand):
    total = 0
    for c in hand:
        if c in "TJQK":
            total+=10
        elif c == "A":
            total += 11
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
    #soft count
    if ("A" in playerHand) and total < 11:
        #deviations
        if count >= 3 and total == 9 and dealer == 4:
            return True
        if count >= 1 and total == 9 and dealer == 5:
            return True
        if count < 0 and total == 9 and dealer == 6:
            return True
        if(count >=1 and total == 7 and dealer == 2):
            return True
        #/deviations

        
        if(total > 8):
            return False
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




def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("blackjack.misc.ctf.umasscybersec.org", 2207))

    intro = s.recv(1024)
    #print(intro.decode())
    s.send(b"ready\n")
    time.sleep(.1)
    nextCards = s.recv(50240).decode("utf-8")

    result = nextCards
    for i in range(1002):
        if(i % 250 == 0):
            print(i)
        
        time.sleep(.04)
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

        playerHand = hand


        while hit(playerHand, nextHands):
            
            s.send(b"hit\n")
            time.sleep(.04)
            f = s.recv(50240)
            ins = f.decode("utf-8")
            result += ins
            #print(ins)
            
            if "Dealer's hand" in ins:
                nextCards = ins
                break

            for h in ins:
                line = decodeLine(h)
                if line != "":
                    playerHand = line

            
        else:
            
            s.send(b"stand\n")
            time.sleep(.1)
            ins = s.recv(50240).decode("utf-8")
            result += ins
            nextCards = ins

    end = result.rindex("win percentage")
    percent = float(result[end + 18: result.index("%",end)])
    if(percent > 51):
        print("!!!!!!!!!!!!!")
    print(result[end -500: end + 500])
    return percent

while True:
    run()
    

