# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup as BS 
import requests 
import sys 


class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		# setting title 
		self.setWindowTitle("Python life ") 

		# setting geometry 
		self.setGeometry(100, 100, 400, 500) 

		# calling method 
		self.UiComponents() 

		# showing all the widgets 
		self.show() 

	# method for widgets 
	def UiComponents(self): 

		# countries list // user can add other countries as well 
		self.country = ["india", "us", "spain", "china", "russia", 
							"pakistan", "nepal", "italy", "spain", 
												"uk", "brazil"] 

		# creating a combo box widget 
		self.combo_box = QComboBox(self) 

		# setting geometry to combo box 
		self.combo_box.setGeometry(100, 50, 200, 40) 

		# setting font 
		self.combo_box.setFont(QFont('Times', 10)) 

		# adding items to combo box 
		for i in self.country: 
			i = i.upper() 
			self.combo_box.addItem(i) 

		# adding action to the combo box 
		self.combo_box.activated.connect(self.get_cases) 

		# creating label to show the total cases 
		self.label_total = QLabel("Total Cases ", self) 

		# setting geometry 
		self.label_total.setGeometry(100, 300, 200, 40) 

		# setting alignment to the text 
		self.label_total.setAlignment(Qt.AlignCenter) 

		# adding border to the label 
		self.label_total.setStyleSheet("border : 2px solid black;") 

		# creating label to show the recovered cases 
		self.label_reco = QLabel("Recovered Cases ", self) 

		# setting geometry 
		self.label_reco.setGeometry(100, 350, 200, 40) 

		# setting alignment to the text 
		self.label_reco.setAlignment(Qt.AlignCenter) 

		# adding border 
		self.label_reco.setStyleSheet("border : 2px solid black;") 

		# creating label to show death cases 
		self.label_death = QLabel("Total Deaths ", self) 

		# setting geometry 
		self.label_death.setGeometry(100, 400, 200, 40) 

		# setting alignment to the text 
		self.label_death.setAlignment(Qt.AlignCenter) 

		# adding border to the label 
		self.label_death.setStyleSheet("border : 2px solid black;") 


	# method called by push 
	def get_cases(self): 

		# getting country name 
		index = self.combo_box.currentIndex() 
		country_name = self.country[index] 


		# creating url using country name 
		url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

		# getting the request from url 
		data = requests.get(url) 

		# converting the text 
		soup = BS(data.text, 'html.parser') 

		# finding meta info for cases 
		cases = soup.find_all("div", class_="maincounter-number") 

		# getting total cases number 
		total = cases[0].text 

		# filtering it 
		total = total[1: len(total) - 2] 

		# getting recovered cases number 
		recovered = cases[2].text 

		# filtering it 
		recovered = recovered[1: len(recovered) - 1] 

		# getting death cases number 
		deaths = cases[1].text 

		# filtering it 
		deaths = deaths[1: len(deaths) - 1] 

		# show data through labels 
		self.label_total.setText("Total Cases : " + total) 
		self.label_reco.setText("Recovered Cases : " + recovered) 
		self.label_death.setText("Total Deaths : " + deaths) 


# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 

window.show() 

# start the app 
sys.exit(App.exec()) 
