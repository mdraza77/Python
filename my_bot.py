import random
import time
from datetime import datetime


def my_bot():
    responses = {
        "hi": [
            "Hello!", "Hi there!", "Hey! Kaise ho?",
            "Namaste!", "Good to see you here!"
        ],

        "kaise ho": [
            "Main badhiya hoon, aap batao?",
            "I am doing great, thanks for asking!",
            "Sab mast! Tum sunao kya chal raha hai?"
        ],

        "name": [
            "Main ek simple Python chatbot hoon.",
            "Tum mujhe PyBot bula sakte ho.",
            "Abhi mera naam decide nahi hua 😄"
        ],

        "help": [
            "Main basic questions ka jawab de sakta hoon.",
            "Tum mujhse project, coding, ya general baatein puch sakte ho.",
            "Try asking about Python, Laravel, ya internship."
        ],

        "project": [
            "Yeh mera Python project hai, ek interactive chatbot.",
            "Maine ise as a mini project banaya hai.",
            "Is project ka goal basic conversation handle karna hai."
        ],

        "skills": [
            "Mujhe Python, basic NLP logic, aur chatbot flow pata hai.",
            "Main keyword matching se kaam karta hoon.",
            "Abhi AI level smart nahi hoon, but improving 😄"
        ],

        "python": [
            "Python ek powerful aur beginner-friendly language hai.",
            "Python automation, AI, web dev sab mein use hoti hai.",
            "Kya tum Python seekh rahe ho?"
        ],

        "laravel": [
            "Laravel ek PHP framework hai, maine Yasham mein ispe internship ki hai.",
            "Laravel MVC architecture follow karta hai.",
            "Authentication aur routing Laravel mein easy hota hai."
        ],

        "internship": [
            "Internship real-world experience deti hai.",
            "Tumne kis tech stack par kaam kiya?",
            "Internship se learning fast hoti hai."
        ],

        "time": [
            "Mujhe real time nahi pata, but tum system clock check kar sakte ho.",
            "Time dekhna ho to device ka clock use karo current_time 😄",
        ],

        "date": [
            "Aaj ka exact date mujhe nahi pata bina system access ke.",
            "Calendar check karo, wahi safest option hai."
        ],

        "joke": [
            "Programmer ne girlfriend kyun chhodi? Because she had too many bugs 😄",
            "Why do programmers love dark mode? Because light attracts bugs.",
            "Debugging: Being the detective in a crime movie where you are also the murderer."
        ],

        "thanks": [
            "You're welcome!",
            "Koi baat nahi 😄",
            "Happy to help!"
        ],

        "bye": [
            "Alvida! Phir milenge.",
            "Bye! Have a great day!",
            "Take care! Coding mat chhodna 😄"
        ],

        "default": [
            "Hmm, main samjha nahi. Kya aap kuch aur puch sakte hain?",
            "Interesting! Mujhe is baare mein aur batao.",
            "Ye thoda mere scope ke bahar hai abhi.",
            "Try asking something about coding, project, ya internship."
        ],
    }

    print("\n--- My ChatBot ---")
    print("(Type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'bye':
            print("Bye!")

        print("Thinking...")
        time.sleep(1)

        result = False

        for key in responses:
            if key in user_input:
                print(f"MyBot: {random.choice(responses[key])}")
                result = True
                break
        if not result:
            print(f"Chatbot: {random.choice(responses['default'])}")


if __name__ == '__main__':
    my_bot()
