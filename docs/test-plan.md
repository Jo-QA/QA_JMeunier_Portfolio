# Plan de test - version 1.0

## Organisation et environnement

Étude de portfolio individuelle préparée avec assistance IA. Le propriétaire du portfolio doit savoir expliquer et adapter les livrables ; cette étude ne constitue pas une expérience client. Rôles à prévoir en mission : QA (conception/exécution), PO (validation des oracles), développeur (analyse/correction), décideur livraison (risques résiduels). Ici, aucun PO ou développeur client n’a validé les résultats.

Cible principale : https://www.saucedemo.com/ ; source officielle associée : https://github.com/saucelabs/sample-app-web. Application publique évolutive, aucun hash déployé déduit de celui du dépôt source. Disponibilité et restrictions vérifiées dans [sources-and-scope.md](sources-and-scope.md).

Python 3.12, Robot Framework 7.3.2, SeleniumLibrary 6.7.1, Selenium 4.35.0 ; dépendances transitives figées dans requirements.txt. Le navigateur et le pilote sont consignés par exécution ; ils ne sont pas figés par requirements.txt. Le runner Linux CI et Jenkins ont leurs propres prérequis. La première preuve Windows ne valide pas à elle seule ces environnements.

## Données

- D-01 : identité synthétique Camille Test, code postal 75001. Aucun renseignement client.
- D-02 : Sauce Labs Backpack (29.99 USD) et Sauce Labs Bike Light (9.99 USD), quantité 1 chacun.
- D-03 : catalogue de référence standard : Backpack 29.99 ; Bike Light 9.99 ; Bolt T-Shirt 15.99 ; Fleece Jacket 49.99 ; Onesie 7.99 ; Test.allTheThings() T-Shirt (Red) 15.99 USD. Noms complets visibles dans le catalogue.
- Comptes : standard_user, locked_out_user ; mot de passe public affiché par le site. Mauvais mot de passe : invalid-demo-password.

Les prix sont des données de référence datées. Un changement exige une revue du référentiel, sans adapter mécaniquement les assertions pour obtenir du vert.

## Préparation, exécution et clôture

1. Installer les dépendances figées et vérifier l’environnement ; conserver la cible, la date et les versions.
2. Vérifier la disponibilité par une ouverture normale. En cas d’échec, distinguer DNS, pilote, navigation et erreur applicative.
3. Lancer C-01 puis C-02 ; inspecter les journaux, captures et codes retour. Aucun retry implicite.
4. Exécuter C-03 avec la grille de 24 cas, en enregistrant observé, attendu, statut, date et preuve. Un cas non lancé reste NOT RUN.
5. Effectuer C-04 si utile, avec charte et durée bornée. Enregistrer les observations et les questions métier.
6. Triage : reproduire, contrôler l’oracle, classer produit / démo intentionnelle / incident de test / question. Créer un ticket produit uniquement pour un écart réellement observé et qualifié.
7. Restituer les taux avec leur dénominateur, les limites et les risques résiduels. Décision de livraison explicitement séparée des résultats techniques.

Estimations initiales, non mesurées : préparation 30 min, revue des 12 cas manuels 45-60 min, exploration 30 min. Le temps effectif de la campagne Robot est issu de son XML. Les critères d’entrée/sortie et la sévérité sont définis dans la stratégie.

## Sécurité des données et conservation

Variables d’environnement pour la configuration ; aucun vrai secret dans le dépôt ; `.env` ignoré et non chargé automatiquement. `Input Password` masque les saisies dans les logs SeleniumLibrary ; les arguments des mots-clés de niveau supérieur et les captures peuvent cependant exposer des données de démonstration. Cette suite est limitée au site public/local et ne doit pas être employée telle quelle avec des comptes privés.

Les artefacts CI sont conservés 14 jours ; les preuves initiales sont versionnées pour la démonstration. Avant de publier de futures preuves, vérifier les données et les chemins. Les captures attestent seulement l’écran à un instant ; elles ne remplacent pas les assertions et le journal.
