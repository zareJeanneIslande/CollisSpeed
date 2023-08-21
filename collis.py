class Utilisateur:
    def __init__(self, nom, email, mot_de_passe):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.connecte = False

class Colis:
    def __init__(self, poids, destination):
        self.poids = poids
        self.destination = destination
        self.paye = False

class Livraison:
    def __init__(self):
        self.utilisateurs = []
        self.colis_en_attente = []

    def s_inscrire(self, nom, email, mot_de_passe):
        utilisateur = Utilisateur(nom, email, mot_de_passe)
        self.utilisateurs.append(utilisateur)
        print("Inscription réussie.")

    def se_connecter(self, email, mot_de_passe):
        for utilisateur in self.utilisateurs:
            if utilisateur.email == email and utilisateur.mot_de_passe == mot_de_passe:
                utilisateur.connecte = True
                print("Connexion réussie.")
                return
        print("Identifiants incorrects.")

    def ajouter_colis(self, poids, destination):
        colis = Colis(poids, destination)
        self.colis_en_attente.append(colis)
        print("Colis ajouté avec succès.")

    def traiter_paiement(self):
        utilisateur_connecte = None
        for utilisateur in self.utilisateurs:
            if utilisateur.connecte:
                utilisateur_connecte = utilisateur
                break

        if utilisateur_connecte:
            for colis in self.colis_en_attente:
                colis.paye = True
            print("Paiement effectué pour tous les colis en attente.")
        else:
            print("Vous devez être connecté pour effectuer un paiement.")

def main():
    livraison = Livraison()

    while True:
        print("1. S'inscrire")
        print("2. Se connecter")
        print("3. Ajouter un colis")
        print("4. Traiter le paiement")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            nom = input("Entrez votre nom : ")
            email = input("Entrez votre email : ")
            mot_de_passe = input("Entrez votre mot de passe : ")
            livraison.s_inscrire(nom, email, mot_de_passe)

        elif choix == '2':
            email = input("Entrez votre email : ")
            mot_de_passe = input("Entrez votre mot de passe : ")
            livraison.se_connecter(email, mot_de_passe)

        elif choix == '3':
            poids = float(input("Entrez le poids du colis (en kg) : "))
            destination = input("Entrez la destination du colis : ")
            livraison.ajouter_colis(poids, destination)

        elif choix == '4':
            livraison.traiter_paiement()

        elif choix == '5':
            print("Merci d'utiliser notre application de livraison.")
            break

        else:
            print("Option invalide. Veuillez entrer une option valide.")

if __name__ == "__main__":
    main()
