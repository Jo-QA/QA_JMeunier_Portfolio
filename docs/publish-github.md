# Publication et maintenance GitHub

Le portfolio est publié dans le dépôt public **[Jo-QA/QA_JMeunier_Portfolio](https://github.com/Jo-QA/QA_JMeunier_Portfolio)**.

La première exécution publique du workflow GitHub Actions a réussi sur Linux en 43 secondes : [consulter l’exécution 38882835172](https://github.com/Jo-QA/QA_JMeunier_Portfolio/actions/runs/38882835172). Le badge du README reflète le dernier état du workflow.

## Mettre à jour le dépôt

Dans le dossier contenant `README.md` :

```powershell
git status --short
git add .
git commit -m "Describe the change"
git push
```

Avant chaque publication, vérifier que `.env`, `.venv`, les caches navigateur et les secrets ne sont pas suivis. Les rapports livrés contiennent seulement des données publiques ou synthétiques et des chemins locaux d’exécution.

Chaque push sur `main` lance les validations, les tests unitaires et la régression Robot sur Chrome headless. Le résultat détaillé et l’artefact de rapports se trouvent dans l’onglet **Actions** du dépôt. Un échec doit être analysé avant de présenter le badge comme preuve de fonctionnement.

Jenkins et Jira/Xray sont des démonstrations d’intégration préparées. Leur mise en service n’est pas indispensable pour montrer le portfolio ; elle demande des instances et droits réels. Le dépôt ne prétend pas démontrer une exploitation de ces services en production.
