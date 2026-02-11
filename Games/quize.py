import requests
import random
import html
import os


class QuizEngine:
    def __init__(self):
        self.api_url = "https://opentdb.com/api.php?amount=1&category=18&type=multiple"

    def fetch_question(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()

            if data['response_code'] == 0:
                result = data['results'][0]

                # Sawal aur sahi jawab nikalna
                question = html.unescape(result['question'])
                correct_ans = html.unescape(result['correct_answer'])
                incorrect_ans = [html.unescape(ans)
                                 for ans in result['incorrect_answers']]

                options = incorrect_ans + [correct_ans]
                random.shuffle(options)

                return {
                    "question": question,
                    "options": options,
                    "answer": correct_ans
                }
        except Exception as e:
            return None


class Quiz:
    def __init__(self):
        self.engine = QuizEngine()
        self.score = 0

    def start(self):
        print("Welcome to CodeQuiz!")

        while True:
            q_data = self.engine.fetch_question()
            if not q_data:
                print("Error fetching question. Check Internet.")
                break

            print(f"\nScore: {self.score}")
            print(f"Q: {q_data['question']}")

            for idx, opt in enumerate(q_data['options'], 1):
                print(f"{idx}. {opt}")

            user_input = input(
                "\nYour Answer (1-4) or 'q' to quit: ").strip().lower()

            if user_input == 'q':
                print(f"Final Score: {self.score}. Goodbye!")
                break

            try:
                choice_idx = int(user_input) - 1
                selected_ans = q_data['options'][choice_idx]

                if selected_ans == q_data['answer']:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! Correct answer was: {q_data['answer']}")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1-4.")


if __name__ == "__main__":
    app = Quiz()
    app.start()
