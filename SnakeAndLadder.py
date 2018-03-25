#Hi there,enjoy playing the game and also check out my profile on github "https://github.com/BadsewalPawan"
#Author:Badsewal Pawan
#python v3.6.1 (Windows OS)
#THE ONLY SNAKE AND LADDER GAME EVER MADE ON PYTHON!

#importing modules
import os, random, time

#declaring variables
iWidth = 10*4 +1               
sDelimiter = "|"
iPadChar = 0
iNumbertoPrint = int
iMax = 10
sLine = str
iTemp = int
sLine_dash = '-'*iWidth
iP1=1
iCpu=1

#prints board
def show( iP1_pos , iCpu_pos ):
  print('\n')
  bisReverse = True
  for x in range (1,11)[::-1]:
    print (sLine_dash)
    sLine = ""
    iNumbertoPrint = x * 10
    for y in range (0,10):
        iTemp = iNumbertoPrint
        if iP1_pos == iNumbertoPrint and iCpu_pos == iNumbertoPrint:
           iNumbertoPrint = 'XO'
        elif iP1_pos == iNumbertoPrint:
           iNumbertoPrint = ' X'
        elif iCpu_pos == iNumbertoPrint:
           iNumbertoPrint = ' O'
        iPadChar = 3 - len(str(iNumbertoPrint))
        if bisReverse:
            sLine += sDelimiter + (" "*iPadChar) + str(iNumbertoPrint) 
        else:
            sLine = sDelimiter + (" "*iPadChar) + str(iNumbertoPrint)  + sLine 
        iNumbertoPrint = iTemp
        iNumbertoPrint -= 1          
    sLine += sDelimiter
    print (sLine)
    bisReverse = not (bisReverse)
  print (sLine_dash)
  print('\n')

#prints snake and ladder spots
def show_snake_ladder_list():
  print('Ladder at :  4 --> 14 ,  9 --> 31  ,  20 --> 38  ,  28 --> 84  ,  36 --> 44  ,  42 --> 63  ,  51 --> 67  ,  62 --> 98  ,  71 --> 90')
  print('\n')
  print('Snake  at : 99 --> 80 , 94 --> 26  ,  91 --> 73  ,  83 --> 57  ,  69 --> 32  ,  59 --> 1   ,  56 --> 48  ,  25 --> 3   ,  11 --> 8 ')
  print('\n')

#checks if player spot is equal to snake or ladder spot
def checking_for_snake_ladder(n):   
 ladder = { 4:14 , 9:31 , 20:38 , 28:84 , 36:44 , 42:63 , 51:67 , 62:98 , 71:90 }

 snake = { 99:80 , 94:26 , 91:73 , 83:57 , 69:32 , 59:1 , 56:48 , 25:3 , 11:8 }

 if ( n == 4 ) or ( n == 9 ) or ( n == 20 ) or ( n == 28 ) or ( n == 36 ) or ( n == 42 ) or ( n == 51 ) or ( n == 62 ) or ( n == 71 ) or ( n == 9 ):   
   #if ladder[n]:
     print('it\'s a ladder,climb up!')
     n=ladder[n]
     return n 
 elif ( n == 99 ) or ( n == 94 ) or ( n == 91 ) or ( n == 83 ) or ( n == 69 ) or ( n == 59 ) or ( n == 56 ) or ( n == 25 ):  
     print('Szzz snake bites,go down!')
     n=snake[n]
     return n 

 else:
     return n  

#calling func to display snake ladder board (P1 and P2 at spot 0) and spot list
show_snake_ladder_list()
show(iP1 , iCpu)

#game begins
while True:
  #player's turn
  while True:
    print('Your turn')
    print('\n')
    input('Press "Enter" key to roll the die')
    os.system('cls')
    show_snake_ladder_list()
    z = random.randint(1,6)
    print('You got {}'.format(z))
    print('\n')
    if iP1+z<101:
      if z<6:
        iP1+=z
        iP1=checking_for_snake_ladder(iP1)
        print('Your new position is {}'.format(iP1))
        show(iP1 , iCpu)
        break
      else:
        iP1+=z
        iP1=checking_for_snake_ladder(iP1)
        print('Your new position is {}'.format(iP1)) 
        show(iP1 , iCpu)
        print('Die rolled 6,get one more chance')
        time.sleep(3)
    else:
      print('The sum is out of range!')
      print('\n')
      z+=iP1
      print('Sum is {}'.format(z))
      print("Player position is {}".format(iP1))
      show(iP1 , iCpu)
      break
  if iP1 == 100:
    #if player position is 100 (player won),declare winner and end the game
    break
  #CPU's turn
  while True: 
    print('\n')
    print('CPU turn')
    time.sleep(3)
    os.system('cls')
    show_snake_ladder_list()
    z = random.randint(1,6)
    print('CPU got {}'.format(z))
    print('\n')
    if iCpu+z<101:
      if z<6:
        iCpu+=z
        iCpu=checking_for_snake_ladder(iCpu)
        print('CPU position is {}'.format(iCpu))
        show(iP1 , iCpu)
        break
      else:
        iCpu+=z
        iCpu=checking_for_snake_ladder(iCpu)
        print('CPU new position is {}'.format(iCpu))      
        show(iP1 , iCpu)
        print('Die rolled 6,get one more chance')
        time.sleep(3)
    else:
      print('The sum is out of range!')
      print('\n')
      z+=iCpu
      print('Sum is {}'.format(z))
      print("CPU position is {}".format(iCpu))
      show(iP1 , iCpu)
      break
  if iCpu == 100:
    #if CPU position is 100 (CPU won),declare winner and end the game
    break

print('\n')

#Declaring respective winner
if iP1 == 100:
   print('~~You win~~')

else:
   print('~~CPU wins~~')


#Dealy of 5 sec before closing terminal console for player to analyse the winner is declared and game is over
time.sleep(5)            
#Game ends!

