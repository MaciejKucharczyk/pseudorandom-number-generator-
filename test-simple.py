from generator import LinearCongruentialGenerator
from scipy.stats import chisquare

def chi_square_test(data):
    """Przeprowadza test chi-kwadrat na wygenerowanych danych."""
    # Obliczamy, ile razy każda liczba występuje w danych
    frequency = [0] * 1000
    for number in data:
        frequency[number] += 1
    
    # Oczekiwana liczba wystąpień każdej liczby, jeśli rozkład jest równomierny
    expected = [len(data) / 1000] * 1000
    
    # Wykonanie testu chi-kwadrat
    statistic, p_value = chisquare(frequency, f_exp=expected)
    return statistic, p_value

def parity_test(data):
    """Liczy i porównuje liczbę parzystych i nieparzystych wartości w danych."""
    even_count = sum(1 for x in data if x % 2 == 0)
    odd_count = len(data) - even_count
    return even_count, odd_count

if __name__ == "__main__":
    # Generujemy 10,000 liczb losowych
    lcg = LinearCongruentialGenerator(seed=42)
    random_data = lcg.generate_numbers(10000)

    # Przeprowadzamy test chi-kwadrat
    chi_stat, chi_p = chi_square_test(random_data)
    print(f"Chi-square test statistic: {chi_stat}, p-value: {chi_p}")

    # Przeprowadzamy test parzystości
    even_count, odd_count = parity_test(random_data)
    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
