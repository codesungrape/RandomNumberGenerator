import random

# generating single random numbers
random_number = random.randint(1, 59); # inclusive
print(f"Random number: {random_number}")


# generating multiple random numbers
random_numbers = [random.randint(1, 59) for _ in range(6)]
print(f"Random numbers: {random_numbers}")


# generating UNIQUE random numbers
unique_random_numbers = random.sample(range(1, 59), 7)
print(f"Unique random numbers: {unique_random_numbers}")
