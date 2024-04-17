import socket
import pickle

class Livre:
    def __init__(self, auteur, titre, contenu):
        self.auteur = auteur
        self.titre = titre
        self.contenu = contenu

def connect_to_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

def close_connection(client_socket):
    client_socket.close()

def send_request(client_socket, request):
    request = pickle.dumps(request)
    client_socket.send(request)

def receive_response(client_socket):
    response = client_socket.recv(4096)
    response = pickle.loads(response)
    return response

def main():
    server_ip = input("Entrez l'adresse IP du serveur : ")
    server_port = int(input("Entrez le numéro de port du serveur : "))

    while True:
        client_socket = connect_to_server(server_ip, server_port)
        
        print("Que souhaitez-vous faire ?")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Mettre à jour un livre")
        print("4. Afficher les livres")
        print("5. Quitter")
        choice = input("Votre choix : ")

        if choice == '5':
            print("Déconnexion...")
            close_connection(client_socket)
            break

        if choice == '1':
            auteur = input("Entrez le nom de l'auteur : ")
            titre = input("Entrez le titre du livre : ")
            contenu = input("Entrez le contenu du livre : ")
            livre = Livre(auteur, titre, contenu)
            request = {'action': 'ajouter', 'data': livre}
        elif choice == '2':
            titre = input("Entrez le titre du livre à supprimer : ")
            request = {'action': 'supprimer', 'data': titre}
        elif choice == '3':
            titre = input("Entrez le titre du livre à mettre à jour : ")
            nouveau_auteur = input("Entrez le nouveau nom de l'auteur : ")
            nouveau_contenu = input("Entrez le nouveau contenu du livre : ")
            request = {'action': 'mettre_a_jour', 'data': (titre, nouveau_auteur, nouveau_contenu)}
        elif choice == '4':
            request = {'action': 'afficher'}
        else:
            print("Choix invalide")
            close_connection(client_socket)
            continue

        send_request(client_socket, request)
        response = receive_response(client_socket)
        print(response)
        close_connection(client_socket)
        
if __name__ == "__main__":
    main()