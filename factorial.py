#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1  # Décrémenter n pour éviter une boucle infinie
	return result

# Vérifier si un argument a été passé
if len(sys.argv) != 2:
	print("Usage: ./script.py <nombre>")
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
f = factorial(num)
print(f)
