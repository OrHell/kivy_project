import os
import zipfile
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics','resizeble','0');
Config.set('graphics','width','640');
Config.set('graphics','height','480');

class BoxApp(App):
	def build(self):
		self.formula = "0"
		al = AnchorLayout()
		bl = BoxLayout(orientation= 'vertical',size_hint =[.4,.4])
		bl.add_widget(TextInput(text = "C:\\Users\\Mentall\\Desktop\\Project\\Arch\\kim.jpg", font_size = "12"))
		bl.add_widget(Button(text="Save", on_press = self.btn_pressss,font_size = "8"))
		bl.add_widget(Button(text = "Zip", on_press = self.btn_press,font_size = "8"))
		bl.add_widget(Button(text = "AllZip",on_press = self.btn_presss,font_size = "8"))
		al.add_widget(bl)
		return al
		



	def btn_pressss(self,instance):
		instance = b = print ('Pisa is jopi')


	def btn_press(self, instance):
		instance = jungle_zip = zipfile.ZipFile('yes.zip', 'w')
		jungle_zip.write('C:\\Users\\Mentall\\Desktop\\Project\\Arch\\kim.jpg', compress_type=zipfile.ZIP_DEFLATED)
		jungle_zip.close()##Конец
		
	
	
		
	
	def btn_presss(self, instance)
		instance = fantasy_zip = zipfile.ZipFile('yes_two.zip', 'w')
		for folder, subfolders, files in os.walk('C:\\Users\\Mentall\\Desktop\\Project\\Arch'):
			for file in files:
				if file.endswith('.py'):
					fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Users\\Гусев\\Desktop\\Project'), compress_type = zipfile.ZIP_DEFLATED)
		fantasy_zip.close()
		
 		


if __name__ == "__main__":##
	 BoxApp().run()##

