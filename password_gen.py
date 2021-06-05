import random
import string
from colorama import Fore, init

init()

try:
    total = string.ascii_letters + string.digits + string.punctuation

    length = int(input(Fore.YELLOW + "Entrez la taille du mot de passe: "))
    password = "".join(random.sample(total, length))

    print(Fore.GREEN + "Voici le mot de passe généré: " + password)
except:
    print(Fore.RED + "Erreur dans la génération du mot de passe.")
