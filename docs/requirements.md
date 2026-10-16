# Référentiel d’exigences et d’oracles

Version 1.0 - 16 octobre 2026. Il n’existe dans ce projet aucune spécification approuvée par un client ou Product Owner. **Toutes les H-xx sont des hypothèses de comportement attendu**, établies pour l’étude et soumises à validation métier dans une mission réelle. Une observation de l’application décrit l’existant ; elle ne prouve pas à elle seule que cet existant est correct.

Les identifiants restent stables entre cas, risques, tags Robot et résultats. Les données D-01 à D-03 sont définies dans le plan de test. La référence des prix et la taxe sont des oracles de démonstration susceptibles d’évoluer ; un écart appelle un triage, pas une mise à jour automatique des attendus.

| ID | Hypothèse de comportement attendu | Risque |
|---|---|---|
| H-01 | **Authentification valide.** Un compte standard actif ouvre le catalogue après connexion. | R-01 |
| H-02 | **Refus de connexion.** Un compte verrouillé ou un mot de passe erroné reste sur la connexion avec une erreur explicite. | R-01 |
| H-03 | **Champs de connexion.** Le nom utilisateur et le mot de passe sont obligatoires. | R-01 |
| H-04 | **Déconnexion.** La déconnexion ferme l’accès au catalogue ; une navigation directe ultérieure est refusée. | R-01 |
| H-05 | **Catalogue et fiche produit.** Le catalogue standard contient les six produits de référence ; nom et prix restent cohérents sur la fiche. | R-02 |
| H-06 | **Tri.** Les quatre tris réordonnent les produits sans perte ni duplication. | R-05 |
| H-07 | **Contenu du panier.** Ajout/retrait conserve les bons produits, prix, quantité unitaire et badge. | R-02 |
| H-08 | **Persistance de session.** Un rechargement conserve le panier dans la même session navigateur. | R-03 |
| H-09 | **Identité obligatoire.** Prénom, nom et code postal non vides sont requis avant le récapitulatif. | R-04 |
| H-10 | **Annulation.** Annuler avant finalisation retourne à un écran antérieur sans confirmation de commande ni perte du panier. | R-06 |
| H-11 | **Cohérence des montants.** Sous-total = somme des lignes ; taxe = 8 % arrondis au centime (HALF_UP) ; total = sous-total + taxe. | R-02 |
| H-12 | **Finalisation.** Finish affiche la confirmation et vide le panier. Le retour au catalogue reste possible. | R-07 |
| H-13 | **Navigation du panier.** Continue Shopping retourne au catalogue et conserve le panier. | R-03 |
| H-14 | **Accès direct sans session.** L’URL du catalogue sans session renvoie à la connexion avec une erreur. | R-01 |


H-11 : le taux de 8 % n’est pas présenté comme une règle fiscale réelle. Il s’agit d’un oracle inféré propre à la démonstration. Le contrôle utilise `Decimal`, une somme indépendante des lignes et un arrondi explicite. Exemple pour D-02 : 29,99 + 9,99 = 39,98 ; taxe attendue 3,20 ; total attendu 43,18 USD.

H-04 et H-14 évaluent une protection de navigation côté interface. Ils ne démontrent ni une authentification serveur sécurisée ni une résistance à une attaque. SauceDemo n’est pas un système de paiement réel.

Gestion du changement : identifier l’écart, confronter source et comportement, obtenir l’arbitrage métier, versionner l’hypothèse et les cas impactés, puis seulement modifier l’oracle et relancer la campagne.
