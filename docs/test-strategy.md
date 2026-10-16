# Stratégie de test fondée sur les risques

## Objectif et contexte

Évaluer la fiabilité des parcours d’achat principaux d’une application web de démonstration et rendre les résultats auditables. Le livrable est une étude indépendante de portfolio, sans mission client ni recette officielle. Profil présenté : ingénieur QA freelance, certifié ISTQB Foundation selon les informations fournies, en reconversion QSE vers QA. Aucun numéro de certificat, employeur ou ancienneté QA n’est inventé.

La continuité avec le QSE est concrète : cartographie des risques, mesures de maîtrise, preuves, traitement des écarts et amélioration continue. La réussite d’une exécution n’est jamais assimilée à une garantie de qualité globale.

## Méthode de priorisation

Échelles ordinales de 1 à 5 : impact 1 = gêne mineure, 3 = parcours dégradé, 5 = intégrité d’achat ou accès compromis ; probabilité 1 = rare supposée, 3 = plausible, 5 = fréquente supposée. Ces estimations sont des hypothèses d’atelier, sans historique de production. Score = impact × probabilité. P1 : 15-25 ; P2 : 8-14 ; P3 : 1-7. Le score ordonne l’effort et ne mesure pas une probabilité statistique.

| Risque | Score | Priorité | Mesure principale |
|---|---:|---|---|
| R-01 - Accès incorrect ou session non révoquée | 15 | P1 | Connexion, erreurs, déconnexion, accès direct |
| R-02 - Panier, produits ou montants incohérents | 20 | P1 | Contrôles des lignes, badge, prix et calculs indépendants |
| R-03 - Perte du panier pendant la navigation | 12 | P2 | Rechargement dans la même session et retour au catalogue |
| R-04 - Commande avec identité incomplète | 12 | P2 | Classes d’équivalence : prénom, nom, code postal absents |
| R-05 - Tri trompeur ou perte d’un produit | 6 | P3 | Ordre ascendant/descendant et conservation du multiensemble |
| R-06 - Annulation destructive ou commande involontaire | 12 | P2 | Annuler aux deux étapes et contrôler le panier |
| R-07 - Fausse confirmation ou panier non vidé | 20 | P1 | Parcours complet, confirmation, panier vide et retour catalogue |
| R-08 - Environnement instable ou résultats peu fiables | 9 | P2 | Sessions neuves, dépendances figées, preuves et code retour conservé |


La liste détaillée, les cas associés et les risques résiduels sont dans [risks.csv](risks.csv). R-08 est transversal : chaque exécution et sa preuve contribuent à sa maîtrise.

## Niveaux, techniques et automatisation

- Tests système UI en boîte noire ; contrôle indépendant des montants en Python, sans prétendre tester le serveur.
- Partition d’équivalence : utilisateur standard/verrouillé, mot de passe valide/invalide, champs obligatoires présents/absents.
- Table de décision simplifiée pour la validation d’identité : première erreur attendue selon l’ordre prénom, nom, code postal.
- Transitions : anonyme → connecté → panier → identité → récapitulatif → confirmation ; annulation et déconnexion.
- Propriétés : le tri conserve le multiensemble des prix ; panier et badge restent cohérents ; total = somme + taxe.
- Exploration distincte des cas scriptés : blancs, navigation arrière, panier vide, double clic, comptes de démonstration particuliers. Aucun résultat exploratoire n’est présumé acquis.

Douze scénarios Robot sont choisis pour les parcours à valeur et risque élevés. Les autres cas décrivent les contrôles complémentaires. Un navigateur neuf par test évite les dépendances d’ordre et les paniers hérités. `data-test` isole les sélecteurs ; attentes explicites sur les états ; aucun `Sleep`, aucun retry masquant un échec. La limite globale de 90 s borne les blocages, sans être un test de performance.

## Périmètre et limites

Dans le périmètre : connexion, catalogue fixe, tri, panier, identité, annulation, calcul de démonstration, commande simulée. Référence d’exécution initiale : Chrome sur Windows, affichage 1440 × 1000 demandé au navigateur.

Hors périmètre : charge, intrusion, scans de sécurité, paiement réel, backend/API, stock, e-mail transactionnel, conformité d’accessibilité exhaustive, compatibilité mobile et tous navigateurs. Les profils `problem_user`, `error_user`, `visual_user` et `performance_glitch_user` sont réservés à une exploration dédiée. Leur comportement particulier ne devient pas automatiquement un bug de produit.

## Critères de décision

Entrée : cible disponible, données publiques connues, version de la base identifiée, dépendances installées, contrôle statique et dry-run passants. Sortie de la campagne automatisée : 12/12 scénarios réellement passants, aucun échec inexpliqué, rapports et environnement archivés. Sortie de la campagne complète : 24 cas exécutés, oracles revus et toutes les anomalies critiques/majeures arbitrées. La livraison du portfolio n’affirme pas que cette dernière recette est achevée si des cas restent non exécutés.

Blocage : indisponibilité du site, pilote incompatible, oracle ambigu ou erreur d’infrastructure. Consigner BLOCKED/FAIL selon la cause, ne pas fabriquer de PASS. Si un test change après un échec, conserver la tentative et relancer les scénarios impactés ; une correction de bibliothèque commune justifie une nouvelle campagne complète.

Sévérité des anomalies : S1 bloque le parcours essentiel sans contournement ; S2 altère le contenu ou les montants ; S3 dégrade une fonction avec contournement ; S4 cosmétique. Priorité de correction séparée, décidée au triage selon impact, fréquence et exposition. Un environnement défaillant est un incident de test, pas une anomalie produit.
