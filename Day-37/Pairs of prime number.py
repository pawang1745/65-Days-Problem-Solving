class Solution:
    def prime_pairs(self, n):
        # Function to generate prime numbers up to n
        def sieve_of_eratosthenes(limit):
            sieve = [True] * (limit + 1)
            sieve[0] = sieve[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, limit + 1, i):
                        sieve[j] = False
            primes = [i for i in range(limit + 1) if sieve[i]]
            return primes

        primes = sieve_of_eratosthenes(n)
        pairs = []

        # Form pairs of primes
        for i in range(len(primes)):
            for j in range(i, len(primes)):
                product = primes[i] * primes[j]
                if product <= n:
                    pairs.append((primes[i], primes[j]))
                    if primes[i] != primes[j]:
                        pairs.append((primes[j], primes[i]))  # Include the reverse pair

        # Remove duplicates and sort the pairs
        unique_pairs = sorted(set(pairs))

        # Format the pairs as strings in the required format
        formatted_pairs = [' '.join(map(str, pair)) for pair in unique_pairs if pair[0] * pair[1] <= n]
        return formatted_pairs


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.prime_pairs(n)
		for i in ans:
			print(i, end = " ")
		print()
