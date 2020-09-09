from tkinter import *
from tkinter import simpledialog
from playsound import playsound
from PIL import ImageTk, Image
import glob
import os
from Cards import *
import sys


root = Tk()
root.title('Cards')
root.geometry('800x600')
root.configure(bg='#007d00')
root.iconbitmap('extras/poker-cards.ico')

player_count = 2
dealer_count = 2
pcol = 2
dcol = 2

dealer_board = Frame(root, bg = '#007d00', width = 900, height = 600)
result_frame = Frame(root, bg = '#007d00')
player_board = Frame(root, bg = '#007d00', width = 900, height = 600)
menu = LabelFrame(root, text= 'Menu', bg = 'white', padx = 250, pady = 5)

dealer_board.grid(row = 0, columnspan = 10, sticky = N)
result_frame.grid(row = 1, columnspan = 10)
player_board.grid(row = 2, columnspan = 10, sticky = S)
menu.grid(row = 10, columnspan = 10, sticky = S)

CardLabel.load_images()
player_cards = []
dealer_cards = []

player_count = 2
dealer_count = 2
pcol = 2
dcol = 2


for i in range(6):
	player_cards.append(CardLabel(player_board))
	dealer_cards.append(CardLabel(dealer_board))


l0 = dealer_cards[0]
l0.display(side = 'front')
l0.grid(row = 0, column = 0)

l1 = dealer_cards[1]
l1.grid(row = 0, column = 1)

l2 = player_cards[0]
l2.display(side = 'front')
l2.grid(row = 2, column = 0)

l3 = player_cards[1]
l3.display(side = 'front')
l3.grid(row = 2, column = 1)


player_total = CardLabel.card_value(l2) + CardLabel.card_value(l3)
dealer_total = CardLabel.card_value(l0)

player_total_text = Label(player_board, text = 'Your Total: {}'.format(player_total))
player_total_text.config(font = ("Arial", 18), bg = '#007d00', fg = 'black')

dealer_total_text = Label(dealer_board, text = 'Dealers Total: ?')
dealer_total_text.config(font = ("Arial", 18), bg = '#007d00', fg = 'black')

player_total_text.grid(row = 0, column = pcol+1)
dealer_total_text.grid(row = 2, column = dcol+1)

def newGame():
	os.execl(sys.executable, sys.executable, * sys.argv)

def stay():
	global player_total
	global dealer_total

	if player_total == 21:
		results(result = 'won')

	stayButton.config(state = DISABLED)
	hitButton.config(state = DISABLED)

	l1.display(side = 'front')

	dealer_total += CardLabel.card_value(l1)
	dealer_total_text.config(text = 'Dealers total: {}'.format(dealer_total))


	hit(player = 'dealer')



def hit(player = 'player'):
	global player_count
	global dealer_count
	global pcol
	global dcol
	global player_total
	global dealer_total

	if player == 'player':
		player_cards[player_count].display(side = 'front')
		player_cards[player_count].grid(row = 2, column = pcol)

		player_total+= CardLabel.card_value(player_cards[player_count])
		player_count+= 1
		pcol+= 1

		player_total_text.config(text = 'Your Total: {}'.format(player_total))
		player_total_text.grid(column = pcol + 1)

		if player_total > 21:
			results()
			player_total_text.config(fg = 'red')

		if player_count >= 5 and player_total <= 21:
			results(result = 'won')

		if player_total == 21:
			results(result = 'won')
	else:
		while True:
			if dealer_total >= 22:
				results(result = 'won')
				dealer_total_text.config(fg = 'red')
				break

			elif dealer_total > player_total and dealer_total <= 21:
				results()
				break

			elif dealer_total == 21 and player_total < 21:
				results()
				break

			elif dealer_total == player_total and dealer_total >= 17:
				results(result = 'tie')
				break

			elif dealer_count >= 5 and dealer_total < 21:
				results()
				break

			else:
				dealer_cards[dealer_count].display(side = 'front')
				dealer_cards[dealer_count].grid(row = 0, column = dcol)

				dealer_total+= CardLabel.card_value(dealer_cards[dealer_count])
				dealer_count+= 1
				dcol+= 1

				dealer_total_text.config(text = 'Dealers Total: {}'.format(dealer_total))
				dealer_total_text.grid(column = dcol+ 1)


def results(result = 'lost'):
	if result == 'lost':
		stayButton.config(state = DISABLED)
		hitButton.config(state = DISABLED)

		defeat = Label(result_frame, bg = '#007d00',fg = '#fc5603', text = 'Better Luck Next Time!')
		defeat.config(font = ("Courier", 40))
		defeat.grid(row = 1)

		playsound('sounds/lost.wav', 0)

	elif result == 'won':
		stayButton.config(state = DISABLED)
		hitButton.config(state = DISABLED)

		victory = Label(result_frame, bg = '#007d00', fg = '#c38fff', text = 'You Win!')
		victory.config(font = ("Courier", 40))
		victory.grid(row = 1)

		playsound('sounds/victory.wav', 0)

	elif result == 'tie':
		stayButton.config(state = DISABLED)
		hitButton.config(state = DISABLED)

		tie = Label(result_frame, bg = '#007d00', fg = '#c38fff', text = "It's a tie!")
		tie.config(font = ("Courier", 40))
		tie.grid(row = 1)

		playsound('sounds/tie.mp3', 0)


hitButton = Button(menu, text = 'Hit Me!', command = lambda: hit())
stayButton = Button(menu, text = 'Stay', command = lambda: stay())
newGameButton = Button(menu, text = 'Start New Game', command = lambda: newGame())
quit = Button(menu, text = 'Quit', command = root.quit)

newGameButton.grid(row = 2, column = 0)
hitButton.grid(row = 2, column = 1)
stayButton.grid(row = 2, column = 2)
quit.grid(row = 2, column = 3)


for row in range(10):
	root.grid_rowconfigure(row, weight = 1)

	for col in range(10):
		root.grid_columnconfigure(col, weight = 1)

def main():
	root.mainloop()


if __name__ == '__main__':
	main()



