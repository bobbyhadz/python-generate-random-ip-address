# Generate a random IP address in Python

from random import randint


def generate_random_ip():
    return '.'.join(
        str(randint(0, 255)) for _ in range(4)
    )


random_ip = generate_random_ip()
print(random_ip)  # 👉️ 178.166.111.80

random_ip = generate_random_ip()
print(random_ip)  # 👉️ 124.56.199.70