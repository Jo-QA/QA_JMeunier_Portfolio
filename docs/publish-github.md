# Publication du dépôt QA-Portfolio-SauceDemo

Le dépôt complet est livré localement. Aucun dépôt distant n’a été créé et aucune exécution GitHub Actions/Jenkins n’est annoncée. Aucun connecteur GitHub authentifié ni CLI `gh` n’était disponible dans l’environnement de réalisation. L’état d’une éventuelle session GitHub du navigateur n’a pas été exploité.

## Procédure précise

1. Décompresser l’archive ; ouvrir un terminal dans `QA-Portfolio-SauceDemo` (le dossier contenant README.md).
2. Sur GitHub, créer un dépôt nommé **QA-Portfolio-SauceDemo**, visibilité **Public**, sans ajouter de README, licence ou .gitignore. Description proposée : `Portfolio QA indépendant : analyse des risques, 24 cas, Robot Framework/Selenium, POM et preuves réelles sur SauceDemo.`
3. Copier son URL HTTPS. Exécuter les commandes ci-dessous. Remplacer uniquement l’URL par celle copiée ; aucune identité n’est préremplie.

```powershell
git init -b main
git add .
git status --short
git commit -m "Publish independent SauceDemo QA portfolio"
git remote add origin URL_HTTPS_COPIEE_DE_GITHUB
git push -u origin main
```

Le dossier du projet s’utilise sans historique Git préexistant ; si Git signale une identité manquante, configurer `git config user.name` et `git config user.email` avec les vraies valeurs, idéalement une adresse GitHub noreply. Ne jamais coller de token dans l’URL.

4. Ouvrir Actions : le premier push lance la suite. Vérifier le résultat puis télécharger l’artefact ; comparer l’environnement Linux à la preuve Windows. Si une politique du compte exige une approbation, l’appliquer avant publication/exécution. Ne pas annoncer la CI comme validée avant ce premier résultat.
5. Ajouter le dépôt à la sélection de profil GitHub et partager son lien. Les captures et le PDF sont déjà inclus. Aucun hébergement de site web n’est requis.

Avant le push, `git status --short` doit montrer uniquement les livrables : pas de `.env`, `.venv`, cache navigateur ou vrais secrets. Les rapports livrés contiennent seulement des données publiques/synthétiques et des chemins locaux d’exécution ; ces chemins ne sont pas des coordonnées client.

Jenkins et Jira/Xray sont des démonstrations d’intégration préparées. Leur mise en service n’est pas indispensable pour montrer le portfolio ; elle demande vos instances et droits réels. Le dépôt ne prétend pas démontrer une exploitation de ces services en production.
