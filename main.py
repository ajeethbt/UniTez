import jellyfish
import json
import re


class Unitez:
    def __init__(self, chapter="NA", subject="NA"):
        self.location = [chapter, subject]
        open1 = open('data.json', 'r')
        card_datas = json.load(open1)
        open1.close()
        self.card_data = card_datas

    def card_organizer(self):
        self.card_location_check()
        cards = sorted(self.card_keys(), key=lambda x: int(re.sub("card_", "", x)))
        for index, key in enumerate(cards):
            if key != "card_" + str(index):
                self.card_data[self.location[1]][self.location[0]]["card_" + str(index)] = \
                    self.card_data[self.location[1]][self.location[0]][key]
                del self.card_data[self.location[1]][self.location[0]][key]
                self.card_refresh()

    def card_location_check(self):
        if any(element == "NA" for element in self.location):
            raise TypeError("Location of Card not specified, provide \"chapter\" and \"subject\"")

    def card_keys(self):
        self.card_location_check()
        self.card_refresh()
        return list(self.card_data[self.location[1]][self.location[0]].keys())

    def card_refresh(self):
        self.card_location_check()
        with open('data.json', 'w') as file_w:
            json.dump(self.card_data, file_w, indent=2)
        with open('data.json', 'r') as file_r:
            self.card_data = json.load(file_r)

    def card_add(self, question, option):
        self.card_location_check()
        cards = self.card_keys()
        number_card = 0
        for i in cards:
            number_card = int(re.sub("card_", "", i))
        self.card_data[self.location[1]][self.location[0]]["card_" + str(number_card + 1)] = [question, option]
        self.card_refresh()
        print(self.card_data)

    def card_del(self, card_number):
        self.card_location_check()
        del self.card_data[self.location[1]][self.location[0]]["card_" + str(card_number)]
        self.card_refresh()
        self.card_organizer()
        # card_data[self.location[1]][self.location[0]]


class Console:
    def __init__(self):
        self.Unitez = Unitez("oscillation", "physics")
        self.loc = ["NA","NA"]

    def console_start(self):
        while True:
            something = self.console_in()

    def location(self):

        (self.console_in().strip())
        return "hi"

    def console_in(self):
        return input(f"Console({self.location()}): ")


console = Console()
console.console_start()
