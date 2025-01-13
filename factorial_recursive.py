#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Vérifier si un argument a été passé
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <nombre>")
        sys.exit(1)

    # Valider que l'argument est un entier positif
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Erreur : Le nombre doit être un entier positif.")
            sys.exit(1)
    except ValueError:
        print("Erreur : L'argument doit être un entier valide.")
        sys.exit(1)

    # Calculer et afficher la factorielle
    try:
        result = factorial(num)
        print(f"La factorielle de {num} est : {result}")
    except RecursionError:
        print("Erreur : Le nombre est trop grand pour être calculé avec cette méthode.")

if __name__ == "__main__":
    main()
