# Matrice de traçabilité

Couverture de conception : 14/14 hypothèses disposent d’au moins un cas. Couverture automatisée : 9/14 hypothèses disposent d’un scénario Robot (64,3 %) ; 12/24 cas sont automatisés (50 %). Ces ratios mesurent la conception, pas une couverture de code ou de tous les comportements. R-08 concerne tous les cas. Les scénarios et leurs tags H-xx/R-xx sont vérifiés par `scripts/validate_portfolio.py`.

| Hypothèse | Risque | Cas conçus | Cas Robot |
|---|---|---|---|
| H-01 | R-01 | TC01 | TC01 |
| H-02 | R-01 | TC02 TC03 | TC02 TC03 |
| H-03 | R-01 | TC04 TC05 | AUCUN |
| H-04 | R-01 | TC06 | TC06 |
| H-05 | R-02 | TC07 TC08 | AUCUN |
| H-06 | R-05 | TC09 TC10 TC11 TC12 | TC09 |
| H-07 | R-02 | TC13 TC14 TC15 TC16 | TC13 TC14 TC15 |
| H-08 | R-03 | TC17 | TC17 |
| H-09 | R-04 | TC19 | TC19 |
| H-10 | R-06 | TC20 TC23 | AUCUN |
| H-11 | R-02 | TC21 | TC21 |
| H-12 | R-07 | TC22 | TC22 |
| H-13 | R-03 | TC18 | AUCUN |
| H-14 | R-01 | TC24 | AUCUN |


La liaison effective entre cas et rapport est le préfixe stable TCxx du nom de test, repris dans `execution.csv`. Les clés Jira ne sont pas inventées. Le lien avec un Test Jira doit être renseigné après création dans une instance réelle.
