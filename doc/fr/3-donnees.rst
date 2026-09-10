Importer des données
====================

`English <../en/3-data.html>`__

Sources de données
------------------

Il y a deux types de sources de données :

1. On peut créer des données de base à partir d’un **objet Source**.
2. On peut aussi lire des données à partir d’un **fichier**.

Tel que mentionné en introduction, ParaView peut charger des dizaines de
formats de données -- les principaux sont listés dans la note ci-dessous.

.. admonition:: Liste des formats de données pris en charge
    :collapsible: closed

    La liste ci-dessous est basée sur ParaView 5.9.0 en date du 2 avril 2021.

    - ADAPT Files (``*.nc *.cdf *.elev *.ncd``)
    - Adaptive cosmo files (``*.cosmo``)
    - ADIOS2 BP3 File (Corelmage) (``*.bp``)
    - ADIOS2 BP4 Directory (Corelmage) (``*.bp``)
    - ADIOS2 BP4 Metadata File (Corelmage) (``md.idx``)
    - AMR Enzo Files (``*.boundary *.hierarchy``)
    - AMR Flash Files (``*.Flash *.flash``)
    - AMR Velodyne Files (``*.xarnr *.Xamr *.XAMR``)
    - AMReX/BoxLib plotfiles (grids) (``plt*``)
    - AMReX/BoxLib plotfiles (particles) (``plt*``)
    - ANSYS Files (``*.inp``)
    - AU File Files (``*.aux``)
    - AVS UCD Binary/ASCII Files (``*.inp``)
    - BOV Files (``*.bov``)
    - BYU Files (``*.g``)
    - CAM NetCDF (Unstructured) (``*.nc *.ncdf``)
    - Case file for restarted CTH outputs
    - CCSM MTSD Files (``*.nc *.cdf *.elev *.ncd``)
    - CCSM STSD Files (``*.nc *.cdf *.elev *.ncd``)
    - CEAucd Files (``*.ucd *.inp``)
    - CGNS Files (``*.cgns``)
    - Chombo Files (``*.hdf5 *.h5``)
    - CityGML files (``*.gml *.xml``)
    - Claw Files (``*.claw``)
    - CMAT Files (``*.cmat``)
    - CML (``*.cml``)
    - CONVERGE CFD (``*.h5``)
    - Cosmology Files (``*.cosmo64 *.cosmo``)
    - CTRL Files (``*.ctrl``)
    - Curve2D Files (``*.curve *.ultra *.ult *.u``)
    - DDCMD Files (``*.ddcmd``)
    - Delimited Text (``*.csv *.tsv *.txt *.CSV *.TSV *.TXT``)
    - DICOM Files (directory) (``*.dcm``)
    - DICOM Files (single) (``*.dcm``)
    - Digital Elevation Map Files (``*.dem``)
    - Dyna3D Files (``*.dyn``)
    - EnSight Files (``*.case *.CASE *.Case``)
    - EnSight Master Server Files (``*.sos *.SOS``)
    - ENZO AMR Particles (``*.boundary *.hierarchy``)
    - Exodus11 (``*.g *.gc *.ex2 *.ex2v2 *.exo *.gen *.par``)
    - ExtrudedVol Files (``*.exvol``)
    - Facet Polygonal Data Files (``*.facet``)
    - Fides Data Model File (JSON) (``*.json``)
    - Fides Files (ADIOS2 BP) (``*.bp``)
    - FLASH AMR Particles Reader (``*.Flash *.flash``)
    - FLASH Files (Visit) (``*.flash *.f5``)
    - Fluent Case Files (``*.cas``)
    - Fluent Files (Visit) (``*.cas``)
    - FVCOM MTMD Files (``*.nc *.cdf *.elev *.ncd``)
    - FVCOM MTSD Files (``*.nc *.cdf *.elev *.ncd``)
    - FVCOM Particle Files (``*.nc *.cdf *.elev *.ncd``)
    - FVCOM STSD Files (``*.nc *.cdf *.elev *.ncd``)
    - Gadget Files (``*.gadget``)
    - Gaussian Cube Files (``*.cube``)
    - GDAL Raster (``*.tif *.gen *.thf *.adf *.arg *.blx *.xlb``)
    - GDAL Vector (``*.shp *.faa *.bnn *.dxf *.csv *.geojson``)
    - Generic10 files to MultiBlockDataSet (``*.gio``)
    - Generic10 files to UnstructuredGrid (``*.gio``)
    - GGCM Files (``*.3df *.mer``)
    - gITF 2.0 Files (``*.gltf *.glb``)
    - GTC Files (``*.h5``)
    - GULP Files (``*.trg``)
    - H5Nimrod Files (``*.h5nimrod``)
    - H5Part particle files (``*.h5part``)
    - HyperTreeGrid (``*.htg``)
    - HyperTreeGrid (partitioned) (``*.phtg``)
    - Image Files (``*.pnm *.ppm *.sdt *.spr *.imgvol``)
    - JPEG Image
    - LAMMPS Dump Files (``*.dump``)
    - LAMMPS Struct. (``*.eam *.meam *.rigid *.lammps``)
    - Legacy VTK files (``*.vtk *.vtk.series``)
    - Legacy VTK Files (partitioned) (``*.pvtk``)
    - Lines Files (``*.lines``)
    - LODI Files (``*.no *.cdf *.elev *.ncd``)
    - LODI Particle Files (``*.nc *.cdf *.elev *.ncd``)
    - LSDyna (``*.k *.lsdyna *.d3plot``)
    - M3DC1 Files (``*.h5``)
    - Meta Image Files (``*.mhd *.mha``)
    - Meta-Generic10 files (``*.gios``)
    - Metafile for restarted exodus outputs
    - MFiX netcdf Files (``*.nc``)
    - MFiX Res Files (Visit) (``*.RES``)
    - MFIX Unstructured Grid Files (``*.RES``)
    - Mill Files (``*.m``)
    - Miranda Files (``*.mir *.raw``)
    - MM5 Files (``*.mm5``)
    - MotionFX CFG Files (``*.cfg``)
    - MPAS NetCDF (Unstructured) (``*.ncdf *sic``)
    - MRC Image Files (``*.mrc *.ali *.st *.rec``)
    - Multilevel 3D Plasma Files (``*.m3d *.h5``)
    - NASTRAN Files (``*.nas *.f06``)
    - Nek5000 (``*.nek3d *.nek2d *.nek5d *.nek5000 *.nek``)
    - netCDF generic and CF conventions (``*.ncdf *.nc``)
    - Nrrd Raw Image Files (``*.nrrd *.nhdr``)
    - OME TIFF Files (``*.ome.tif *.ome.tiff``)
    - OpenFOAM (``*.foam``)
    - OpenFOAM Files (Visit) (``*.controlDict``)
    - openPMD files (``*.pmd``)
    - OVERFLOW Files (Visit) (``*.dat *.save``)
    - ParaDIS Files (``*.prds *.data *.dat``)
    - ParaDIS Tecplot (``Mid *.field *.cyl *.cylinder *.dat``)
    - Parallel POP Ocean NetCDF (``*.pop.ncdf *.pop.nc``)
    - ParaView Data Files (``*.pvd``)
    - ParaView Ensemble Data (``*.pve``)
    - PATRAN Files (``*.neu``)
    - PFLOTRAN Files (``*.h5``)
    - Phasta Files (``*.pht``)
    - PIO Dump Files (``*.pio``)
    - Pixie Files (``*.h5``)
    - PLOT2D Files (``*.p2d``)
    - PLOT3D Files (``*.xyz``)
    - PLOT3D Meta Files (``*.p3d``)
    - PLY Polygonal File Format (``*.ply *.ply.series``)
    - PNG Image Files (``*.png``)
    - POINT3D Files (``*.3D``)
    - POP Ocean NetCDF Rectilinear (``*.pop.nc*``)
    - POP Ocean NetCDF Unstructured (``*.pop.nc*``)
    - proSTAR Files (``*.cel *.vrt``)
    - Protein Data Bank Files (``*.pdb``)
    - Protein Data Bank Files (Visit) (``*.ent *.pdb``)
    - PTS (Point Cloud) Files (``*.pts``)
    - Radiance HDR file (``*.hdr``)
    - Raw (binary) Files (``*.raw``)
    - RAW Files (``*.raw``)
    - SAMRAI series files (``*.samrai``)
    - SAR Files (``*.SAR *.sar``)
    - SAS Files (``*.sasgeom *.sas *.sasdata``)
    - SEG-Y Files (``*.sgy *.segy``)
    - SEP file (Plugin) (``*.H``)
    - Silo Files (``*.silo *.pdb *.silo.series *.pdb.series``)
    - SLAC Mesh Files (``*.ncdf *.nc``)
    - SLAC Particle Files (``*.ncdf *.netcdf``)
    - Spheral Files (``*.spheral *.sv``)
    - Spy Plot History Files (``*.hscth *hsct*``)
    - SpyPlot CTH dataset (``*.spct* spot*``)
    - Stereo Lithography (``*.stl *.stl.series``)
    - Tecplot Binary Files (Visit) (``*.plt``)
    - Tecplot Files (``*.tee *.TEC *.Tec *.tp *.TP *.dat``)
    - Tecplot Files (Visit) (``*.tec *.TEC *.Tec *.tp *.TP``)
    - Tecplot Table (``*.dat *.DAT``)
    - Tetrad Files (``*.hdf5 *.h5``)
    - TFT Files (``*.dat *.tft``)
    - TIFF Image Files (``*.tif *.tiff``)
    - TRUCHAS dataset (``*.hdf5 *.h5``)
    - TSurf Files (``*.ts_deg83``)
    - UNIC Files (``*.h5``)
    - VASP Animation Files (``*.out``)
    - VASP CHGCA Files (``*.CHG*``)
    - VASP OUT Files (``*.OUT*``)
    - VASP POSCAR Files (``*.POS*``)
    - VASP Tessellation Files (``*.out``)
    - Velodyne Files (``*.vld *.rst``)
    - Visit MetaPLOT3D Files (Visit) (``*.vp3d``)
    - VizSchema Files (``*.h5 *.vsh5``)
    - VPIC Files (``*.vpc``)
    - VRML 2 Files (``*.wrl *.vrml``)
    - VTK Hierarchical Box Data Files (``*.vthb``)
    - VTK ImageData Files (``*.vti *.vti.series``)
    - VTK ImageData Files (partitioned) (``*.pvti``)
    - VTK MultiBlock Data Files (``*.vtm *.vtmb``)
    - VTK Particle Files (``*.particles``)
    - VTK Partitioned Dataset Collection Files (``*.vtpc``)
    - VTK Partitioned Dataset Files (``*.vtpd *.vtpd.series``)
    - VTK PolyData Files (``*.vtp *.vtp.series``)
    - VTK PolyData Files (partitioned) (``*.pvtp``)
    - VTK RectilinearGrid Files (``*.vtr *.vtr.series``)
    - VTK RectiiinearGrid Files (partitioned) (``*.pvtr``)
    - VTK StructuredGrid Files (``*.vts *.vts.series``)
    - VTK StructuredGrid Files (partitioned) (``*.pvts``)
    - VTK Table (partitioned) (``*.pvtt *.pvtt.series``)
    - VTK Table Files (``*.vtt *.vtt.series``)
    - VTK UnstructuredGrid Files (``*.vtu *.vtu.series``)
    - VTK UnstructuredGrid Files (partitioned) (``*.pvtu``)
    - VTX reader: ADIOS2 BP3 File (``*.bp``)
    - VTX reader: ADIOS2 BP4 Directory (``*.bp *.bp4``)
    - Wavefront OBJ Files (``*.obj``)
    - WindBlade Data (``*.wind``)
    - Xdmf Reader (``*.xmf *.xdmf *.xmf2 *.xdmf2``)
    - Xdmf3 Reader (``*.xmf *.xdmf *.xmf3 *.xdmf3``)
    - Xdmf3 Reader (Top Level Partition) (``*.xmf* *.xdmf``)
    - Xmdv Files (``*.okc``)
    - XMol Molecule Files (``*.xyz``)
    - XYZ Files (``*.xyz``)

Exemple -- Lire des données brutes ou binaires
''''''''''''''''''''''''''''''''''''''''''''''

On souhaite visualiser la fonction suivante pour :math:`x,y,z\in[0,1]` sur une
grille :math:`16 \times 16 \times 16` :

:math:`f(x,y,z)=(1-z)\left[(1-y)\sin(\pi x) + y\sin^2(2\pi x)\right] + z\left[(1-x)\sin(\pi y) + x\sin^2(2\pi y)\right]`

.. grid:: 2

    .. grid-item::
        :columns: 8

        1. Ouvrez le fichier ``~/prv101-main/lab/simpleData.raw``.

           - Lorsque demandé, sélectionnez *Image Reader*.

        2. Spécifiez ensuite les propriétés des données :

           - *Data Scalar Type* : ``float``
           - *Data Byte Order* : ``LittleEndian``
           - *Scalar Array Name* : ``density``
           - *File Dimensionality* : ``3``
           - *Data Extent* : ``0`` à ``15`` pour chaque dimension (``1`` à
             ``16`` chargerait les données incorrectement).

        3. Modifiez la vue : *Outline*, *Points*, *Wireframe*, *Volume*.
        4. Avec la vue en *Volume*, éditez l’échelle de couleurs.

    .. grid-item::
        :columns: 4

        .. figure:: ../images/twist.png

    .. grid-item::
        :columns: 12

        5. (Optionnel) Sauvegardez et rechargez les données.

           - Via *File* :math:`\rightarrow` *Save Data...*, sauvegardez l’objet
             dans un fichier de données ParaView (``*.pvd``).
           - Supprimez l’objet.
           - Chargez le fichier ``*.pvd`` -- ce fichier de données contient
             effectivement toutes les propriétés que nous avons définies.
