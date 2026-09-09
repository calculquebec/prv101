Architecture et interface graphique
===================================

`English <../en/2-architecture.html>`__

Architecture parallèle distribuée
---------------------------------

ParaView comprend trois composants logiques qui sont intégrés dans une même
application à utiliser sur un ordinateur personnel, mais qui peuvent également
s'exécuter séparément sur des machines différentes :

- **Serveur de données** -- composant responsable de la lecture, du filtrage et
  de l'écriture des données. Tous les objets du pipeline visibles dans
  l'explorateur de pipelines sont contenus dans le serveur de données.
  Ce serveur peut être exécuté en parallèle.
- **Serveur de rendu** -- composant responsable du rendu. Le serveur de rendu
  peut également être parallèle.
- **Client** -- composant responsable de la visualisation. Le client contrôle
  la création, l'exécution et la destruction des objets sur les serveurs, mais
  ne contient aucune donnée, ce qui permet aux serveurs de prendre toute la
  charge. Si une interface graphique est présente, elle se trouve également du
  côté client. Le client est toujours une application séquentielle.
