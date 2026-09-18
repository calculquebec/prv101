SGrid: SGrid.cpp
	g++ $^ -o $@ -I"${EBROOTVTK}/include/vtk-9.4" \
	-lvtkIOXML-9.4 -lvtkCommonDataModel-9.4 -lvtkCommonCore-9.4 \
	-lvtksys-9.4
writeVolume: writeVolume.cpp
	g++ $^ -o $@
# writeVolume: writeVolume.f90
# 	gfortran $^ -o $@
writeNetCDF: writeNetCDF.cpp
	g++ $^ -o $@ -I$(NETCDFDIR)/include -L$(NETCDFDIR)/lib -lnetcdf_c++4 -lnetcdf
#writeNetCDF: writeNetCDF.f90
#	gfortran $^ -o $@ -I$(NETCDFDIR)/include -L$(NETCDFDIR)/lib -lnetcdff -lnetcdf
optimization: optimization.c
	gcc $^ -o $@ -I$(NETCDFDIR)/include -L$(NETCDFDIR)/lib -lnetcdf
writeRawBinary: writeRawBinary.f90
	gfortran $^ -o $@     # with Intel compiler use -assume byterecl
clean:
	@/bin/rm -rf *.o *.mod *~ cylinder.vtk volume.nc stvol.nc 111* halfCylinder.vts
	@find . -type f -perm +111 | xargs /bin/rm -rf
