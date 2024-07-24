class Sieve:
    def __init__(self) -> None:
        # Load precomputed prime numbers from the file
        self.primes = []
        with open("primes.txt", "r") as f:
            for line in f:
                self.primes.append(int(line.strip()))

    def nth_prime(self, n: int) -> int:
        # Return the nth prime number if within the precomputed range
        if n < len(self.primes):
            print(f"{n}-th prime number: {self.primes[n]}")
            return self.primes[n]
        else:
            raise ValueError("Prime number out of precomputed range")

    def is_prime(self, num: int) -> bool:
        # Check if a number is prime
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
