import unittest
from validators import calculate_compliance_score

class TestComplianceRules(unittest.TestCase):

    def test_prescription_parfaite_individuel(self):
        # RPPS valide, Signature présente
        score, alerts = calculate_compliance_score(
            prescripteur_type="INDIVIDUEL",
            has_signature=True,
            rpps="10002030405",
            finess=""
        )
        self.assertEqual(score, 100)
        self.assertEqual(len(alerts), 0)

    def test_signature_manquante(self):
        # Pénalité -40 attendue
        score, alerts = calculate_compliance_score(
            prescripteur_type="INDIVIDUEL",
            has_signature=False,
            rpps="10002030405",
            finess=""
        )
        self.assertEqual(score, 60)
        self.assertTrue(any(a['msg'] == "Signature manquante" for a in alerts))

    def test_rpps_invalide_individuel(self):
        # Pénalité -30 attendue (RPPS manquant/invalide)
        score, alerts = calculate_compliance_score(
            prescripteur_type="INDIVIDUEL",
            has_signature=True,
            rpps="12345", # Invalide
            finess=""
        )
        self.assertEqual(score, 70)
        self.assertTrue(any(a['msg'] == "RPPS manquant ou format invalide" for a in alerts))

    def test_etablissement_sans_finess(self):
        # Pas de pénalité pour structure sans FINESS si identifié comme ETABLISSEMENT
        score, alerts = calculate_compliance_score(
            prescripteur_type="ETABLISSEMENT",
            has_signature=True,
            rpps="",
            finess=""
        )
        self.assertEqual(score, 100)
        self.assertEqual(len(alerts), 0)

    def test_tout_faux(self):
        # Pas de signature (-40), Pas de RPPS (-30) -> Score 30
        # + Pas de cachet (-10) ?
        # Dans le code actuel: 
        # 1. Signature check (-40) -> 60
        # 2. RPPS check (-30) -> 30
        # 3. Cachet check (has_rpps or has_finess). Ici ni l'un ni l'autre -> -10
        # Total attendu: 20
        score, alerts = calculate_compliance_score(
            prescripteur_type="INDIVIDUEL",
            has_signature=False,
            rpps="",
            finess=""
        )
        self.assertEqual(score, 20)

if __name__ == '__main__':
    unittest.main()
