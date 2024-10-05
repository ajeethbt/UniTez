from blessed import Terminal



class Flashterminal:
    def __init__(self):
        self.term = Terminal()
        self.width = self.term.width
        self.height = self.term.height
        
    def console(self):
        print(self.term.home + self.term.move_xy(1, 21) + "CONSOLE:", end = "")
        info_in = input()
        return info_in
        
    def show_in(self):
        print(self.term.home + self.term.move_xy(4,5) + self.console())

something = Flashterminal()
something.show_in
