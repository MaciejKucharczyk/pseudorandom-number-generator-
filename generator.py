class LinearCongruentialGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        """Generuje kolejną liczbę pseudolosową."""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def randint(self, start, end):
        """Generuje losową liczbę w zadanym zakresie."""
        return start + self.next() % (end - start + 1)

    def generate_numbers(self, n):
        """Generuje listę n liczb pseudolosowych."""
        return [self.next() for _ in range(n)]
    
def run2():
    from scipy.stats import chisquare
    # Inicjalizacja generatora z ziarnem
    lcg = LinearCongruentialGenerator(seed=42)
    probes = int(input("Wprowdz liczbe probek: "))
    # Generowanie 10,000 liczb
    random_data = lcg.generate_numbers(probes)
    
    print(random_data)

# nie uzywane, stara wersja
def parking_lot_test_linear_old(generator, num_cars=1200, lot_size=100):
    parked = [0] * lot_size  # Lista miejsc parkingowych, 0 oznacza wolne miejsce
    success = 0

    for _ in range(num_cars):
        spot = generator.randint(0, lot_size - 1)
        if parked[spot] == 0:  # Sprawdzenie, czy miejsce jest wolne
            print(f"Random spot: {spot}")
            parked[spot] = 1  # Parkowanie samochodu
            success += 1

    return [success, parked]

def parking_lot_test_linear(generator, num_cars=1200, lot_size=100):
    parked = [0] * lot_size
    for _ in range(num_cars):
        spot = generator.randint(0, lot_size - 1)
        print(f"Random spot: {spot}")
        parked[spot] += 1
    return ["pusto", parked]

def test_generator():
    generator = LinearCongruentialGenerator(seed=42)
    numbers = generator.generate_numbers(100)
    print(numbers)

def run():
    generator = LinearCongruentialGenerator(seed=42)
    successes, parked = parking_lot_test_linear(generator)
    print(f"Number of cars successfully parked: {successes} out of 1200 attempts")
    
    from scipy.stats import chisquare
    """ test na success"""
    # Inicjalizacja generatora z ziarnem
    lcg = LinearCongruentialGenerator(seed=42)
    # Wykonanie testu Parking Lot
    successes, parked = parking_lot_test_linear(lcg)
    print(f"Liczba samochodów zaparkowanych pomyślnie: {successes} z 1200 prób")
    print(f"Wyniki parkowania: {parked}")
    print("Suma zaparkowanych miejsc:", sum(parked))  # Kontrola sumy
    
    """ Test statystyczny """
     # Obliczanie testu chi-kwadrat
    num_cars=1200
    lot_size=100
    expected = [num_cars / lot_size] * lot_size
    chi2_stat, p_value = chisquare(parked, f_exp=expected)

    print(f"Statystyka chi-kwadrat: {chi2_stat}")
    print(f"Wartość p: {p_value}")
    if p_value < 0.05:
        print("Odrzucamy hipotezę zerową: rozkład parkowania nie jest równomierny.")
    else:
        print("Nie ma podstaw do odrzucenia hipotezy zerowej: rozkład parkowania jest równomierny.")
    

if __name__ == '__main__':
    test_generator()
    run()
    
    
