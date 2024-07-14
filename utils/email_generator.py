import random


class EmailGenerator:
    @staticmethod
    def generate_unique_email(domain):
        random_number = random.randint(1, 999)
        return f"dmitry_bukhvalov_{random_number}@{domain}"
