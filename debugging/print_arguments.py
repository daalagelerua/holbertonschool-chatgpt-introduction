#!/usr/bin/python3
import sys

# Message d'usage
if len(sys.argv) == 1:
	print("Usage: ./script.py <arg1> <arg2> ...")
	print("Exemple: ./script.py arg1 arg2 arg3")
	sys.exit(1)

# Affichage des arguments
print("Arguments passés au script :")
for arg in sys.argv:
	print(arg)
