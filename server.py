import socket
import pickle

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
            return "Livre ajouté à la bibliothèque."
        else:
            return "Erreur: Auteur ou titre manquant."

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                return "Livre supprimé de la bibliothèque."
        return "Erreur: Livre non trouvé dans la bibliothèque."

    def afficher_livres(self):
        livres_list = []
        for livre in self.livres:
            livres_list.append((livre.auteur, livre.titre, livre.contenu))
        return livres_list

    def mettre_a_jour_livre(self, titre, nouveau_auteur, nouveau_contenu):
        for livre in self.livres:
            if livre.titre == titre:
                livre.auteur = nouveau_auteur
                livre.contenu = nouveau_contenu
                return "Informations mises à jour pour le livre " + titre
        return "Erreur: Livre non trouvé dans la bibliothèque."

# Création de la bibliothèque
bibliotheque = Bibliotheque()

# Mise en place du serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(5)

print("Serveur en attente de connexions...")

while True:
    client_socket, addr = server_socket.accept()
    print("Connexion établie avec", addr)

    # Réception de la demande du client
    request = client_socket.recv(1024)
    request = pickle.loads(request)

    if request['action'] == 'ajouter':
        response = bibliotheque.ajouter_livre(request['data'])
    elif request['action'] == 'supprimer':
        response = bibliotheque.supprimer_livre(request['data'])
    elif request['action'] == 'afficher':
        response = bibliotheque.afficher_livres()
    elif request['action'] == 'mettre_a_jour':
        response = bibliotheque.mettre_a_jour_livre(request['data'][0], request['data'][1], request['data'][2])
    else:
        response = "Action non valide"

    # Envoi de la réponse au client
    response = pickle.dumps(response)
    client_socket.send(response)

    client_socket.close()