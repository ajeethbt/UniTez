import pymysql as sqlpy
from blessed import Terminal

global_in = ""

class flashfunc:
	def __init__(self,host,username,passwd,db):
		self.hostname=host
		self.username=username
		self.passwd=passwd
		self.db=db
		
	def newdeck(self,deck_n):
		mycon = sqlpy.connect(host = self.hostname,user = self.username,password = self.passwd,database = self.db)
		cursor = mycon.cursor()
		cursor.execute(f"create table {deck_n}(frontcard blob not null unique,backcard mediumtext not null,difficulty tinyint default 5,seen smallint default 0)")		
		mycon.commit()
		mycon.close()
		
	def dropdeck(self,deck_n):
		mycon = sqlpy.connect(host = self.hostname,user = self.username,password = self.passwd,database = self.db)
		cursor = mycon.cursor()
		cursor.execute(f"drop table {deck_n}")		
		mycon.commit()
		mycon.close()
		
	def showdecks(self):
		mycon = sqlpy.connect(host = self.hostname,user = self.username,password = self.passwd,database = self.db)
		cursor = mycon.cursor()
		cursor.execute(f"show tables")
		data_p = []
		data = cursor.fetchall()
		mycon.close()
		for i in data:
			data_p.append(i[0])
		return data_p
		
	def curlout(self,table_d):
		mycon = sqlpy.connect(host = self.hostname,user = self.username,password = self.passwd,database = self.db)
		cursor = mycon.cursor()
		cursor.execute(f"select * from {table_d}")
		data_p = []
		data = cursor.fetchall()
		mycon.close()
		return data
		
		
	def curlins(self,execute_c):
		mycon = sqlpy.connect(host = self.hostname,user = self.username,password = self.passwd,database = self.db)
		cursor = mycon.cursor()
		cursor.execute(execute_c)
		mycon.commit()
		mycon.close()
		
	def newcard(self,table_d,front_c,back_c):
		self.curlins(f"insert into {table_d}(frontcard,backcard) values('{front_c}','{back_c}')")
		
dostuff=flashfunc("localhost","root","password","flashcards")


class FlashTerminal:
	def __init__(self):
		self.whereit = 0
		self.session_info = ["",""] #database,table  for now only has table in the start
		self.term=Terminal()
		self.width= self.term.width
		self.height = self.term.height
		print(self.term.home + self.term.clear, end='')
		self.data_b = flashfunc("localhost","root","password","flashcards")
		
	def console(self):
		print(self.term.home + self.term.move_xy(1, 21) + "CONSOLE:", end = "")
		info_in = input()
		return info_in

	def homescreen(self):
		print(self.term.move_xy((self.width-10)//2,2) + "Welcome to" + self.term.move_xy((self.width-8)//2,4)+ "FlashPy" + self.term.move_xy(3,6) + "Your decks: ")
		for i in enumerate(self.data_b.showdecks(),0):
			print(self.term.move_xy(4,8 + i[0]) + f"{i[0]}.{i[1]}")
	
	def play_screen(self):
		print(self.term.clear + self.term.move_xy((self.width-5)//2,2) + f"Learning deck: {info_in}" + self.term.move_xy(3,6) + f"Your cards:{len(self.data_b.curlout(info_in.lower()))} ")
		info_in = self.console()
		if info_in == "back":
			self.homescreen()
			break
		
		
	
	def deck_play(self):
		info_in = self.console()
		if info_in == "start":
			all_cards_front= []
			all_cards_back = []
			for i in self.data_b.curlout(self.session_info[1]):
				all_cards_front.append(i[0])
				all_cards_back.append(i[1])
			for i in range(len(all_cards_front)):
				print(self.term.clear + self.term.home + self.term.move_xy(5, 10) + all_cards_front[i].decode(encoding="utf-8"), end = "")
				if self.console() == "show":
					print(self.term.clear + self.term.home + self.term.move_xy(5, 10) + all_cards_back[i], end = "")
					if self.console() == "next":
						continue
				elif self.console() == "back":
					self.play_screen()
					break
					

			
    		
flashy = FlashTerminal()
flashy.play_screen()
flashy.deck_play()


