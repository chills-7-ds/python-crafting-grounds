# This file contains various quiz questions categorized into different topics.

science_questions = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
        "answer": "b"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "answer": "b"
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "answer": "c"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["a) Gold", "b) Iron", "c) Diamond", "d) Quartz"],
        "answer": "c"
    },
    {
        "question": "What part of the human body has the smallest bones?",
        "options": ["a) Hands", "b) Feet", "c) Ears", "d) Spine"],
        "answer": "c"
    }
]

history_questions = [
    {
        "question": "Who was the first President of the United States?",
        "options": ["a) George Washington", "b) Thomas Jefferson", "c) Abraham Lincoln", "d) John Adams"],
        "answer": "a"
    },

    {
        "question": "What year did World War II end?",
        "options": ["a) 1945", "b) 1944", "c) 1946", "d) 1947"],
        "answer": "a"
    },

    {
        "question": "Who discovered penicillin?",
        "options": ["a) Marie Curie", "b) Alexander Fleming", "c) Louis Pasteur", "d) Albert Einstein"],
        "answer": "b"
    },

    {
        "question": "What ancient civilization built the pyramids?",
        "options": ["a) Romans", "b) Greeks", "c) Egyptians", "d) Mayans"],
        "answer": "c"
    }
]

pop_culture_questions = [
    {
        "question": "Who played Jack Dawson in Titanic?",
        "options": ["a) Brad Pitt", "b) Leonardo DiCaprio", "c) Johnny Depp", "d) Tom Cruise"],
        "answer": "b"
    },

    {
        "question": "What is the highest-grossing film of all time?",
        "options": ["a) Avatar", "b) Titanic", "c) Star Wars: The Force Awakens", "d) Avengers: Endgame"],
        "answer": "d"
    },

    {
        "question": "Which singer is known as the 'Queen of Pop'?",
        "options": ["a) Britney Spears", "b) Madonna", "c) Lady Gaga", "d) Taylor Swift"],
        "answer": "b"
    },

    {
        "question": "What animated film features a talking snowman named Olaf?",
        "options": ["a) Moana", "b) Frozen", "c) Tangled", "d) Zootopia"],
        "answer": "b"
    }
]

 
def get_questions(category_choice):  
    question_categories = {
        "1": science_questions,  
        "2": history_questions,  
        "3": pop_culture_questions
    }
    return question_categories.get(category_choice)