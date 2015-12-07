#!/usr/local/bin/python2.7
import sys, pygame, json, urllib2, math
from decimal import *
pygame.init()
size = width, height = 800, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size,0, 32)

bitcoin = pygame.image.load('images/bitcoin.png').convert()
bitcoin = pygame.transform.scale(bitcoin, (288,100))


litecoin = pygame.image.load('images/litecoin.png').convert()
litecoin = pygame.transform.scale(litecoin, (288,110 ))

dogecoin = pygame.image.load('images/dogecoin2.png').convert()
dogecoin = pygame.transform.scale(dogecoin, (288,110 ))

back = pygame.image.load('images/back.png').convert()
back = pygame.transform.scale(back, (100,100 ))

buynow = pygame.image.load('images/buynow.gif').convert()
buynow = pygame.transform.scale(buynow, (300,50 ))

balance=float(0);
font = pygame.font.Font("fonts/lucida.ttf", 20)



def main(balance):
    print balance

    while 1:
        screen.fill(black)
        current_balance = font.render("Current Balance: ", 1, (255, 255, 255))
        balancetxt = font.render("$"+str(balance), 1, (255, 255, 255))
        msg = font.render("Please Select The Currency You Want To Purchase ", 1, (255, 255, 255))
        msgpay = font.render("Insert USD ", 1, (255, 255, 255))
        bitcoinbtn = screen.blit(bitcoin,(256,140))
        litecoinbtn = screen.blit(litecoin,(256,250))
        dogecoinbtn = screen.blit(dogecoin,(256,370))
        screen.blit(msg,(100,70))
        screen.blit(current_balance,(0,0))
        screen.blit(msgpay,(675,0))
        screen.blit(balancetxt,(210,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if bitcoinbtn.collidepoint(x,y):
                    buyCoins("bitcoin",balance)
                if litecoinbtn.collidepoint(x,y):
                    buyCoins("litecoin",balance)
                    print "Litecoin!" 
                if dogecoinbtn.collidepoint(x,y):
                    print "dogecoin!" 
                    buyCoins("dogecoin",balance)
     
def buyCoins(type,balance):
    typeCapital = type.capitalize()
    screen.fill(black)
    font = pygame.font.Font("fonts/lucida.ttf", 20)
    current_balance = font.render("Current Balance: ", 1, (255, 255, 255))
    balancetxt = font.render("$"+str(balance), 1, (255, 255, 255))
    msg = font.render("You Have Opted To Buy " + typeCapital, 1, (255, 255, 255))
    msgpay = font.render("Insert USD ", 1, (255, 255, 255))
    screen.blit(msg,(240,70))
    screen.blit(current_balance,(0,0))
    screen.blit(msgpay,(675,0))
    bt = screen.blit(balancetxt,(210,0))
    backbtn = screen.blit(back,(50,450))
    url = ""
    if (type == "litecoin"):
        url="http://coinmarketcap-nexuist.rhcloud.com/api/ltc"   
    if (type == "bitcoin"):
        url="http://coinmarketcap-nexuist.rhcloud.com/api/btc"   
    if (type == "dogecoin"):
        url="http://coinmarketcap-nexuist.rhcloud.com/api/doge"   
    
    json_output = urllib2.urlopen(url).read()

    parsed_json = json.loads(json_output)
    usd = parsed_json['price']['usd']
    orig_usd = usd
    print orig_usd
    usd = Decimal(usd)
    usd = (float(usd) * float(.01))    
    
    amount_per = float(orig_usd) - float(usd)

    #print amount_per

    
    
    while 1:
        screen.fill(pygame.Color("black"))
        current_balance = font.render("Current Balance: ", 1, (255, 255, 255))
        balancetxt = font.render("$"+str(balance), 1, (255, 255, 255))
        msg = font.render("You Have Opted To Buy " + typeCapital, 1, (255, 255, 255))
        msgpay = font.render("Insert USD ", 1, (255, 255, 255))
        screen.blit(msg,(240,70))
        screen.blit(current_balance,(0,0))
        screen.blit(msgpay,(675,0))
        bt = screen.blit(balancetxt,(210,0))
        backbtn = screen.blit(back,(50,450))
        currenttxt = font.render("The Current Rate is $" + str(amount_per) + "/USD per "+ typeCapital, 1, (255, 255, 255))
        screen.blit(currenttxt,(100,200))
        buybtn = screen.blit(buynow,(250,300))
        total = float(balance)/float(amount_per)
        
        totaltxt = font.render("At Your Current Deposit you could buy " + str(total) + " "+ typeCapital, 1, (255, 255, 255))
        screen.blit(totaltxt,(10,250))
        #this is test code


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if backbtn.collidepoint(x,y):
                    main(balance)
                if bt.collidepoint(x,y): #this is test code to emulate a deposit
                    balance = balance + 20
                    print str(balance)
                    balancetxt = font.render("$"+str(balance), 1, (255, 255, 255))
                    bt = screen.blit(balancetxt,(210,0))
                if buybtn.collidepoint(x,y):
                    print "Buying!"
        
        

        pygame.display.flip()

if __name__ == '__main__': main(balance)

