import random
import hashlib
import string
import base64
import bcrypt


class DevToolkit:
    def __init__(self):
        self.lorem_words = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor".split()

    def password_generate(self, length=12):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for i in range(length))

    def bcrypt_hash(self, text):
        salt = bcrypt.gensalt()
        bcrypt.hashpw(text.encode(), salt).decode()

    def base64_handle(self, text, mode='encode'):
        try:
            if mode == 'encode':
                return base64.b64encode(text.encode()).decode()
            return base64.b64decode(text.encode()).decode()
        except Exception:
            print("Error: Invalid input for Base64")

    def get_lorem(self, count=20):
        return ' '.join(random.choice(self.lorem_words) for i in range(count))


class CLI:
    def __init__(self):
        self.tool = DevToolkit()

    def run(self):
        print("1. Password Gen | 2. Bcrypt | 3. Base64 Encode | 4. Base64 Decode | 5. Lorem | 6. Exit")

        choice = input("\nAction: ")

        while True:
            try:
                if choice == '1':
                    size = int(input("Length (Default 12): ") or 12)
                    print(f"Password: {self.tool.password_generate(size)}")
                elif choice == '2':
                    text = input("Enter the Text to Hash: ")
                    print(f"{self.tool.bcrypt_hash(text)}")
                elif choice == '3':
                    value = input("Enter the Text to Encode: ")
                    print(f"{self.tool.base64_handle(value, 'encode')}")
                elif choice == '4':
                    value = input("Enter the Text to Decode: ")
                    print(f"{self.tool.base64_handle(value, 'decode')}")
                elif choice == '5':
                    length = int(input("Enter the length: ") or 20)
                    print(f"{self.tool.get_lorem(length)}")
                elif choice == '6':
                    print("Bye")
                    break

            except ValueError:
                print("Please enter a valid number!")


if __name__ == "__main__":
    cli = CLI()
    cli.run()
