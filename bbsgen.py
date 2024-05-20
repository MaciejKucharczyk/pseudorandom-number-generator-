import random

def get_prime(bitsize):
    """Generuje dużą liczbę pierwszą o określonym rozmiarze bitów."""
    while True:
        p = random.getrandbits(bitsize)
        print(f"Liczba: {p}")
        if is_prime(p):
            return p
        
def sieve_of_eratosthenes(limit): # e.g. limit = 100
    """Zwraca listę liczb pierwszych do określonego limitu używając sita Eratostenesa."""
    sieve = [True] * (limit + 1)  # Tworzymy listę początkowo ustawioną na True
    p = 2  # Najmniejsza liczba pierwsza

    while (p * p <= limit):
        if sieve[p] == True:  # Jeśli sieve[p] nie zostało jeszcze przekreślone, to jest pierwsze
            # Przekreślamy wszystkie wielokrotności p, zaczynając od p^2
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1

    # Zbieramy wszystkie liczby pierwsze
    primes = [p for p in range(2, limit + 1) if sieve[p]]
    return primes


def is_prime(n, k=100000):  # zwiększ k dla większej dokładności testu
    """ Test Pierwszosci Millera-Rabina """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Znajdź r i s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    # Wykonaj k testów Millera-Rabina
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def is_prime2(n):
    """Prosty test pierwszości """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class BlumBlumShub:
    def __init__(self, bit_size=512):
        self.p = get_prime(bit_size // 2)
        self.q = get_prime(bit_size // 2)
        self.M = self.p * self.q
        self.state = random.randint(2, self.M - 1)
    
    def next(self):
        self.state = pow(self.state, 2, self.M)
        return self.state
    
    def get_bits(self, num_bits):
        result = 0
        for _ in range(num_bits):
            result = (result << 1) | (self.next() & 1)
        return result
    
    def randint(self, start, end):
        return start + self.next() % (end - start + 1)

# Użycie generatora BBS
bbs = BlumBlumShub(bit_size=128)
print([bbs.get_bits(10) for _ in range(10)])  # generuje liczby losowe z 10 bitów




