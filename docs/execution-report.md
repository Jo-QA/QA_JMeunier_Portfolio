# Bilan d’exécution - 16 octobre 2026

**Résultat final : 24/24 cas vérifiés PASS**, avec deux modalités distinctes : 12/12 scénarios de régression Robot Framework/SeleniumLibrary, puis 12/12 contrôles complémentaires selon un protocole ponctuel assisté Selenium. Aucun cas n’a été déclaré passant sans exécution. Ces contrôles complémentaires ne sont pas une recette humaine ni une suite Robot supplémentaire.

## Environnement et disponibilité

| Élément | Constat |
|---|---|
| Cible | https://www.saucedemo.com/ |
| Disponibilité | HTTP 200, page de connexion et catalogue réellement chargés le 16 octobre 2026 |
| OS / Python | Windows / 3.12.14 |
| Navigateur | Chrome 155.0.8059.41, headless |
| Pilote | ChromeDriver 155.0.8059.84 |
| Robot / SeleniumLibrary / Selenium | 7.3.2 / 6.7.1 / 4.35.0 |
| Fenêtre demandée | 1440 × 1000 pixels ; le viewport intérieur dépend du navigateur |
| Début Robot | 2026-10-16T10:54:12.355425 (heure système Europe/Paris, UTC+02:00 ce jour) |
| Durée Robot | 42.62 secondes, tirées du statut de suite XML |
| Données | Comptes publics, identité synthétique Camille Test, code 75001 |
| Version applicative | Déploiement public non attribué à un commit précis |

## Résultats et preuves

- Suite maintenue : 12 PASS, 0 FAIL, 0 SKIP. Les six cas smoke sont inclus dans cette régression ; aucun lancement smoke séparé n’est revendiqué.
- Complément : 12 PASS, 0 FAIL, selon le protocole et les assertions archivés dans [results.json](../evidence/2026-10-16/complementary/results.json).
- Total : 24 cas exécutés sur 24 conçus ; 14 hypothèses exercées sur 14, sans validation métier officielle de ces hypothèses.
- 25 captures navigateur authentiques : 13 dans la campagne Robot, 12 dans le complément.
- Montants contrôlés avec deux articles : 39.98 USD de sous-total, 3.20 USD de taxe, 43.18 USD de total ; oracle H-11 explicitement inféré.
- Aucun ticket produit créé : aucun écart à un oracle de la base n’a été confirmé dans ces contrôles. Ce constat ne prouve pas l’absence de bugs.

Sources de vérité : [report.html](../evidence/2026-10-16/robot/report.html), [log.html](../evidence/2026-10-16/robot/log.html), [output.xml](../evidence/2026-10-16/robot/output.xml), [environment.json](../evidence/2026-10-16/robot/environment.json) et [registre par cas](case-execution-status.csv). Les horodatages natifs Robot sont ceux du système ; les métadonnées et le protocole complémentaire contiennent des horodatages UTC avec décalage explicite.

## Historique de mise au point

| Tentative | Résultat | Diagnostic et traitement |
|---|---|---|
| 01 | 0/12 PASS au statut global | L’archivage de capture utilisait un attribut inexistant de SeleniumLibrary ; la fermeture des navigateurs s’exécutait néanmoins. Le menu était aussi ciblé comme bouton sur un attribut porté par une image. Corrections du harnais, pas bugs produit. |
| 02 | 11/12 PASS | Le clic sur l’image du menu était intercepté par le vrai bouton. Remplacement par l’identifiant stable du bouton `react-burger-menu-btn`. |
| Finale | 12/12 PASS | Régression complète relancée après les corrections communes ; captures et rapports conservés. |
| Complément 01 | 11/12 PASS | Référence Selenium du sélecteur de tri conservée après un changement qui recrée le composant React. Correction : retrouver le sélecteur avant la seconde sélection. Incident de protocole, pas écart de produit. |
| Complément final | 12/12 PASS | Protocole corrigé puis contrôles complémentaires relancés, résultats et captures conservés. |

Les tentatives réelles sont dans `evidence/engineering/`. Le contrôle dry-run initial a aussi permis de corriger l’ordre de chargement du fichier de variables avant SeleniumLibrary. Les échecs de conception ne sont pas présentés comme des observations produit.

## Vérifié et non vérifié

Vérifié : disponibilité ponctuelle, 24 cas dans Chrome/Windows avec les modalités ci-dessus, installation des dépendances figées dans un second environnement virtuel vierge, cohérence des dépendances, syntaxe Robot et traçabilité. Les résultats détaillés constituent les preuves.

Contrôles internes distincts des 24 cas fonctionnels : 9 tests unitaires passants sur les oracles monétaires et la configuration. Ils vérifient notamment le rejet des montants incohérents, des monnaies mal formées et des cibles non autorisées. Les actions GitHub sont épinglées à des commits officiels vérifiés.

La syntaxe et la structure YAML du workflow et du modèle de ticket ont aussi été contrôlées. La première exécution publique GitHub Actions sur Linux a réussi en 43 secondes : [run 38882835172](https://github.com/Jo-QA/QA_JMeunier_Portfolio/actions/runs/38882835172). Les journaux du contrôle local final restent dans `evidence/2026-10-16/quality-checks/`.

Non vérifié : exécution Jenkins, import dans Jira/Xray, autre navigateur/mobile, tests de charge/sécurité, exploration hors des 24 cas et approbation métier. Les fichiers Jenkins et Xray sont préparés et inspectés, sans résultat inventé. Aucune vidéo n’a été enregistrée ; un guide de démonstration et les captures sont fournis.

Conclusion de cette étude : les contrôles définis passent dans l’environnement testé. Le portfolio est montrable en expliquant ses oracles et ses limites. Une décision de mise en production réelle demanderait un périmètre, des exigences approuvées et des critères de risque propres au client.
