#!/usr/local/bin/python2.7
import sys, pygame, json, urllib2, math, locale
from decimal import *
pygame.init()
locale.setlocale( locale.LC_ALL, '' )
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

ok = pygame.image.load('images/ok.png').convert()
ok = pygame.transform.scale(ok, (100,50 ))

cancel = pygame.image.load('images/cancel.png').convert()
cancel = pygame.transform.scale(cancel, (100,50 ))

balance=float(0);
font = pygame.font.Font("fonts/lucida.ttf", 20)



def main(balance):
    while 1:
        screen.fill(black)
        current_balance = font.render("Current Balance: ", 1, (255, 255, 255))
        balancetxt = font.render(locale.currency(balance, grouping=True), 1, (255, 255, 255))
        msg = font.render("Please Select The Currency You Want To Purchase ", 1, (255, 255, 255))
        if (balance > 0):
            msgpay = font.render("", 1, (255, 255, 255))
        else:
            msgpay = font.render("Insert USD", 1, (255, 255, 255))

        textpos = bitcoin.get_rect()
        textpos.centerx = screen.get_rect().centerx

        bitcoinbtn = screen.blit(bitcoin,(textpos[0],140))
        litecoinbtn = screen.blit(litecoin,(textpos[0],250))
        dogecoinbtn = screen.blit(dogecoin,(textpos[0],370))

        textpos = msg.get_rect()
        textpos.centerx = screen.get_rect().centerx


        screen.blit(msg,(textpos[0],70))
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

def buy(type,balance,qr):
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
    usd = Decimal(usd)
    usd = (float(usd) * float(.01))        
    amount_per = float(orig_usd) - float(usd)
    total = float(balance)/float(amount_per)
    total = total - 0.00001000
    getcontext().rounding = ROUND_DOWN
    print total
    if (total < 0):
        total = 0
    else:
        total = math.floor(total*100000000)/100000000
        print total

    while 1:
        screen.fill(black)
        print "Buying: " + type + " With " + str(balance) + " to " + qr + " " + str(total)


def buyCoins(type,balance):
    typeCapital = type.capitalize()
    qr=""
    screen.fill(black)
    font = pygame.font.Font("fonts/lucida.ttf", 20)
    current_balance = font.render("Current Balance: ", 1, (255, 255, 255))
    balancetxt = font.render(locale.currency(balance, grouping=True), 1, (255, 255, 255))
    msg = font.render("You Have Opted To Buy " + typeCapital, 1, (255, 255, 255))
    buying=0
    if (balance > 0):
        msgpay = font.render("", 1, (255, 255, 255))
    else:
        msgpay = font.render("Insert USD", 1, (255, 255, 255))

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
    usd = Decimal(usd)
    usd = (float(usd) * float(.01))        
    amount_per = float(orig_usd) - float(usd)
    scanned=0

    while 1:
        screen.fill(pygame.Color("black"))
        current_balance = font.render("Current Balance: ", 1, (255, 255, 255))
        balancetxt = font.render(locale.currency(balance,grouping=True), 1, (255, 255, 255))
        msg = font.render("You Have Opted To Buy " + typeCapital, 1, (255, 255, 255))
        if (balance > 0):
            msgpay = font.render("", 1, (255, 255, 255))
        else:
            msgpay = font.render("Insert USD", 1, (255, 255, 255))


        textpos = msg.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(msg,(textpos[0],70))

        screen.blit(current_balance,(0,0))
        screen.blit(msgpay,(675,0))
        bt = screen.blit(balancetxt,(210,0))
        backbtn = screen.blit(back,(50,450))
        currenttxt = font.render("The Current Rate is $" + str(amount_per) + "/USD per "+ typeCapital, 1, (255, 255, 255))
        textpos = currenttxt.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(currenttxt,(textpos[0],200))

        buybtn = screen.blit(buynow,(250,300))
        total = float(balance)/float(amount_per)
        total = total - 0.00001000
        getcontext().rounding = ROUND_DOWN
        print total
        if (total < 0):
            total = 0
        else:
            total = math.floor(total*100000000)/100000000
            print total

        totaltxt = font.render("At Your Current Deposit you could buy " + str(total) + " "+ typeCapital, 1, (255, 255, 255))
        textpos = totaltxt.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(totaltxt,(textpos[0],250))
        
        if buying == 1 and balance <= 0:
            surface = pygame.Surface((400,200))
            surface.fill((100,149,237))
            surfacecenter = surface.get_rect()
            surfacecenter.centerx = screen.get_rect().centerx
            errortxt = font.render("You Must Insert Some Money", 1, (255, 255, 255))
            textpos = errortxt.get_rect()
            textpos.centerx = surface.get_rect().centerx
            surface.blit(errortxt,(textpos[0],50))
            pygame.draw.rect(surface,(255,255,255),(0,0,400,200),5)
            screen.blit(surface,(surfacecenter[0],200))
            okbtn = screen.blit(ok,(350,300))
        elif buying == 1 and balance > 0 and scanned == 0:
            surface = pygame.Surface((400,200))
            surface.fill((100,149,237))
            surfacecenter = surface.get_rect()
            surfacecenter.centerx = screen.get_rect().centerx
            errortxt = font.render("Insert Your QR Code", 1, (255, 255, 255))
            textpos = errortxt.get_rect()
            textpos.centerx = surface.get_rect().centerx
            surface.blit(errortxt,(textpos[0],50))
            pygame.draw.rect(surface,(255,255,255),(0,0,400,200),5)
            screen.blit(surface,(surfacecenter[0],200))
            cancelbtn = screen.blit(cancel,(350,300))
            scanned=1
        elif buying == 1 and balance > 0 and scanned == 1:
            #18TspoUt9wfW9ESPivTZCeY4imvVNCbaiJ
            qr="18TspoUt9wfW9ESPivTZCeY4imvVNCbaiJ"
            surface = pygame.Surface((500,200))
            surface.fill((100,149,237))
            surfacecenter = surface.get_rect()
            surfacecenter.centerx = screen.get_rect().centerx
            msg1 = font.render("Payment Will Be Sent To", 1, (255, 255, 255))
            msg2 = font.render(qr, 1, (255, 255, 255))
            msg3 = font.render("Is This Correct?", 1, (255, 255, 255))
            textpos = msg1.get_rect()
            textpos.centerx = surface.get_rect().centerx
            surface.blit(msg1,(10,50))
            surface.blit(msg2,(10,80))
            surface.blit(msg3,(10,110))
            pygame.draw.rect(surface,(255,255,255),(0,0,500,200),5)
            screen.blit(surface,(surfacecenter[0],200))
            cancelbtn = screen.blit(cancel,(400,340))
            okbtn = screen.blit(ok,(250,340))

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
                    balancetxt = font.render(locale.currency(balance,grouping=True), 1, (255, 255, 255))
                    bt = screen.blit(balancetxt,(210,0))
                if buybtn.collidepoint(x,y):
                    if buying != 1:
                        print "Buying!"
                        buying = 1
                try:
                    okbtn
                except NameError:
                    print "okbtn not defined"
                else:
                    print event.pos
                    print okbtn
                    if okbtn.collidepoint(x,y):
                        if buying == 1 and balance > 0 and scanned == 1:
                            print "BUYING NOW!!!!"
                            buying = 0
                            del okbtn
                            del cancelbtn
                            buy(type,balance,qr)
                        else:
                            print "OK!"
                            buying = 0
                            del okbtn
                try:
                    cancelbtn
                except NameError:
                    print "cancelbtn not defined"
                else:
                    if cancelbtn.collidepoint(x,y):
                        print "Cancel!"
                        buying = 0
                        del cancelbtn
        


        pygame.display.flip()

if __name__ == '__main__': main(balance)

