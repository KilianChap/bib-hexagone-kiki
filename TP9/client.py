import requests

class Livre:
    def __init__(self, auteur, titre, contenu):
        self.auteur = auteur
        self.titre = titre
        self.contenu = contenu

def main():
    server_ip = input("Entrez l'adresse IP du serveur : ")
    server_port = int(input("Entrez le numéro de port du serveur : "))
    base_url = f'http://{server_ip}:{server_port}'

    while True:
        print("Que souhaitez-vous faire ?")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Mettre à jour un livre")
        print("4. Afficher les livres")
        print("5. Quitter")
        choice = input("Votre choix : ")

        if choice == '5':
            print("Déconnexion...")
            break

        if choice == '1':
            auteur = input("Entrez le nom de l'auteur : ")
            titre = input("Entrez le titre du livre : ")
            contenu = input("Entrez le contenu du livre : ")
            livre = Livre(auteur, titre, contenu)
            response = requests.post(f'{base_url}/ajouter', json=livre.__dict__)
        elif choice == '2':
            titre = input("Entrez le titre du livre à supprimer : ")
            response = requests.delete(f'{base_url}/supprimer', json={'titre': titre})
        elif choice == '3':
            titre = input("Entrez le titre du livre à mettre à jour : ")
            nouveau_auteur = input("Entrez le nouveau nom de l'auteur : ")
            nouveau_contenu = input("Entrez le nouveau contenu du livre : ")
            response = requests.put(f'{base_url}/mettre_a_jour', json={'titre': titre, 'nouveau_auteur': nouveau_auteur, 'nouveau_contenu': nouveau_contenu})
        elif choice == '4':
            response = requests.get(f'{base_url}/afficher')
        else:
            print("Choix invalide")
            continue

        print(response.json())

if __name__ == "__main__":
    main()
