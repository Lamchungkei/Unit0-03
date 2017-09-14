# Created by: Kay Lin
# Created on: 14-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program displays address    but in GUI

import ui

def address_touch_up_inside(sender):
	#print ('Hello, World!')
	view['name_label'].text = ("Kay")
	view['city_label'].text = ("Ottawa")
	view['country_label'].text = ("Canada")

view = ui.load_view()
view.present('sheet')
