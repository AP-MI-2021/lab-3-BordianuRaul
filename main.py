import math


def citire_lista():
    """
    Citeste elemente unei liste
    :return: lista cu elementele citite
    """

    string_lst = input("Introduce-ti elementele separate prin spatiu: ")
    string_elemente = string_lst.split(sep=" ")
    result_lst = []
    for element in string_elemente:
        result_lst.append(int(element))
    return result_lst


def get_longest_all_not_prime(lst: list[int]) -> list[int]:
    """
    Afla cea mai lunga secventa de numere neprime din lista transmisa ca parametru
    :param lst: lista de elemente
    :return: cea mai lunga secventa de numere neprime din lst
    """
    lista_secvente = []

    for start in range(0, len(lst)+1):
        for stop in range(start+1, len(lst)+1):
            if is_all_not_prime(lst[start:stop]):
                lista_secvente.append(lst[start:stop])
    secventa_max = []
    for secventa in lista_secvente:
        if len(secventa) > len(secventa_max):
            secventa_max = secventa

    return secventa_max


def is_all_not_prime(sec):
    """
    Verifica daca o secventa este alcatuita doar din numere prime
    :param sec: secventa de lista
    :return: True sau False
    """
    for element in sec:
        if not is_not_prime(element):
            return False
    return True


def is_not_prime(n):
    """
    Verifica daca un numar este neprim sau nu
    :param n: numarul care va fi verificat
    :return: True sau False
    """
    if n == 2:
        return False
    elif n % 2 == 0 or n == 1:
        return True
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return True
    return False


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([2, 10, 12, 15, 20, 21, 7, 8, 10, 12, 7]) ==  \
        ([10, 12, 15, 20, 21])
    assert get_longest_all_not_prime([4, 10, 12, 15, 20, 21, 7, 8, 7, 121, 12, 7]) ==  \
        ([4, 10, 12, 15, 20, 21])
    assert get_longest_all_not_prime([2, 10, 3, 4, 5, 6, 7, 8, 11, 20, 13]) ==  \
        ([10])


def get_longest_average_below(lst: list[int], average: float) -> list[int]:
    """
    Afiseaza cea mai lunga secventa de elemente a caror medie nu depaseste o anumita valoare
    :param lst: lista de elemente
    :param average: valoarea care nu trebuie depasita
    :return: secventa de elemente maxima
    """
    lista_secvente = []

    for start in range(0, len(lst)+1):
        for stop in range(start+1, len(lst)+1):
            if is_smaller_than_average(lst[start:stop], average):
                lista_secvente.append(lst[start:stop])

    secventa_max = []

    for secventa in lista_secvente:
        if len(secventa) > len(secventa_max):
            secventa_max = secventa
    return secventa_max


def is_smaller_than_average(sec, average):
    """
    Verifica daca media elementelor unei liste este mai mare sau mai mica
    decat a unei valori transmise ca parametru
    :param sec: lista de elemente
    :param average: valoarea care nu trebuie depasita
    :return: True sau False
    """
    s = 0

    for element in sec:
        s = s + element

    media = s/len(sec)

    if media > average:
        return False
    else:
        return True


def test_get_longest_average_below():
    assert get_longest_average_below([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3.7) == \
            [1, 2, 3, 4, 5, 6]

    assert get_longest_average_below([10, 2, 7, 12, 30, 21, 2], 7) == [10, 2, 7]

    assert get_longest_average_below([20, 15, 10, 5, 1], 3) ==  \
        [5, 1]


def main():

    while True:
        print("1.Cea mai lunga secventa de elemente neprime dintr-o lista \n"
              "2.Cea mai lunga secventa de elemente ale caror medie nu depaseste o valoare citita \n"
              "x. Iesire din program")

        optiune = input("Selectati optiunea: ")

        if optiune == '1':
            lista = citire_lista()
            print(get_longest_all_not_prime(lista))

        elif optiune == '2':
            lista = citire_lista()
            average = float(input("Introduceti valoarea care nu trebuie depasita: "))
            print(get_longest_average_below(lista, average))

        elif optiune == 'x':
            break

        else:
            print("Optiune invalida!")


test_get_longest_all_not_prime()
test_get_longest_average_below()
main()
