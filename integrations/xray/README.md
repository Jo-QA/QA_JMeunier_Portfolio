# Jira / Xray - préparation, sans import prétendu

Ce dossier ne contient aucune clé Jira fictive ni ticket créé à distance. Le CSV décrit les 24 cas comme définitions manuelles ; douze ont aussi une implémentation Robot. Avant un import dans un vrai projet, décider si l’on maintient une définition manuelle distincte ou si les 12 Tests seront de type Robot afin d’éviter les doublons.

## Définitions des cas

Dans Xray Test Case Importer, importer `test-case-import.csv` en UTF-8, séparateur virgule, avec la première ligne comme en-tête. Sélectionner le vrai projet et mapper :

| Colonne CSV | Champ cible à choisir dans l’importeur |
|---|---|
| Test Case Identifier | Identifiant de regroupement de cas de l’importeur |
| Summary | Summary |
| Test Type | Test Type (valeur Manual à adapter à l’instance) |
| Description | Description |
| Action | Test Step / Action |
| Data | Test Step / Data |
| Expected Result | Test Step / Expected Result |

Chaque ligne est un cas comportant une étape composée ; TC19 contient trois partitions décrites dans cette étape. Vérifier l’aperçu sur un cas avant le lot. Les intitulés exacts, champs obligatoires et droits dépendent de la version Cloud/Server/DC et de la configuration du projet. Ce mapping est préparé, non testé dans une instance.

## Résultats Robot

Xray sait consommer le fichier natif `output.xml` de Robot Framework. Utiliser Import Execution Results d’une Test Execution et sélectionner Robot, en vérifiant la compatibilité du schéma Robot 7 avec la version installée. Ne pas importer le dry-run. Les balises TCxx sont des identifiants locaux, pas des clés Jira.

Pour lier un scénario à un Test Xray existant, ajouter uniquement sa vraie clé Jira aux tags Robot suivant la convention de la documentation de votre version. Sans clé, l’importeur peut créer de nouveaux Tests. Renseigner ensuite le mapping dans une copie de `test-key-mapping.csv`. Le scénario local ne doit pas être dupliqué à chaque exécution.

Les API Cloud et Server/DC et leurs mécanismes d’authentification diffèrent. Aucune clé d’API ni requête de création n’est incluse. L’intégration réelle exige une instance, des droits, des clés Test valides et une validation du mapping. Les rapports xUnit servent aussi au plugin JUnit de Jenkins.

Sources officielles consultées le 16 octobre 2026 :
- [Import Execution Results](https://docs.getxray.app/display/XRAYCLOUD/Import%2BExecution%2BResults)
- [Robot XML reports](https://getxraydocs.atlassian.net/wiki/spaces/XRAYCLOUD/pages/44564940)
