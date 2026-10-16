# Registre des anomalies

**Aucun ticket de bug produit ouvert à la livraison.** Cette phrase ne certifie pas l’absence de défauts : seuls les contrôles réellement exécutés peuvent être commentés dans le bilan. Les comportements d’un compte verrouillé sont attendus, pas des bugs.

Les incidents rencontrés pendant la mise au point du harnais sont conservés dans `evidence/engineering/attempt-01` et décrits dans le bilan. Ils concernent le code de test, pas SauceDemo. Aucun résultat fictif ni ticket inventé n’est utilisé pour enrichir artificiellement le portfolio.

Le formulaire GitHub `.github/ISSUE_TEMPLATE/observed-defect.yml` est un **modèle vierge**, pas une anomalie constatée. Un futur ticket doit contenir : environnement/date, préconditions, données synthétiques, étapes minimales, attendu + oracle, observé, reproductibilité, impact, sévérité, priorité à arbitrer, cas lié et preuve. Statuts conseillés : Observé → À qualifier → Confirmé / Comportement intentionnel / Question métier / Incident de test → Corrigé → Retesté.
