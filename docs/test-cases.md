# Catalogue de 24 cas de test

Base de test v1.0 du 16 octobre 2026. Chaque cas utilise un navigateur neuf ou un état explicitement préparé. Comptes publics et données synthétiques uniquement. Les attendus reposent sur les hypothèses H-xx, sans validation métier officielle. Le statut d’exécution figure dans le bilan et non dans ce référentiel de conception. TC19 regroupe trois partitions dans un seul cas ; le décompte reste 24 cas et 12 scénarios Robot.

## TC01 - Connexion standard

- Traçabilité : H-01 / R-01 ; priorité P1 ; mode : Robot.
- Préconditions : Session neuve, page de connexion.
- Actions : Saisir standard_user et le mot de passe public ; cliquer Login.
- Résultat attendu : Le catalogue Products est visible et le formulaire de connexion est absent.

## TC02 - Compte verrouillé

- Traçabilité : H-02 / R-01 ; priorité P1 ; mode : Robot.
- Préconditions : Session neuve, page de connexion.
- Actions : Saisir locked_out_user et le mot de passe public ; cliquer Login.
- Résultat attendu : Erreur « Sorry, this user has been locked out. » ; connexion visible, catalogue absent.

## TC03 - Mot de passe erroné

- Traçabilité : H-02 / R-01 ; priorité P1 ; mode : Robot.
- Préconditions : Session neuve, page de connexion.
- Actions : Saisir standard_user / invalid-demo-password ; cliquer Login.
- Résultat attendu : Erreur « Username and password do not match any user in this service » ; pas de catalogue.

## TC04 - Nom utilisateur absent

- Traçabilité : H-03 / R-01 ; priorité P1 ; mode : manuel.
- Préconditions : Session neuve, page de connexion.
- Actions : Laisser le nom utilisateur vide ; saisir le mot de passe public ; cliquer Login.
- Résultat attendu : Erreur « Username is required » ; rester sur la connexion.

## TC05 - Mot de passe absent

- Traçabilité : H-03 / R-01 ; priorité P1 ; mode : manuel.
- Préconditions : Session neuve, page de connexion.
- Actions : Saisir standard_user ; laisser le mot de passe vide ; cliquer Login.
- Résultat attendu : Erreur « Password is required » ; rester sur la connexion.

## TC06 - Déconnexion et accès ultérieur

- Traçabilité : H-04 / R-01 ; priorité P1 ; mode : Robot.
- Préconditions : Compte standard connecté.
- Actions : Ouvrir le menu ; Logout ; tenter directement inventory.html.
- Résultat attendu : Formulaire de connexion visible après Logout et accès direct ; catalogue inaccessible.

## TC07 - Référence du catalogue

- Traçabilité : H-05 / R-02 ; priorité P1 ; mode : manuel.
- Préconditions : Compte standard connecté, tri par défaut.
- Actions : Compter les produits ; comparer les six noms et prix à D-03 ; vérifier la présence de l’image et du bouton Add to cart.
- Résultat attendu : Six produits uniques ; noms/prix conformes à D-03 ; chaque image est chargée et chaque bouton visible.

## TC08 - Fiche produit et retour

- Traçabilité : H-05 / R-02 ; priorité P1 ; mode : manuel.
- Préconditions : Compte standard connecté.
- Actions : Ouvrir Sauce Labs Backpack ; contrôler nom/prix ; cliquer Back to products.
- Résultat attendu : Nom identique, prix 29.99 USD ; retour au catalogue sans changement de panier.

## TC09 - Tri prix croissant

- Traçabilité : H-06 / R-05 ; priorité P3 ; mode : Robot.
- Préconditions : Compte standard connecté, catalogue.
- Actions : Relever les prix ; sélectionner Price (low to high) ; comparer ordre et multiensemble.
- Résultat attendu : Prix en ordre croissant, même liste avec mêmes multiplicités, au moins deux produits.

## TC10 - Tri prix décroissant

- Traçabilité : H-06 / R-05 ; priorité P3 ; mode : manuel.
- Préconditions : Compte standard connecté, catalogue.
- Actions : Relever les couples nom/prix ; sélectionner Price (high to low).
- Résultat attendu : Prix en ordre décroissant ; mêmes couples nom/prix, doublons de prix autorisés.

## TC11 - Tri nom croissant

- Traçabilité : H-06 / R-05 ; priorité P3 ; mode : manuel.
- Préconditions : Compte standard connecté, tri Z to A déjà sélectionné.
- Actions : Relever les six noms ; sélectionner Name (A to Z).
- Résultat attendu : Ordre alphabétique croissant ; mêmes noms uniques et mêmes prix.

## TC12 - Tri nom décroissant

- Traçabilité : H-06 / R-05 ; priorité P3 ; mode : manuel.
- Préconditions : Compte standard connecté, catalogue.
- Actions : Relever les six noms ; sélectionner Name (Z to A).
- Résultat attendu : Ordre alphabétique décroissant ; mêmes noms uniques et mêmes prix.

## TC13 - Ajout d’un produit

- Traçabilité : H-07 / R-02 ; priorité P1 ; mode : Robot.
- Préconditions : Compte standard connecté, panier vide.
- Actions : Ajouter Sauce Labs Backpack ; contrôler le badge ; ouvrir le panier.
- Résultat attendu : Badge 1 ; une ligne Backpack, quantité 1, prix 29.99 USD.

## TC14 - Ajout de deux produits

- Traçabilité : H-07 / R-02 ; priorité P1 ; mode : Robot.
- Préconditions : Compte standard connecté, panier vide.
- Actions : Ajouter Backpack puis Bike Light ; ouvrir le panier.
- Résultat attendu : Badge 2 ; exactement les deux produits, quantité 1 pour chacun.

## TC15 - Retrait depuis le panier

- Traçabilité : H-07 / R-02 ; priorité P1 ; mode : Robot.
- Préconditions : Panier contenant Backpack et Bike Light.
- Actions : Dans le panier, cliquer Remove sur Backpack.
- Résultat attendu : Badge 1 ; seule Bike Light reste, quantité 1 ; Backpack absent.

## TC16 - Retrait du dernier produit depuis le catalogue

- Traçabilité : H-07 / R-02 ; priorité P1 ; mode : manuel.
- Préconditions : Compte standard connecté, Backpack seul dans le panier.
- Actions : Depuis le catalogue cliquer Remove sur Backpack ; ouvrir le panier.
- Résultat attendu : Badge absent ; bouton Add to cart restauré ; aucune ligne dans le panier.

## TC17 - Panier après rechargement

- Traçabilité : H-08 / R-03 ; priorité P2 ; mode : Robot.
- Préconditions : Compte standard connecté, Backpack dans le panier.
- Actions : Ouvrir le panier ; recharger la page dans la même session.
- Résultat attendu : Backpack reste présent avec quantité 1 ; badge 1.

## TC18 - Continuer les achats

- Traçabilité : H-13 / R-03 ; priorité P2 ; mode : manuel.
- Préconditions : Compte standard connecté, Backpack dans le panier.
- Actions : Dans le panier cliquer Continue Shopping ; retourner au panier.
- Résultat attendu : Catalogue puis panier accessibles ; Backpack conservé et badge 1.

## TC19 - Identité obligatoire - trois partitions

- Traçabilité : H-09 / R-04 ; priorité P2 ; mode : Robot.
- Préconditions : Compte standard connecté, Backpack dans le panier, Checkout ouvert.
- Actions : Continuer avec trois champs vides ; puis prénom seul ; puis prénom et nom sans code postal.
- Résultat attendu : Erreurs successives First Name is required / Last Name is required / Postal Code is required ; pas de récapitulatif.

## TC20 - Annulation de l’identité

- Traçabilité : H-10 / R-06 ; priorité P2 ; mode : manuel.
- Préconditions : Compte standard connecté, Backpack dans le panier, Checkout ouvert.
- Actions : Saisir D-01 ; cliquer Cancel avant Continue.
- Résultat attendu : Retour au panier ; Backpack et badge 1 conservés ; aucune confirmation.

## TC21 - Intégrité du récapitulatif et montants

- Traçabilité : H-11 / R-02 ; priorité P1 ; mode : Robot.
- Préconditions : Panier D-02, identité D-01.
- Actions : Continuer jusqu’au récapitulatif ; contrôler les lignes et calculer les montants indépendamment.
- Résultat attendu : Backpack + Bike Light, quantité 1 ; sous-total 39.98, taxe 3.20, total 43.18 USD selon H-11.

## TC22 - Commande simulée complète

- Traçabilité : H-12 / R-07 ; priorité P1 ; mode : Robot.
- Préconditions : Compte standard connecté, Backpack dans le panier, identité D-01.
- Actions : Checkout ; Continue ; Finish ; contrôler confirmation ; Back Home ; ouvrir le panier.
- Résultat attendu : « Thank you for your order! » ; badge absent ; catalogue accessible puis panier vide.

## TC23 - Annulation du récapitulatif

- Traçabilité : H-10 / R-06 ; priorité P2 ; mode : manuel.
- Préconditions : Compte standard connecté, Backpack au récapitulatif.
- Actions : Cliquer Cancel ; ouvrir le panier depuis le catalogue.
- Résultat attendu : Retour au catalogue ; Backpack et badge 1 conservés ; aucune confirmation.

## TC24 - Accès direct sans connexion

- Traçabilité : H-14 / R-01 ; priorité P1 ; mode : manuel.
- Préconditions : Session entièrement neuve, aucune connexion.
- Actions : Ouvrir directement https://www.saucedemo.com/inventory.html.
- Résultat attendu : Retour à la connexion, message demandant la connexion ; catalogue inaccessible.

