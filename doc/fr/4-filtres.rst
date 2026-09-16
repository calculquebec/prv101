Enrichir la visualisation avec des filtres
==========================================

`English <../en/4-filters.html>`__

Introduction aux filtres
------------------------

Plusieurs caractéristiques intéressantes d’un ensemble de données ne peuvent
être observées en surface : une grande quantité d’informations utiles se
trouve plutôt **à l’intérieur**, ou peut être extraite d’une **combinaison de
variables**.

.. grid:: 2

    .. grid-item::
        :columns: 6

        Parfois, une vue souhaitée n’est pas disponible pour un certain type de
        données, par exemple :

        - Un ensemble de données 2D :math:`f(x,y)` sera affiché comme une
          surface 2D, même en 3D (essayez de charger
          ``~/prv101-main/lab/2d000.vtk``), mais nous pourrions vouloir
          visualiser **l’élévation** :math:`z=f(x,y)`.
        - Une **vue volumétrique** -- non disponible pour toutes les
          discrétisations VTK, mais disponible, entre autres, pour les **points
          structurés** (*Image Data*) et même les **grilles non structurées
          si la connectivité est fournie**.

    .. grid-item::
        :columns: 3

        .. figure:: ../images/grids1.png
            :width: 75%

    .. grid-item::
        :columns: 3

        .. figure:: ../images/grids2.png
            :width: 75%

Les **filtres** sont des unités fonctionnelles qui traitent les données pour
générer, extraire ou dériver des caractéristiques supplémentaires. Les
connexions entre les filtres forment un **pipeline de visualisation**.

- ParaView fournit déjà plus de 140 filtres et on peut en ajouter via des
  scripts Python ou via des plugiciels programmés en C++.

  - Explorez le menu *Filters* ; certains filtres se trouvent aussi dans la
    barre d’outils.

- L’édition des propriétés d’un filtre se fait dans le panneau *Properties*.
