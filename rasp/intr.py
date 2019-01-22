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
Config.set('graphics','height','720');##Изминение высоты


class BoxApp(App):

	

	def build(self):
		al = AnchorLayout()
		bl = BoxLayout(spacing = 15,orientation= 'vertical',padding = 55)
		self.lbl = Label(text = "",size=(360,480))
		bl.add_widget(self.lbl)
		bl.add_widget(Button(text = "Понедельник",halign = "center" ,on_press = self.btn_press_ponedel))
		bl.add_widget(Button(text = "Вторник",halign = "center" ,on_press = self.btn_press_vtornick))
		bl.add_widget(Button(text = "Среда",halign = "center" , on_press = self.btn_press_sreda))
		bl.add_widget(Button(text = "Четверг",halign = "center" ,on_press = self.btn_press_chetverg))
		bl.add_widget(Button(text = "Пятница",halign = "center" ,on_press = self.btn_press_pytnica))
		bl.add_widget(Button(text = "Суббота",halign = "center" ,on_press = self.btn_press_subbota))
		al.add_widget(bl)
		return al
		
	def btn_press_ponedel(self,instance):
		p=open(u'C:/Users/Гусев/Desktop/Project/rasp/Понедельник.txt','r')
		s1=p.read()
		self.lbl.text =s1
		p.close()
	def btn_press_vtornick(self,instance):
		v=open(u'C:/Users/Гусев/Desktop/Project/rasp/Вторник.txt','r')
		s2=v.read()
		self.lbl.text = s2
		v.close()
	def btn_press_sreda(self,instance):
		sr=open(u'C:/Users/Гусев/Desktop/Project/rasp/Среда.txt','r')
		s3=sr.read()
		self.lbl.text =s3
		sr.close()
	def btn_press_chetverg(self,instance):
		c=open(u'C:/Users/Гусев/Desktop/Project/rasp/Четверг.txt','r')
		s4=c.read()
		self.lbl.text =s4
		c.close()
	def btn_press_pytnica(self,instance):
		pt=open(u'C:/Users/Гусев/Desktop/Project/rasp/Пятница.txt','r')
		s5=pt.read()
		self.lbl.text =s5
		pt.close()
	def btn_press_subbota(self,instance):
		su=open(u'C:/Users/Гусев/Desktop/Project/rasp/Суббота.txt','r')
		s6=su.read()
		self.lbl.text =s6
		su.close()



			

		
		
 		


if __name__ == "__main__":##
	 BoxApp().run()##

