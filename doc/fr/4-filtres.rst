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

  - Tous les filtres se trouvent dans le menu *Filters*.
  - `Certains filtres
    <https://docs.paraview.org/en/latest/UsersGuide/filteringData.html#filters-for-sub-setting-data>`__
    se trouvent aussi dans la barre d’outils.

    .. figure:: ../images/toolbarFilters.png

    - Un filtre **Calculator** évalue une expression mathématique pour chaque
      point ou chaque cellule.
    - Un filtre **Contour** extrait des points, des isocontours ou des
      isosurfaces à partir d’un champ scalaire.
    - Un filtre **Clip** (rognage) enlève toute la partie de la visualisation
      d’un côté d’un plan dans l’espace 3D.
    - Un filtre **Slice** (tranche) intersecte la visualisation avec un plan ;
      l’effet est similaire au *Clip*, excepté qu’il ne reste que la géométrie
      à l’intersection du plan et de la visualisation.
    - Un filtre **Threshold** (seuil(s)) extrait les cellules se trouvant dans
      un certain intervalle du champ scalaire.
    - Un filtre **Glyph** place des *glyphes* à chaque point d’un maillage ;
      les glyphes peuvent être orientés selon un champ vectoriel et agrandis
      selon un champ vectoriel ou scalaire.
    - Un filtre **Stream Tracer** initialise un champ vectoriel avec des
      points, puis suit ces points initiaux à travers le champ vectoriel en
      régime permanent.

- L’édition des propriétés d’un filtre se fait dans le panneau *Properties*.

Exemple -- Visualiser des données 2D en 3D
''''''''''''''''''''''''''''''''''''''''''

1. Chargez le fichier ``~/prv101-main/lab/2d000.vtk`` qui contient un
   échantillonnage de la fonction 2D
   :math:`f(x,y)=(1-y)\sin(\pi x)+y\sin^2(2\pi x)` pour
   :math:`x,y\in[0,1]` sur une grille :math:`30 \times 30`.
2. Sélectionnez les données dans le *Pipeline Browser*, ajoutez le filtre
   *Miscellaneous* :math:`\rightarrow` *Warp By Scalar* et activez la vue *3D*
   dans la fenêtre de rendu.
3. Dans les propriétés du filtre, ajustez le *Scale Factor* à ``0.3`` pour
   reproduire la vue 3D ci-dessous :

.. grid:: 2

    .. grid-item::
        :columns: 4

        .. figure:: ../images/sin2d.png

    .. grid-item::
        :columns: 1

        |
        |
        |
        | :math:`\Rightarrow`

    .. grid-item::
        :columns: 7

        .. figure:: ../images/sin3d.png

Première série d’exercices avec les filtres
-------------------------------------------

Recréez cette visualisation avec un filtre *Contour*
''''''''''''''''''''''''''''''''''''''''''''''''''''

.. grid:: 2

    .. grid-item::
        :columns: 6

        - Données à la source : ``~/prv101-main/lab/sineEnvelope.nc``
        - Indices :

          - Filtre de type *Contour*.
          - Isosurface à ``0.16``.
          - Échelle de couleurs de ``0.15`` à ``0.20``.

        *(3 minutes + solution)*

    .. grid-item::
        :columns: 5

        .. figure:: ../images/cont015.png

Bonifiez la visualisation avec un filtre *Clip*
'''''''''''''''''''''''''''''''''''''''''''''''

.. grid:: 2

    .. grid-item::
        :columns: 7

        - Données à la source : ``~/prv101-main/lab/sineEnvelope.nc``
        - Indices :

          - Pipeline de visualisation à deux filtres.
          - Filtre de type *Clip*.
          - L’échelle de couleurs selon la variable *density*, partagée par les
            deux calculateurs, s’ajuste automatiquement.
          - Option *Show Plane*.

        *(3 minutes + solution)*

    .. grid-item::
        :columns: 5

        .. figure:: ../images/clipCont.png

Recréez cette visualisation avec un filtre *Threshold*
''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. grid:: 2

    .. grid-item::
        :columns: 7

        - Données à la source : ``~/prv101-main/lab/sineEnvelope.nc``
        - Indices :

          - Filtre de type *Threshold*.
          - Afficher les points dont la valeur :math:`\rho\in[0.8, 1.0]`.
          - Gradient de couleurs pour l’arrière-plan.
          - *Ray tracing* et *Shadows*.
          - *View* :math:`\rightarrow` *Light Inspector*.

        *(3 minutes + solution)*

    .. grid-item::
        :columns: 5

        .. figure:: ../images/threshold0810.png

Recréez cette visualisation avec caméras liées
''''''''''''''''''''''''''''''''''''''''''''''

.. grid:: 2

    .. grid-item::
        :columns: 5

        - Données à la source : ``~/prv101-main/lab/disk_out_ref.ex2``

          - ``Pres`` et ``Temp`` seulement.

        - Indices :

          - Compléter une visualisation à la fois.
          - Coloration selon ``Pres`` à gauche.
          - Coloration selon ``Temp`` à droite.
          - Lier les caméras.

        *(3 minutes + solution)*

    .. grid-item::
        :columns: 7

        .. figure:: ../images/twoVariables.png
            :width: 100%

Visualisation vectorielle -- lignes de flux et glyphes
------------------------------------------------------

Voici un exemple de visualisation des flux à l’intérieur d’un volume :

.. grid:: 2

    .. grid-item::
        :columns: 6

        1. Chargez ``Temp`` et la vélocité ``V`` du fichier
           ``~/prv101-main/lab/disk_out_ref.ex2``.
        2. Ajoutez un filtre *Stream Tracer*, configurez le
           *Seed Type* = ``Point Cloud`` et le *Radius* = ``3`` pour la sphère.
           Ensuite :

           - Essayez différents *Number Of Points* et différents *Maximum
             Streamline Length*.

        3. (Optionnel) Transformez les lignes de flux en tubes en ajoutant :
           *Filters* :math:`\rightarrow` *Miscellaneous* :math:`\rightarrow`
           *Tube* (avec *Radius* = ``0.03``).

    .. grid-item::
        :columns: 6

        .. figure:: ../images/vectorFields.png
            :width: 100%

    .. grid-item::
        :columns: 12

        4. Ajoutez des glyphes aux lignes de flux pour indiquer l’orientation
           et l’amplitude :

           - Sélectionnez le *StreamTracer* dans le *Pipeline Browser*.
           - Ajoutez-lui un filtre *Glyph* de *Type* = ``Arrow``, avec :

             - *Orientation Array* = ``V``,
             - *Scale Array* = ``No scale array``,
             - *Scale Factor* = ``0.5``.

           - Coloriez les glyphes selon ``Temp``.
