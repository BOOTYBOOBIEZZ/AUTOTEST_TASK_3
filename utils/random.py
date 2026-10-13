import random
import string


class RandomText:
    def generate_random_text(self, length: int = 10) -> str:
        letters = string.ascii_letters
        return "".join(random.choice(letters) for _ in range(length))
