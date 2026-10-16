# Architecture et décisions

```text
tests/ui/                 intentions métier et assertions de parcours
resources/common.resource cycle de vie et composition des pages
resources/pages/          Page Objects : connexion, catalogue, panier, checkout
libraries/                Python : navigateur isolé, calcul Decimal, métadonnées
variables/                configuration validée issue de l’environnement
scripts/                  lancement, validation, synthèse factuelle
docs/                     exigences, risques, conception, campagnes et bilan
integrations/xray/        CSV et mapping préparés
evidence/                 preuves figées datées, jamais remplacées par un dry-run
results/                  nouvelles exécutions locales, ignorées par Git
```

1. POM en resource files : les pages possèdent les sélecteurs et les actions. Les tests expriment le comportement attendu ; les sélecteurs sont majoritairement des attributs `data-test`. Une bibliothèque Python limitée prend en charge les préoccupations qui gagnent à être typées. Cela évite une hiérarchie de classes Python doublant les ressources Robot.
2. Isolation par navigateur neuf : coût de démarrage accepté pour la lisibilité et l’indépendance. Pas de profil utilisateur existant, pas de test dépendant du précédent, pas de parallélisme sur la démo publique.
3. Attentes explicites et timeouts : attendre l’état visible pertinent ; aucune pause arbitraire. Un clic ou une assertion échoués arrêtent le cas ; pas de retry automatique.
4. Argent : `Decimal` et arrondi HALF_UP ; vérifier sous-total, taxe et total depuis les lignes. Le taux attendu est documenté en hypothèse, pas codé comme une règle fiscale universelle.
5. Configuration : variables d’environnement, URL restreinte à la démo/localhost ; binaire et pilote optionnels pour les environnements sans téléchargement. L’échec d’accès réseau demeure un échec visible.
6. Preuves : screenshots après assertions ou sur échec, métadonnées de navigateur, XML natif et xUnit. Le CSV de synthèse est dérivé de l’XML et requiert un fichier de métadonnées navigateur. Le lanceur refuse un dossier de sortie non vide ; il crée par défaut un dossier horodaté. Un dry-run doit toujours écrire dans un dossier distinct.
7. CI : dépendances Python figées, permission GitHub read-only, timeout, absence de secrets dans les PR, archivage même sur échec. Les trois actions GitHub sont figées sur des commits SHA vérifiés via l’API des dépôts officiels ; versions et sources dans action-pins.json. Le navigateur/runner évolue : la reproductibilité est documentée, pas hermétique.

Ajouter une page : créer une resource, l’importer dans common, exposer des actions et états, puis écrire le scénario avec identifiants TC/H/R. Après modification, lancer validation, dry-run dans un dossier distinct puis les tests réels concernés. Modifier une bibliothèque commune justifie la régression complète.
