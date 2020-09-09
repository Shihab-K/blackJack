from tkinter import *
from PIL import ImageTk, Image
import random


class CardLabel(Label):
	def __init__(self, parent):
		Label.__init__(self, parent, image = CardLabel.back_image)


	suits = ('H', 'C', 'D', 'S')
	ranks = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
			'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'King': 10,
			'Queen': 10, 'Jack': 10, 'Joker': 0}
	

	directory = []
	front_images = []
	true_directory = []

	@staticmethod
	def load_images():
		root = Toplevel()
		root.withdraw()

		for i in range(52):
			CardLabel.directory.append('jpeg/{}{}.gif'.format(random.choice(list(CardLabel.ranks.keys())), 
												    	      random.choice(CardLabel.suits)))

		global front_images
		front_images = []
		true_directory = []

		for i in range(25):
			true_directory.append(random.choice(CardLabel.directory))

		CardLabel.front_image1 = ImageTk.PhotoImage(file = true_directory[0])
		front_images.append((CardLabel.front_image1, true_directory[0]))

		CardLabel.front_image2 = ImageTk.PhotoImage(file = true_directory[1])
		front_images.append((CardLabel.front_image2, true_directory[1]))

		CardLabel.front_image3 = ImageTk.PhotoImage(file = true_directory[2])
		front_images.append((CardLabel.front_image3, true_directory[2]))

		CardLabel.front_image4 = ImageTk.PhotoImage(file = true_directory[3])
		front_images.append((CardLabel.front_image4, true_directory[3]))

		CardLabel.front_image5 = ImageTk.PhotoImage(file = true_directory[4])
		front_images.append((CardLabel.front_image5, true_directory[4]))

		CardLabel.front_image6 = ImageTk.PhotoImage(file = true_directory[5])
		front_images.append((CardLabel.front_image6, true_directory[5]))

		CardLabel.front_image7 = ImageTk.PhotoImage(file = true_directory[6])
		front_images.append((CardLabel.front_image7, true_directory[6]))

		CardLabel.front_image8 = ImageTk.PhotoImage(file = true_directory[7])
		front_images.append((CardLabel.front_image8, true_directory[7]))

		CardLabel.front_image9 = ImageTk.PhotoImage(file = true_directory[8])
		front_images.append((CardLabel.front_image9, true_directory[8]))

		CardLabel.front_image10 = ImageTk.PhotoImage(file = true_directory[9])
		front_images.append((CardLabel.front_image10, true_directory[9]))

		CardLabel.front_image11 = ImageTk.PhotoImage(file = true_directory[10])
		front_images.append((CardLabel.front_image11, true_directory[10]))

		CardLabel.front_image12 = ImageTk.PhotoImage(file = true_directory[11])
		front_images.append((CardLabel.front_image12, true_directory[11]))

		CardLabel.front_image13 = ImageTk.PhotoImage(file = true_directory[12])
		front_images.append((CardLabel.front_image13, true_directory[12]))

		CardLabel.front_image14 = ImageTk.PhotoImage(file = true_directory[13])
		front_images.append((CardLabel.front_image14, true_directory[13]))

		CardLabel.front_image15 = ImageTk.PhotoImage(file = true_directory[14])
		front_images.append((CardLabel.front_image15, true_directory[14]))

		CardLabel.front_image16 = ImageTk.PhotoImage(file = true_directory[15])
		front_images.append((CardLabel.front_image16, true_directory[15]))

		CardLabel.front_image17 = ImageTk.PhotoImage(file = true_directory[16])
		front_images.append((CardLabel.front_image17, true_directory[16]))

		CardLabel.front_image18 = ImageTk.PhotoImage(file = true_directory[17])
		front_images.append((CardLabel.front_image18, true_directory[17]))

		CardLabel.front_image19 = ImageTk.PhotoImage(file = true_directory[18])
		front_images.append((CardLabel.front_image19, true_directory[18]))

		CardLabel.front_image20 = ImageTk.PhotoImage(file = true_directory[19])
		front_images.append((CardLabel.front_image20, true_directory[19]))

		CardLabel.front_image21 = ImageTk.PhotoImage(file = true_directory[20])
		front_images.append((CardLabel.front_image21, true_directory[20]))

		CardLabel.front_image22 = ImageTk.PhotoImage(file = true_directory[21])
		front_images.append((CardLabel.front_image22, true_directory[21]))

		CardLabel.front_image23 = ImageTk.PhotoImage(file = true_directory[22])
		front_images.append((CardLabel.front_image23, true_directory[22]))

		CardLabel.front_image24 = ImageTk.PhotoImage(file = true_directory[23])
		front_images.append((CardLabel.front_image24, true_directory[23]))

		CardLabel.front_image25 = ImageTk.PhotoImage(file = true_directory[24])
		front_images.append((CardLabel.front_image25, true_directory[24]))


		CardLabel.back_image = ImageTk.PhotoImage(file = 'jpeg/back-blue.gif')
		CardLabel.blank_image = ImageTk.PhotoImage(file = 'jpeg/blank.gif')
		

	def display(self, side = 'back', id = 0):
		self.img = random.choice(front_images)
		if side == 'back':
			self.configure(image = CardLabel.back_image)

		elif side == 'front':
			self.configure(image = self.img[0])

		else:
			self.configure(image = CardLabel.blank_image)



	def card_value(self):
		str = self.img[1]

		card_value = re.findall(r'(\w+)', str)[1]
		card_type = re.findall(r'(\w+)', str)[1]
		value = CardLabel.ranks.get(card_value[:-1])
		
		return value



