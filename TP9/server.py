from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Simulating a database of books
books = []

class Livre:
    def __init__(self, auteur, titre, contenu):
        self.auteur = auteur
        self.titre = titre
        self.contenu = contenu

@app.route('/ajouter', methods=['POST'])
def ajouter_livre():
    data = request.get_json()
    livre = Livre(**data)
    books.append(livre)
    return jsonify({'message': 'Livre ajouté avec succès'}), 201

@app.route('/supprimer', methods=['DELETE'])
def supprimer_livre():
    titre = request.get_json().get('titre')
    global books
    books = [book for book in books if book.titre != titre]
    return jsonify({'message': 'Livre supprimé avec succès'}), 200

@app.route('/mettre_a_jour', methods=['PUT'])
def mettre_a_jour_livre():
    data = request.get_json()
    titre = data.get('titre')
    nouveau_auteur = data.get('nouveau_auteur')
    nouveau_contenu = data.get('nouveau_contenu')
    for book in books:
        if book.titre == titre:
            book.auteur = nouveau_auteur
            book.contenu = nouveau_contenu
            return jsonify({'message': 'Livre mis à jour avec succès'}), 200
    return jsonify({'message': 'Livre non trouvé'}), 404

@app.route('/afficher', methods=['GET'])
def afficher_livres():
    response = [{'auteur': book.auteur, 'titre': book.titre, 'contenu': book.contenu} for book in books]
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
