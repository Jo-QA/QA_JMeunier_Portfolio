# Historique technique de mise au point

Tentative 01 : 12 statuts FAIL, en raison principalement d’un appel à un attribut inexistant de SeleniumLibrary dans la capture de teardown ; TC06 comporte aussi un sélecteur de menu inadéquat. Les assertions métier passantes ne suffisent pas à classer le cas PASS si le teardown échoue. Les fichiers d’origine sont conservés.

Tentative 02 : 11 PASS, TC06 FAIL sur un clic visant l’image du menu, intercepté par le bouton associé. Correction avec `id:react-burger-menu-btn`.

La régression finale a été relancée intégralement et a passé les 12 cas. Aucun de ces incidents de test n’a donné lieu à un ticket produit SauceDemo. L’état courant du code correspond à la version corrigée ; ces dossiers sont une archive d’exécution, pas des suites à rejouer.

Complément 01 : 11 PASS, TC11 FAIL avec StaleElementReferenceException. Le premier tri recrée le composant React ; le protocole réutilisait l’objet Select précédent. Le sélecteur est maintenant retrouvé avant la seconde sélection. Le complément final a passé les 12 contrôles. Le protocole initial est archivé dans ce dossier ; le fichier explicitement nommé corrected-for-retest correspond à la correction suivante, pas au code exécuté lors de cette tentative.
