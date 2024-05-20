from bbsgen import BlumBlumShub

""" Dla generatora BBS - wersja starsza na bitach """
def parking_lot_test_bbs(generator, num_cars=1200, lot_size=100):
    parked = [0] * lot_size  # Lista parkingów, 0 oznacza wolne miejsce
    success = 0

    for _ in range(num_cars):
        spot = generator.get_bit()  # Załóżmy, że otrzymujemy bit na bit od generatora BBS
        for _ in range(lot_size):
            if parked[spot] == 0:  # Sprawdzenie czy miejsce jest wolne
                parked[spot] = 1  # Parkowanie samochodu
                success += 1
                break
            spot = (spot + 1) % lot_size  # Przejście do następnego miejsca

    return success

""" Dla generatora BBS - wersja lepsza """
def parking_lot_test(generator, num_cars=1200, lot_size=100):
    parked = [0] * lot_size
    for _ in range(num_cars):
        spot = generator.randint(0, lot_size - 1)
        print(f"Random spot: {spot}")
        parked[spot] += 1
    return parked


from scipy.stats import chisquare

def chi_square_test(parked_results):
    num_cars=1200
    lot_size=100
    expected = [num_cars / lot_size] * lot_size
    chi2_stat, p_value = chisquare(parked_results, f_exp=expected)
    return chi2_stat, p_value

def run():
    bbs = BlumBlumShub(bit_size=512)
    parked_results = parking_lot_test(bbs)
    chi2_stat, p_value = chi_square_test(parked_results)
    
    print(f"Results of parking: {parked_results}")
    print(f"Sum of parked places:", sum(parked_results))  # Kontrola sum
    print(f"Chi-squared statistic: {chi2_stat}, p-value: {p_value}")
    if p_value < 0.05:
        print("Reject the null hypothesis: The distribution of parking is not uniform.")
    else:
        print("Do not reject the null hypothesis: The distribution of parking is uniform.")

if __name__ == '__main__':
    run()
