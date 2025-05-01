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

    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}")

    print(f"\n🎉 Quiz completed! Your score: {score}/{len(questions)}")

# Run the quiz
run_quiz()
