import jellyfish
import json
import re


class Unitez:
    def __init__(self, chapter, subject):
        self.location = [chapter, subject]
        open1 = open('data.json', 'r')
        card_datas = json.load(open1)
        open1.close()
        self.card_data = card_datas

    def card_refresh(self):
        with open('data.json', 'w') as file_w:
            json.dump(self.card_data, file_w, indent=2)
        with open('data.json', 'r') as file_r:
            self.card_data = json.load(file_r)

    def add_card(self, question, option):
        cards = list(json.load(open('data.json', 'r'))[self.location[1]][self.location[0]].keys())
        number_card = 0
        for i in cards:
            number_card = int(re.sub("card_", "", i))
        self.card_data[self.location[1]][self.location[0]]["card_" + str(number_card + 1)] = [question, option]
        self.card_refresh()
        print(self.card_data)

    def delete_card(self, card_number):
        del self.card_data[self.location[1]][self.location[0]]["card_" + str(card_number)]
        cards = list(self.card_data[self.location[1]][self.location[0]].keys())
        print(cards)
        print(self.card_data)

        # card_data[self.location[1]][self.location[0]]


test = Unitez("oscillation", "physics")
# test.add_card('yes', 'no')
test.delete_card(2)
