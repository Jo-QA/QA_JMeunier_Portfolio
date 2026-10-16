# Plan de campagnes

| Campagne | Déclencheur | Sélection | Critère de sortie | Preuves |
|---|---|---|---|---|
| C-01 Smoke | Nouvelle installation ou changement d’environnement | TC01, TC06, TC13, TC14, TC21, TC22 (6) | 6 PASS réels ; sinon interrompre et diagnostiquer | Robot XML/HTML, captures, environnement |
| C-02 Régression UI | Modification de la suite, push/PR, lancement manuel | Les 12 scénarios tagués regression | 12 PASS réels et zéro échec inexpliqué | Robot, xUnit, CSV, synthèse JSON |
| C-03 Complément fonctionnel | Avant recette complète ou nouvelle version de l’application | TC04, 05, 07, 08, 10, 11, 12, 16, 18, 20, 23, 24 | Chaque cas exécuté et résultat revu ; défauts arbitrés | Grille datée, étapes, observation, preuve |
| C-04 Exploration | Après C-01 et changement de risque | Champs avec blancs, panier vide, Back, double clic, profils de démonstration particuliers | Charte close avec observations et questions ; pas de taux de couverture inventé | Notes exploratoires datées |

Exécuter `python scripts/run.py --suite smoke`, puis `--suite regression`. La campagne C-02 inclut les six cas de C-01 ; une régression complète passante fournit leurs résultats, sans prétendre qu’une campagne smoke séparée a été lancée.

Cadence proposée : CI sur push main, pull request et workflow_dispatch ; aucun cron ni charge régulière inutile sur le site public. Tests séquentiels. Un échec doit rester visible dans le code retour CI ; l’étape d’archivage s’exécute aussi en cas d’échec.

Charte C-04 : « Rechercher les chemins qui permettent de terminer une commande avec un état incohérent, en limitant l’exploration à des interactions normales sur la démo. » Durée indicative 30 min. Ne pas qualifier de défaut une attente non arbitrée ou un comportement intentionnel de démo.
