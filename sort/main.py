import os
import zipfile##Импорт архивации
from kivy.app import App##Импорт киви
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config##Импорт изменения окошка
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','480');##Изминения ширина
Config.set('graphics','height','240');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		bl = BoxLayout(orientation= 'vertical')
		self.lbl = Label(text = "")
		bl.add_widget(self.lbl)
		
		bl.add_widget(Button(text = "Создать Папки", on_press = self.btn_press))
		al.add_widget(bl)
		bl.add_widget(Button(text = "Отсортировать картинки", on_press = self.btn_press2))
		al.add_widget(bl)
		bl.add_widget(Button(text = "Отсортировать скрипты", on_press = self.btn_press3))
		al.add_widget(bl)
		return al
	
	def btn_press(self,instance):
		path = 'C:/Users/Гусев/Desktop'
		projectname = 'sort'
		folders = \
		['png',
		'jpg',
		'py']

		fullPath = os.path.join(path , projectname)
		if not os.path.exists(fullPath):
			os.mkdir(fullPath)
		for f in folders:
			folder = os.path.join(fullPath, f)
			if not os.path.exists(folder):
				os.mkdir(folder)
		self.lbl.text = ('Папки созданы :3')

	def btn_press2(self,instance):
		pass
	def btn_press3(self, instance):
		pass


if __name__ == "__main__":##
	 BoxApp().run()##