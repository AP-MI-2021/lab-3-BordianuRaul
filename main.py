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


def main():

    while True:
        print("1.Cea mai lunga secventa de elemente neprime dintr-o lista \n"
              "x. Iesire din program")
        optiune = input("Selectati optiunea: ")
        if optiune == '1':
            lista = citire_lista()
            print(get_longest_all_not_prime(lista))
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida!")


test_get_longest_all_not_prime()
main()
