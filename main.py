import jellyfish
import json

dict_ = {
    "physics": {
        "oscillation":
            {
                "card_0":
                    ["When did India Get Independence", [1951, 1947, 1948, 1949, 2]]

            }
    }
}
chapters = ""
chapter = ""
chapter_selection = ""
subject = input("Subject: ").lower()
if subject in dict_:
    chapters = dict_[subject]
    chapter = input("Chapter: ").lower()
    if chapter in chapters:
        chapter_selection = dict_[subject][chapter]
        print(f"There are {len(dict_.get(subject).get(chapter))} cards in this chapter")
        cards = dict_.get(subject).get(chapter)
        print(
            f"\n\nQuestion: {list(cards.values())[0][0]}\nOptions: "
            f"{' '.join(map(str, list(cards.values())[0][1][:3]))}")


    else:
        if jellyfish.jaro_similarity("oscillations", chapter) * 100 >= 60:
            print(f"{chapter} is not found, did you mean oscillations?")
        else:
            print(f"{chapter} is not found, please try again")
else:
    if jellyfish.jaro_similarity("physics", subject) * 100 >= 60:
        print(f"{subject} is not found, did you mean physics?")
    else:
        print(f"{subject} is not found, please try again")
