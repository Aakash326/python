def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A. Charles Dickens", "B. Leo Tolstoy", "C. William Shakespeare", "D. Mark Twain"],
            "answer": "C"
        }
    ]

    score = 0

    for idx, i in enumerate(questions, 1):
        print(f"\nQ{idx}: {i['question']}")
        for option in i["options"]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == i["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {i['answer']}")

    print(f"\n🎉 Quiz completed! Your score: {score}/{len(questions)}")

run_quiz()
