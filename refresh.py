from kivy.lang.builder import Builder
import pyautogui,sys,time
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window

Window.size=(100,100)


class MainApp(MDApp):
	def build(self):
		return Builder.load_file("refresher.kv")

	def close(self):
		App.get_running_app().stop()
		Window.close()

	def refresh(self):
		pyautogui.click(x=1919,y=1042)
		pyautogui.click()
		pyautogui.click(x=631,y=388,button='right')
		pyautogui.press('down')
		pyautogui.press('down')
		pyautogui.press('down')
		pyautogui.press('enter')
	def stop(self):
		time.sleep(0.5)



MainApp().run()