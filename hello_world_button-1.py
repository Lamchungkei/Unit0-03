# Created by: Kay Lin
# Created on: 14-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program displays hello_world_button    but in GUI

import ui

def hello_world_touch_up_inside(sender):
	#print('Hello, World!')
	view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')
