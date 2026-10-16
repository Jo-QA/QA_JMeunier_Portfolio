# Preuves d’exécution

Les fichiers des dossiers datés proviennent d’exécutions réelles. Le dry-run de validation est conservé séparément pendant la réalisation et n’est pas présenté comme preuve de fonctionnement UI.

- `2026-10-16/robot/` : régression finale de 12 scénarios maintenus ; XML natif, HTML, xUnit, CSV, environnement et 13 captures. `order-complete.png` est prise au moment de la confirmation ; TC22.png montre le panier vide après retour.
- `2026-10-16/complementary/` : 12 autres cas vérifiés par un protocole ponctuel assisté Selenium ; JSON/CSV, protocole exact et une capture par cas. Il s’agit de contrôles exécutables, pas d’une recette humaine. Le protocole est archivé comme preuve et ne remplace pas la suite Robot maintenue.
- `engineering/attempt-01/` et `attempt-02/` : tentatives de mise au point ayant échoué sur le code de test ; conservées pour la transparence. Le bilan distingue leur cause des résultats finaux.
- `engineering/complementary-attempt-01/` : première vérification complémentaire, 11/12 PASS et une référence Selenium périmée sur TC11 ; incident corrigé dans le protocole final.

Les images ont été produites par le navigateur de test, sans montage. Les XML/HTML d’origine ne sont pas réécrits pour cacher des échecs. Les rapports peuvent contenir des chemins locaux de réalisation et des comptes publics de démo ; aucun compte client ni donnée personnelle de test n’a été utilisé.

`MANIFEST.sha256` à la racine recense les empreintes des fichiers livrés (sauf lui-même et métadonnées Git). Il permet de détecter une modification après livraison ; ce n’est pas une signature de certification.
