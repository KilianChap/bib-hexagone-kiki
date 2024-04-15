import json

class Livre:
    def __init__(self, auteur, titre, contenu):
        self.auteur = auteur
        self.titre = titre
        self.contenu = contenu

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        if livre.auteur and livre.titre:
            self.livres.append(livre)
            print("Livre ajouté à la bibliothèque.")
        else:
            print("Erreur: Auteur ou titre manquant.")

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:    
                self.livres.remove(livre)
                print("Livre supprimé de la bibliothèque.")
                return
        print("Erreur: Livre non trouvé dans la bibliothèque.")

    def modifier_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                nouveau_titre = input("Entrez le nouveau titre du livre : ")
                nouveau_auteur = input("Entrez le nouveau nom de l'auteur : ")
                nouveau_contenu = input("Entrez le nouveau contenu du livre : ")
                livre.titre = nouveau_titre
                livre.auteur = nouveau_auteur
                livre.contenu = nouveau_contenu
                print("Livre modifié avec succès.")
                return
        print("Erreur: Livre non trouvé dans la bibliothèque.")

    def afficher_livres(self):
        print("Livres dans la bibliothèque:")
        for livre in self.livres:
            print("- ", livre.titre, "par", livre.auteur)

    def sauvegarder_bibliotheque(self, nom_fichier):
        with open(nom_fichier, 'w') as f:
            json.dump([{'auteur': livre.auteur, 'titre': livre.titre, 'contenu': livre.contenu} for livre in self.livres], f)

def saisie_livre():
    auteur = input("Entrez le nom de l'auteur : ")
    titre = input("Entrez le titre du livre : ")
    contenu = input("Entrez le contenu du livre : ")
    return Livre(auteur, titre, contenu)

bibliotheque = Bibliotheque()

while True:
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Modifier un livre")
    print("4. Afficher les livres")
    print("5. Sauvegarder la bibliothèque en JSON")
    print("6. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        nouveau_livre = saisie_livre()
        bibliotheque.ajouter_livre(nouveau_livre)
    elif choix == "2":
        titre = input("Entrez le titre du livre à supprimer : ")
        bibliotheque.supprimer_livre(titre)
    elif choix == "3":
        titre = input("Entrez le titre du livre à modifier : ")
        bibliotheque.modifier_livre(titre)
    elif choix == "4":
        bibliotheque.afficher_livres()
    elif choix == "5":
        nom_fichier = input("Entrez le nom du fichier JSON pour sauvegarder la bibliothèque : ")
        bibliotheque.sauvegarder_bibliotheque(nom_fichier)
        print("Bibliothèque sauvegardée avec succès.")
    elif choix == "6":
        print("Merci d'avoir utilisé notre application.")
        break
    else:
        print("Choix invalide. Veuillez choisir une option valide.")
