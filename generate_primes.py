import math

def estimate_nth_prime(n):
    """
    Estimate the upper limit for the nth prime number using the approximation formula:
    p(n) ≈ n * (log(n) + log(log(n)))
    This provides an upper bound which is sufficiently large to contain at least the nth prime.
    """
    if n < 6:
        return 15  # Small approximation for small values of n
    # Using the approximation formula to estimate the upper limit for the nth prime number
    return int(n * (math.log(n) + math.log(math.log(n))))

def generate_primes(limit):
    """
    Generate prime numbers up to the specified limit using the Sieve of Eratosthenes algorithm
    and save them to a file.
    """
    # Initialize the sieve with True values
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Use the Sieve of Eratosthenes algorithm to find all primes up to 'limit'
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit, start):
                sieve[multiple] = False

    # Collect all prime numbers
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    # Save primes to a file
    with open("primes.txt", "w") as f:
        for prime in primes:
            f.write(f"{prime}\n")

# Define the target for the nth prime number
n = 10000000

# Estimate the upper limit for the 10-millionth prime number
limit = estimate_nth_prime(n)
print(f"Estimated upper limit for the {n}-th prime number: {limit}")

# Generate the file with the first 10 million prime numbers
generate_primes(limit)
