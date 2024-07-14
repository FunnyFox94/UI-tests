import random


class PasswordGenerator:
    @staticmethod
    def generate_unique_password():
        random_number = random.randint(1000, 999999)
        return random_number
