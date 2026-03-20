class Animal:  # com construtor e método
    def __init__(self, nom: str, poids: float, taille: float): 
        self._nom = nom
        self.poids = poids      # usa o setter
        self.taille = taille    # usa o setter

    # --- GETTERS ---
    @property
    def nom(self):
        return self._nom

    @property
    def poids(self):
        return self._poids

    @property
    def taille(self):
        return self._taille

    # --- SETTERS ---
    @poids.setter
    def poids(self, valeur):
        if valeur < 0:
            raise ValueError("O peso não pode ser negativo.")
        self._poids = valeur

    @taille.setter
    def taille(self, valeur):
        if valeur < 0:
            raise ValueError("A taille não pode ser negativa.")
        self._taille = valeur

    # --- MÉTODO ---
    def se_deplacer(self):
        self.vitesse = self.taille / 2
        print(self.taille)

    # --- __STR__ --- # Também é um método
    def __str__(self):
        return f"Animal: {self.nom}, poids: {self.poids} kg, taille: {self.taille} cm"

class Souris(Animal):
    def se_deplacer(self):
        print("Je cours très vite")


class Serpent(Animal): 
    def se_deplacer(self):
        print("Je rampe")


class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: float, altitude_max: float):
        super().__init__(nom, poids, taille)
        self.altitude_max = altitude_max

    def se_deplacer(self):
        print("Je vole")


class Veterinaire:
    def __init__(self, nom: str):
        self.nom = nom

    def examiner(self, animal: Animal):
        print(f"{self.nom} examine {animal.nom}.")
        print(f"Poids : {animal.poids} kg")
        print(f"Taille : {animal.taille} cm")

    def peser(self, animal: Animal, nouveau_poids: float):
        print(f"{self.nom} pèse {animal.nom}.")
        animal.poids = nouveau_poids
        print(f"Nouveau poids enregistré : {animal.poids} kg")

    def mesurer(self, animal: Animal, nouvelle_taille: float):
        print(f"{self.nom} mesure {animal.nom}.")
        animal.taille = nouvelle_taille
        print(f"Nouvelle taille enregistrée : {animal.taille} cm")

    def traiter(self, animal: Animal):
        print(f"{self.nom} traite {animal.nom}.")
        print(f"{animal.nom} est en train de se rétablir.")


class Zoo:  # associação: Zoo contém animais
    def __init__(self, animaux: list):
        self.animaux = animaux

    def ajouter_animal(self, animal: Animal): # Também é um método
        self.animaux.append(animal)

# --------- SOBRECARGA DO OPERADOR + NA CLASSE ZOO ---------

    def __add__(self, autre_zoo): # Somar dois zoos 
        nouvelle_liste = self.animaux + autre_zoo.animaux
        return Zoo(nouvelle_liste)
    
    def __str__(self):
        if not self.animaux:
            return "Zoo vide."
        
        liste_animaux = "\n".join(f" - {animal.nom}" for animal in self.animaux)
        return f"Zoo avec {len(self.animaux)} animaux:\n{liste_animaux}"
    
# --------- FILTRAR ANIMAIS POR TIPO ---------

    def filtrer_par_type(self, type_animal):
        return [animal for animal in self.animaux if isinstance(animal, type_animal)]
    

# --------- PROGRAMA PRINCIPAL ---------

souris_verte = Souris(nom='Stewart', poids=0.005, taille=10.0)
python_royal = Serpent(nom='Kaa', poids=12.0, taille=150.0)
aigle = Oiseau(nom='Eagle', poids=5.0, taille=80.0, altitude_max=3000.0)

print(souris_verte)
print(python_royal)
print(aigle)

python_royal.se_deplacer()
aigle.se_deplacer()

mon_zoo = Zoo(animaux=[souris_verte, python_royal])
mon_zoo.ajouter_animal(aigle)

zoo1 = Zoo([souris_verte])
zoo2 = Zoo([python_royal, aigle])

zoo3 = zoo1 + zoo2

print("Animais do zoo3.")
for animal in zoo3.animaux:
    print(animal)

print(mon_zoo)
print(zoo3)

serpentes = mon_zoo.filtrer_par_type(Serpent)
for s in serpentes:
    print("Serpentes:", s.nom)

aves = mon_zoo.filtrer_par_type(Oiseau)
for a in aves:
    print("Aves:", a.nom)

camundongos = mon_zoo.filtrer_par_type(Souris)
for c in camundongos:
    print("Roedores:", c.nom)

vet = Veterinaire("Dr. Patrice")

print("\n--- Consultation Veterinaire ---")
vet.examiner(aigle)
vet.peser(aigle, 6.0)
vet.mesurer(souris_verte, 12.0)
vet.traiter(python_royal)

def menu(zoo, vet):
    continuer = True

    while continuer:
        print("\n--- MENU DU ZOO ---")
        print("1. Voir tous les animaux")
        print("2. Filtrer par type")
        print("3. Ajouter un animal")
        print("4. Consulter le vétérinaire")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            print(zoo)

        elif choix == "2":
            print("\n--- FILTRER PAR TYPE ---")
            print("1. Serpents")
            print("2. Oiseaux")
            print("3. Souris")
            type_choisi = input("Choisissez le type : ")

            if type_choisi == "1":
                animaux = zoo.filtrer_par_type(Serpent)
            elif type_choisi == "2":
                animaux = zoo.filtrer_par_type(Oiseau)
            elif type_choisi == "3":
                animaux = zoo.filtrer_par_type(Souris)
            else:
                print("Type invalide.")
                continue

            print("\n--- RÉSULTATS ---")
            for a in animaux:
                print(a)

        elif choix == "3":
            print("\n--- AJOUTER UN ANIMAL ---")
            nom = input("Nom de l'animal : ")
            poids = float(input("Poids : "))
            taille = float(input("Taille : "))
            nouvel_animal = Animal(nom, poids, taille)
            zoo.ajouter_animal(nouvel_animal)
            print("Animal ajouté avec succès !")

        elif choix == "4":
            print("\n--- CONSULTATION VÉTÉRINAIRE ---")
            for i, animal in enumerate(zoo.animaux):
                print(f"{i+1}. {animal.nom}")

            idx = int(input("Choisissez un animal : ")) - 1
            animal = zoo.animaux[idx]

            print("\n1. Examiner")
            print("2. Peser")
            print("3. Mesurer")
            print("4. Traiter")
            action = input("Choisissez une action : ")

            if action == "1":
                vet.examiner(animal)
            elif action == "2":
                nouveau_poids = float(input("Nouveau poids : "))
                vet.peser(animal, nouveau_poids)
            elif action == "3":
                nouvelle_taille = float(input("Nouvelle taille : "))
                vet.mesurer(animal, nouvelle_taille)
            elif action == "4":
                vet.traiter(animal)
            else:
                print("Action invalide.")

        elif choix == "5":
            print("Au revoir !")
            continuer = False   # <-- sem break

        else:
            print("Option invalide.")