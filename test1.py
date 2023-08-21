import unittest
from collis import Utilisateur, Colis, Livraison

class TestLivraison(unittest.TestCase):
    def setUp(self):
        self.livraison = Livraison()

    def test_s_inscrire(self):
        self.livraison.s_inscrire("Alice", "alice@example.com", "motdepasse")
        self.assertEqual(len(self.livraison.utilisateurs), 1)
        self.assertEqual(self.livraison.utilisateurs[0].nom, "Alice")

    def test_se_connecter_valide(self):
        self.livraison.s_inscrire("Bob", "bob@example.com", "motdepasse")
        self.livraison.se_connecter("bob@example.com", "motdepasse")
        self.assertTrue(self.livraison.utilisateurs[0].connecte)

    def test_se_connecter_invalide(self):
        self.livraison.s_inscrire("Charlie", "charlie@example.com", "motdepasse")
        self.livraison.se_connecter("charlie@example.com", "mauvais_motdepasse")
        self.assertFalse(self.livraison.utilisateurs[0].connecte)

    def test_ajouter_colis(self):
        self.livraison.ajouter_colis(5.0, "Destination A")
        self.assertEqual(len(self.livraison.colis_en_attente), 1)
        self.assertEqual(self.livraison.colis_en_attente[0].poids, 5.0)

    def test_traiter_paiement_sans_connexion(self):
        self.livraison.ajouter_colis(5.0, "Destination A")
        self.livraison.traiter_paiement()
        self.assertFalse(self.livraison.colis_en_attente[0].paye)

    def test_traiter_paiement_avec_connexion(self):
        self.livraison.s_inscrire("David", "david@example.com", "motdepasse")
        self.livraison.se_connecter("david@example.com", "motdepasse")
        self.livraison.ajouter_colis(5.0, "Destination A")
        self.livraison.traiter_paiement()
        self.assertTrue(self.livraison.colis_en_attente[0].paye)

if __name__ == '__main__':
    unittest.main()
