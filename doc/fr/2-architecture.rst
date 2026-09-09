Architecture et interface graphique
===================================

`English <../en/2-architecture.html>`__

Architecture parallèle distribuée
---------------------------------

ParaView comprend trois composants logiques qui sont intégrés dans une même
application à utiliser sur un ordinateur personnel, mais qui peuvent également
s’exécuter séparément sur des machines différentes :

- **Serveur de données** -- composant responsable de la lecture, du filtrage et
  de l’écriture des données. Tous les objets du pipeline visibles dans
  l’explorateur de pipelines sont contenus dans le serveur de données.
  Ce serveur peut être exécuté en parallèle.
- **Serveur de rendu** -- composant responsable du rendu. Le serveur de rendu
  peut également être parallèle.
- **Client** -- composant responsable de la visualisation. Le client contrôle
  la création, l’exécution et la destruction des objets sur les serveurs, mais
  ne contient aucune donnée, ce qui permet aux serveurs de prendre toute la
  charge. Si une interface graphique est présente, elle se trouve également du
  côté client. Le client est toujours une application séquentielle.

Il y a deux principaux modes d’utilisation :

.. grid:: 2

    .. grid-item-card:: Mode autonome
        :columns: 5

        .. figure:: ../images/client1.png
            :width: 83%

        Les calculs et l’interface utilisateur s’exécutent sur le même
        ordinateur (local ou distant).

    .. grid-item-card:: Mode client-serveur
        :columns: 7

        .. figure:: ../images/client2.png

        Une instance parallèle de ``pvserver`` s’exécute à distance sur un
        serveur multicœur ou sur une grappe de calcul.

Or, le *mode autonome* est **limité par l’ordinateur utilisé** :

- Bande-passante de la lecture des données ;
- Mémoire système ;
- Puissance CPU / GPU.

Par exemple, **un ordinateur doté de 48 Go de mémoire** pourrait traiter des
modèles jusqu’à :math:`2048^3` valeurs, mais sous certaines conditions :

1. les valeurs sont à virgule flottante à simple précision ...
2. sur des grilles structurées ...
3. stockées localement (faible latence).

Ainsi, un tel ordinateur ne pourrait traiter :

- des données plus larges ou de plus haute résolution ;
- des grilles plus complexes ;
- des données nécessitant des filtres complexes.

Par exemple, une **simulation d’écoulement d’air autour d’une aile d’avion**
sur une *grille non structurée* ayant :math:`246\times10^6` cellules
(:math:`\sim627^3`) est un problème typique qui ne tiendrait pas sur un
ordinateur de 48 Go : une seule variable contenant tout le modèle prendrait
déjà 25 Go. Par contre, il serait possible de visualiser ce modèle
interactivement à distance sur un serveur de 64 cœurs avec un processus
``pvserver`` prenant environ 120 Go de mémoire.

Pour cet atelier d’introduction, nous allons nous contenter du *mode autonome*.
