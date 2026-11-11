

def get_phrase_input():
    user_phrase = input("Type a phrase (or quit to exit program): ").lower()
    
    return user_phrase
        
def get_user_letters():

    user_letters = input("\nType a comma-separated list of letter to redact: ").split(",")

    return user_letters


def redact_letters(user_letters, user_phrase):
    redacted_count = 0
    

    for char in user_letters:

        char = char.strip().lower()


        redacted_count += user_phrase.count(char)
        
        user_phrase = user_phrase.replace(char, "_")

    return user_phrase, redacted_count



def output(user_phrase, user_letters):
    redacted_user_phrase, redacted_count = redact_letters(user_letters, user_phrase)

    print(f"Number of letters redacted: {redacted_count}")
    print(f"Redacted phrase: {redacted_user_phrase}\n")
    
def main():
    while True:
        user_phrase = get_phrase_input()

        if user_phrase == 'quit':
            break
        else: 
            user_letters = get_user_letters()
            output(user_phrase, user_letters)
            


main()