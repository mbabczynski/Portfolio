
from random import choice
import art
import time

def comp(x):
    if x < 17:
        computer_cards.append(choice(cards))
        x = sum(computer_cards)
    if x > 21 and 11 in computer_cards:
        x -=10
    return x

def player(y):
    if y > 21 and 11 in player_cards:
        y -=10
    return y

def winner(player,comp):
    print('\n\nCompyter Cards: ', computer_cards , '\n')
    time.sleep(2)
    print('Your score: ', player, 'Computer score: ', comp, end='   ')
    if (player == 21 and (len(player_cards) == 2) and ((comp != 21) or ((len(computer_cards) != 2)))) or (player <= 21 and comp > 21) or (player < 21 and comp < 21 and player > comp):
        print('Congratulations! You won!!!')
    if comp == player:
        print('Draw, try again...')
    else:
        print('Sorry! You lose!!!')
    time.sleep(2)
    print("\n\n loading.", end='')
    for i in range(8):
        print('.', end='')
        time.sleep(1)

def deck():
    print('\n'+"Computer's first card is " , computer_cards[0] )
    print('\n'+"Your cards:  " , player_cards , "  Sum of your cards is " , sum(player_cards) )

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True
while game == True:
    
    computer_cards = [choice(cards), choice(cards)]
    player_cards = [choice(cards), choice(cards)]
        
    print('\n\n')
    print(art.logo)
    
    while True:
        play = input("Do you want to play BlackJack ?? Enter Y or N :   ").lower()
        if play not in ['y','n']:
            print('Bad letter, try again...')
            time.sleep(2)
            continue
        if play == 'y':
            game = True
        else:
            game = False
        break
    deck()

    while True:
        take_card = input('\n'+"Do you need another card ??, Enter Y or N   " ).lower()
        if take_card not in ['y','n']:
            print('Bad letter, try again...')
            time.sleep(2)
            continue
        if take_card == 'y':
            player_cards.append(choice(cards))
        break
      
    deck()

    winner(player(sum(player_cards)),comp(sum(computer_cards)))

print('GAME END !!!')

