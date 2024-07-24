Конечно! Вот обновленная версия в формате Markdown с добавлением команд для генерации файла и запуска тестов:

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

## Running the Code

### Step 1: Generate the `primes.txt` File

Run the following command to generate the `primes.txt` file:

```bash
python generate_primes.py
```

This will create a file named `primes.txt` containing a list of prime numbers.

### Step 2: Run the Tests

After generating the `primes.txt` file, you can run the tests to ensure everything is working correctly:

```bash
python -m unittest discover
```

This command will find and run all the test files and check if everything works correctly.

By following these steps, you can see how I created the solution, how it works, and how to test it. If you need any more help, just let me know!