import random

# ASCII Art-is funqcia
def display_welcome():
    art = """
    lets play history questions!
            \   ^__^
             \  (oo)\_______
                (__)\       )
                    ||-----||
                    ||     ||
    """
    print(art)

# kitxvebis baza
def get_questions():
    return [
        {"question": "Who was the first president of the United States?", "answer": "George Washington"},
        {"question": "What year did World War II end?", "answer": "1945"},
        {"question": "What was the name of the wall that divided Berlin?", "answer": "Berlin Wall"},
        {"question": "In which country did the Industrial Revolution begin?", "answer": "Great Britain"},
        {"question": "Who was the first man on the moon?", "answer": "Neil Armstrong"}
    ]

def start_game():
    questions = get_questions()

    # axali funqcia random.sample - igebs siidan shetxvevit elementebs
    game_questions = random.sample(questions, k = len(questions))

    score = 100
    display_welcome()

    print("welcome! for quiting press 'quit'.")

    # cikli
    for i, q in enumerate(game_questions, 1):
        while True:
            # axali funqcia 2: .upper() an .capitalize() gamoyeneba testis formatirebistvis
            # aseve f-string-s gamosatanad
            user_input = input(f"\nquestion{i}: {q['question']} ").strip()

            #tamashis dassrulebis archeva
            if user_input.lower() == 'quit':
                print(f"\ngame over, your score is: {score}")
                return

            #pirobiTi operratorebi
            if user_input.lower() == q["answer"].lower():
                print("correct, good job")
                break
            else:
                score -= 10
                print(f"incorrect -10 score. Your score now: {score}")
                print("try again or press 'quit'")

    print(f"\ncongratulations")
    print(f"you ended questions, whole score: {score}")

# tamshis dawyeba unda tu ara
choice = input("do you want to play history? (yes/no): ").lower()
if choice == 'yes':
    start_game()
else:
    print("bye, next time")

#ASCII Art- funqcia dasasrulistvis(es pitonia)
art2 = r"""
        /^\/^\
      _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \                  /\
                `\     \                 \ \
                  |     |                  \ \
                  /      /                    \ \
     ( )         /     /                       \ \
      \ \       /      /                         \ \
       \ \     /     /                            \  \
        \   /     /             _----_            \   \
         \/     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
"""
print(art2)
