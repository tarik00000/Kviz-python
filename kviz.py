def multiple_choice(question, answer_options, correct_answer):
    attempts = 0
    while attempts < 3:
        print(question)
        print("B) " + answer_options[0])
        print("C) " + answer_options[1])
        user_answer = input("Vas odgovor: ")
        if user_answer.upper() == correct_answer:
            print("Tacno! Dobili ste 2 boda.")
            return 2
        else:
            attempts += 1
            if attempts < 3:
                print("Pokusaj ponovo.")
            else:
                print("Pogresno. Tacan odgovor je " + correct_answer + ". Izgubio si 1 bod.")
                return -1

play_again = True
while play_again:
    questions = [
        {
            "pitanje": "Koji je glavni grad Kanade?",
            "answer_options": ["Ottawa", "Toronto"],
            "correct_answer": "B"
        },
        {
            "pitanje": "Koji je najveći organ u ljudskom tijelu?",
            "answer_options": ["Pluca", "Koza"],
            "correct_answer": "C"
        },
        {
           "pitanje": "What is the square root of 16?",
            "answer_options": ["3", "4"],
            "correct_answer": "C"
        },
        {
            "pitanje": "Ko je izumio telefon?",
            "answer_options": ["Thomas Edison", "Alexander Graham Bell"],
            "correct_answer": "B"
        },
        {
            "pitanje": "Koji je planet u našem Sunčevom sustavu poznat po tome što ima sustav prstenova?",
            "answer_options": ["Jupiter", "Saturn"],
            "correct_answer": "C"
        }
    ]

    total_score = 0
    for q in questions:
        question_score = multiple_choice(q["pitanje"], q["answer_options"], q["correct_answer"])
        total_score += question_score
        if question_score == -1:
            total_score -= 1
    print("Tvoj score je : " + str(total_score) + " od 10.") 

    play_again_input = input("Da li hocete da pokusate ponovo? (y/n) ")
    if play_again_input.lower() != "y":
        play_again = False
