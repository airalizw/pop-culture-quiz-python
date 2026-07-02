# Pop Culture Quiz Game
# This quiz tests your pop culture knowledge from the early 2000s

# Welcome message
print("Welcome to the Pop Culture Quiz!")
print("Answer each question and see how well you know your pop culture!")
print("")

# Store questions and answers in a dictionary
questions = {
    "Which hit early 2000s song featured the line Im in the club with a bottle full of bub?": "in da club",
    "Which famous couple wore matching all-denim outfits to the 2001 American Music Awards?": "britney spears and justin timberlake",
    "What was the name of the rival cheerleading team in Bring It On?": "the clovers",
    "In Twilight what is the name of the vampire coven Edward belongs to?": "the cullen family",
    "Which book series following a young wizard at a magical school became a defining phenomenon for Millennials?": "harry potter"
}

# Keep track of score
score = 0

# Loop through each question and check the answer
for question, answer in questions.items():
    user_answer = input(question + " ")
    user_answer = user_answer.lower().strip()
    
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer is {answer}")

# Print final score
print(f"\nYou got {score} out of {len(questions)} correct!")

# Personalized score message
if score == 5:
    print("Perfect score! You are a pop culture legend!")
elif score >= 3:
    print("Good job! You know your pop culture!")
else:
    print("Keep brushing up on your pop culture knowledge!")