Name:           hpx
Version:        1.2.0
%global uversion 1.2.0-rc1
Release:        0.1.rc1
Summary:        General Purpose C++ Runtime System
License:        BSL-1.0
URL:            http://stellar.cct.lsu.edu/tag/hpx/
#Source0:        http://stellar.cct.lsu.edu/files/{name}_{uversion}.tar.gz
Source0:        https://github.com/STEllAR-GROUP/%{name}/archive/%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
#hpx has no support for 
ExcludeArch: s390x
ExcludeArch: armv7hl

BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gperftools-devel
BuildRequires:  boost-devel
BuildRequires:  hwloc-devel
BuildRequires:  cmake
BuildRequires:  fdupes

%description
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

%package examples
Summary: HPX examples
Requires:       hpx = %{version}-%{release}

%description examples
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

HPX compiled with gcc, package incl. examples

%package devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx = %{version}-%{release}

%description devel
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

This package contains development headers and libraries for hpx

%package mpich
Summary:        HPX MPICH libraries
Requires:       mpich
BuildRequires:  mpich-devel

%description mpich
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

HPX compiled with MPICH, package incl. libraries

%package mpich-examples
Summary: HPX MPICH examples
Requires:       mpich
Requires:       hpx-mpich = %{version}-%{release}
BuildRequires:  mpich-devel

%description mpich-examples
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

HPX compiled with MPICH, package incl. examples

%package openmpi
Summary:        HPX Open MPI libraries
Requires:       openmpi
BuildRequires:  openmpi-devel

%description openmpi
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

HPX compiled with Open MPI, package incl. libraries

%package openmpi-examples
Summary: HPX Open MPI examples
Requires:       openmpi
Requires:       hpx-openmpi = %{version}-%{release}
BuildRequires:  openmpi-devel

%description openmpi-examples
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

The goal of HPX is to create a high quality, freely available, open source implementation of the 
ParalleX model for conventional systems, such as classic Linux based Beowulf clusters or multi-socket
highly parallel SMP nodes. At the same time, we want to have a very modular and well designed runtime
system architecture which would allow us to port our implementation onto new computer system
architectures. We want to use real world applications to drive the development of the runtime system,
coining out required functionalities and converging onto a stable API which will provide a smooth
migration path for developers. The API exposed by HPX is modelled after the interfaces defined by the
C++11 ISO standard and adheres to the programming guidelines used by the Boost collection of C++
libraries.

HPX compiled with Open MPI, package incl. examples


%prep
%setup -n %{name}-%{uversion} -q

%build
%ifarch aarch64 s390x armv7hl
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

mkdir openmpi mpich serial

pushd serial
%{cmake} -DLIB=%{_lib} %{?cmake_opts:%{cmake_opts}} ..
%make_build
popd

pushd openmpi
%{_openmpi_load}
%{cmake} -DLIB=${MPI_LIB} %{?cmake_opts:%{cmake_opts}} ..
%make_build
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%{cmake} -DLIB=${MPI_LIB} %{?cmake_opts:%{cmake_opts}} ..
%make_build
%{_mpich_unload}
popd

%install
%make_install -C serial 
sed -i '1s@env python@python2@' %{buildroot}/%{_bindir}/{hpx*.py,hpxcxx}  %{buildroot}%{_libdir}/cmake/HPX/templates/hpx{cxx,run.py}.in
chmod +x  %{buildroot}%{_libdir}/cmake/HPX/templates/hpx{cxx,run.py}.in
cd  %{buildroot}/%{_bindir} && rename '' hpx_ * && cd .. 
%{_openmpi_load}
%make_install -C openmpi
mkdir %{buildroot}/${MPI_BIN}
mv %{buildroot}/%{_bindir}/* %{buildroot}/${MPI_BIN}/
sed -i '1s@env python@python2@' %{buildroot}/${MPI_BIN}/{hpx*.py,hpxcxx} %{buildroot}/${MPI_LIB}/cmake/HPX/templates/hpx{cxx,run.py}.in
chmod +x %{buildroot}/${MPI_LIB}/cmake/HPX/templates/hpx{cxx,run.py}.in
cd %{buildroot}/${MPI_BIN}/ && rename '' hpx_ * && cd .. 
%{_openmpi_unload}
%{_mpich_load}
%make_install -C mpich
mkdir %{buildroot}/${MPI_BIN}
mv %{buildroot}/%{_bindir}/* %{buildroot}/${MPI_BIN}/
sed -i '1s@env python@python2@' %{buildroot}/${MPI_BIN}/{hpx*.py,hpxcxx} %{buildroot}/${MPI_LIB}/cmake/HPX/templates/hpx{cxx,run.py}.in
chmod +x %{buildroot}/${MPI_LIB}/cmake/HPX/templates/hpx{cxx,run.py}.in
cd %{buildroot}/${MPI_BIN}/ && rename '' hpx_ * && cd .. 
%{_mpich_unload}

rm %{buildroot}/%{_datadir}/%{name}-*/LICENSE_1_0.txt
rm -rf %{buildroot}/%{_datadir}/%{name}-*/docs/html/code
%fdupes %{buildroot}%{_prefix}

# check currently needs too much memory, re-enable in next version
#%check
#%{_openmpi_load}
#make -C openmpi tests CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}
#%{_openmpi_unload}
#%{_mpich_load}
#make -C mpich tests CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}
#%{_mpich_unload}

%files
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/%{name}/
%{_libdir}/lib*.so.*

%files examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/bin/*

%files openmpi
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/openmpi*/lib/lib*.so.*
%{_libdir}/openmpi*/lib/%{name}

%files openmpi-examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/openmpi*/bin/*


%files mpich
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/mpich*/lib/lib*.so.*
%{_libdir}/mpich*/lib/%{name}

%files mpich-examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/mpich*/bin/*

%files devel
%{_includedir}/%{name}
%{_libdir}/*mpi*/lib/lib*.so
%{_libdir}/*mpi*/lib/%{name}/lib*.so
%{_libdir}/*mpi*/lib/lib*.a
%{_libdir}/*mpi*/lib/pkgconfig/*.pc
%{_libdir}/*mpi*/lib/cmake/HPX
%{_libdir}/*mpi*/lib/bazel
%{_datadir}/%{name}-*

%changelog
