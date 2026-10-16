# Démonstration client - 3 minutes

Ce guide est un support de présentation, pas une transcription d’une vidéo déjà enregistrée.

0:00-0:30 - Présenter le contexte : étude indépendante, certification ISTQB Foundation déclarée, transition QSE vers QA. Expliquer le lien entre analyse des risques QSE, stratégie de test et preuves.

0:30-1:10 - Ouvrir risks.csv, un cas et la matrice. Montrer comment un risque d’intégrité du panier conduit à un contrôle ciblé et à un oracle explicite. Distinguer hypothèse et exigence approuvée.

1:10-2:00 - Ouvrir tests/ui/saucedemo.robot et une page resource. Expliquer intention métier, sélecteurs stables, session neuve, attente explicite et calcul Decimal. Lancer `python scripts/run.py --suite smoke` si l’environnement est préparé ; annoncer qu’il s’agit alors d’une nouvelle exécution.

2:00-2:40 - Ouvrir evidence/2026-10-16/robot/report.html et la capture du récapitulatif. Montrer les résultats réels, l’environnement, les assertions et un lien TCxx. Ouvrir l’historique de mise au point si l’on demande comment les erreurs de test ont été traitées.

2:40-3:00 - Énoncer les limites et la suite d’une mission : valider les oracles avec le métier, compléter la campagne fonctionnelle, intégrer les vrais Tests Xray, élargir selon les risques du client.

Formulation à privilégier : « J’ai construit cette étude avec une assistance IA et je peux expliquer ses choix, ses limites et son évolution. » Ne pas la présenter comme une mission client ni comme une validation exhaustive.
