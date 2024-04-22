import random

# Dictionary of English phrases and their Japanese equivalents
flashcards = {
	"Hajimemashite. [name] desu": "Nice to meet you. I'm [name]",
	"Yoroshiku onegai shimasu": "Please look favorably upon me.",
	"Watashi": "I / me (men and women)",
	"Boku": "I / me (just men)",
	"desu": "to be",
	"wa": "is / was / am",
	"Ohayō": "Good morning (informal)",
	"Ohayō gozaimasu": "Good morning (formal)",
	"Kon'nichi wa": "Hello",
	"Konban wa!": "Good evening",
	"Sayōnara": "Good bye",
	"Omiyage": "souvenir / small gift",
	"Omiyage desu": "(this is) A small gift for you",
	"Arigatō gozaimasu!": "Thank you",
	"Dō itashimashite": "You are welcome",
	"Itatata": "Ouch",
	"Ano": "um",
	"sumimasen": "Excuse me / I am sorry",
	"Hai": "Yes / sure",
	"Iie": "No",
	"Ashi": "foot",
	"Menyū": "Menu",
	"Sumimasen! Menyū, onegai shimasu.": "Excuse me, can I get a menu?",
	"mizu": "water",
	"chūmon": "order",
	"A, [name]-san?": "Oh, [name] (is that you?)",
	"[name]-san! O-hisashiburi desu!": "[name]! It's been a while! (formal)",
	"O-hisashiburi desu!": "Long time no see! (formal)",
	"hisashiburi": "Long time no see! (informal)",
	"San": "suffix to show respect (like Mr or Mrs)" #,
#	"" : "",
#	"" : "",
#	"" : "",
#	"" : "",
#	"" : "",
#	"" : "",
#	"" : "",
#	"" : ""


}

def generate_flashcards():
    while True:
        print("Choose an option:")
        print("1. English phrases with Japanese equivalents")
        print("2. Japanese phrases with English equivalents")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\n--- English phrases with Japanese equivalents ---")
            flashcard_keys = list(flashcards.keys())
            random.shuffle(flashcard_keys)
            for key in flashcard_keys:
                input(f"{key} - Press Enter to reveal the Japanese equivalent")
                print(flashcards[key])
                input("Press Enter for the next flashcard")
            break
        elif choice == "2":
            print("\n--- Japanese phrases with English equivalents ---")
            flashcard_keys = list(flashcards.keys())
            random.shuffle(flashcard_keys)
            for key in flashcard_keys:
                input(f"{flashcards[key]} - Press Enter to reveal the English equivalent")
                print(key)
                input("Press Enter for the next flashcard")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    generate_flashcards()
