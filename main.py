import jellyfish  # not used as of now
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

    def card_subject_search(self):
        self.card_refresh()
        return list(self.card_data.keys())

    def card_chapter_search(self):
        self.card_refresh()
        try:
            self.card_location_check("subject")
            return list(self.card_data[self.location[1]].keys())
        except TypeError:
            print("Location of Card not specified, provide \"chapter\" and \"subject\"")

    def card_location_check(self, card_type="all"):
        if "chapter" in card_type.lower():
            if "NA" in self.location[0]:
                raise TypeError("Location of Card not specified, provide \"chapter\" and \"subject\"")
        elif "subject" in card_type.lower():
            if "NA" in self.location[1]:
                raise TypeError("Location of Card not specified, provide \"chapter\" and \"subject\"")
        elif "all" in card_type.lower():
            if any(element == "NA" for element in self.location):
                raise TypeError("Location of Card not specified, provide \"chapter\" and \"subject\"")

    def card_keys(self):
        self.card_location_check()
        self.card_refresh()
        return list(self.card_data[self.location[1]][self.location[0]].keys())

    def card_refresh(self):
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
        self.loc = ["NA", "NA"]
        self.Unitez = Unitez(self.loc[0], self.loc[1])

    def console_refresh(self):
        self.Unitez = Unitez(self.loc[0], self.loc[1])

    def console_start(self):
        while True:
            self.console_inputs()

    def console_inputs(self):
        input_c = self.console_in().replace(" ", "").lower()
        if re.search("^chp", input_c):
            if "NA" not in self.loc[1]:
                self.loc[0] = re.sub("^chp", "", input_c)
                self.console_refresh()
            else:
                print("Error: Specify Subject first")
        elif re.search("^sub", input_c):
            self.loc[1] = re.sub("^sub", "", input_c)
            self.console_refresh()
        elif re.search("^list", input_c):
            if re.search("^sub", re.sub("^list", "", input_c)):
                for chapter in self.Unitez.card_subject_search():
                    print(chapter)
            if re.search("^chap", re.sub("^list", "", input_c)):
                for chapter in self.Unitez.card_chapter_search():
                    print(chapter)

    def console_in(self):
        return input(f"Console(/{self.loc[1]}/{self.loc[0]}): ")


console = Console()
console.console_start()
