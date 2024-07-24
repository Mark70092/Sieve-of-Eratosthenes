Sure, here is the markdown version:

# Instructions

## How it works:

### Understanding the Task:

- First, I needed to find a way to get the Nth prime number. The Nth prime number means, for example, the 1st prime number is 2, the 2nd is 3, and so on.

### Choosing the Method:

- I chose a method called "Sieve of Eratosthenes." It's a way to find all prime numbers up to a certain number by marking the multiples of each prime number starting from 2.

### Writing the Code:

- I wrote some code in Python. Python is a programming language that I used to make my solution.
- I made a file called `generate_primes.py`. This file creates a list of prime numbers and saves them in another file called `primes.txt`.

### Creating a Function to Get Primes:

- I created a function to estimate how big the list should be to include enough prime numbers.
- Then, I used the "Sieve of Eratosthenes" method to find all these prime numbers and saved them in `primes.txt`.

### Loading Primes for Use:

- I wrote another file called `sieve.py`. This file loads the prime numbers from `primes.txt` so that we can use them quickly.

### Testing the Code:

- I wrote tests in a file called `test_sieve.py`. These tests check if my function to get the Nth prime number works correctly.
- To run the tests, I used the command `python -m unittest discover`. This command finds all the test files and runs them.