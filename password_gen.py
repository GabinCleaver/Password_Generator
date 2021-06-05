import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = int(input("Entrez la taille du mot de passe: "))

password = "".join(random.sample(total, length))

print("Voici le mot de passe généré: " + password)