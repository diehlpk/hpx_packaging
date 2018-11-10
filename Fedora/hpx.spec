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

%package mpich-devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx-mpich = %{version}-%{release}

%description mpich-devel
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

This package contains development headers


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


%package openmpi-devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx-openmpi = %{version}-%{release}

%description openmpi-devel
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

This package contains development headers for hpx

%prep
%setup -n %{name}-%{uversion} -q

%build
%ifarch aarch64 s390x armv7hl
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  mkdir -p ${mpi:-serial}
  pushd ${s:-.}/${mpi:-serial}
  if [ -n "$mpi" ]; then
  export CC=mpicc
  export CXX=mpicxx
  %{cmake} -DHPX_WITH_PARCELPORT_MPI=0N -DLIB=${MPI_LIB} %{?cmake_opts:%{cmake_opts}} ..
  else
  export CC=gcc
  export CXX=g++
  %{cmake} -DLIB=%{_lib} %{?cmake_opts:%{cmake_opts}} ..
  fi
  %make_build 
  popd
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
# do serial install last due to move of executables to _bindir
. /etc/profile.d/modules.sh
for mpi in openmpi mpich '' ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch} && mkdir -p %{buildroot}/${MPI_BIN}
  pushd ${s:-.}/${mpi:-serial}
  %make_install
  if [ -n "$mpi" ]; then
  libdir=${MPI_LIB}
  else
  libdir=%{_libdir}
  fi
  sed -i '1s@env python@python2@' %{buildroot}/%{_bindir}/{hpx*.py,hpxcxx}  %{buildroot}${libdir}/cmake/HPX/templates/hpx{cxx,run.py}.in
  chmod +x  %{buildroot}${libdir}/cmake/HPX/templates/hpx{cxx,run.py}.in
  popd
  pushd %{buildroot}/%{_bindir}
  for exe in  *; do 
    test -n '${exe##hpx*}' && mv "${exe}" "hpx_${exe}"
  done
  popd
  test -n "${mpi}" && mv %{buildroot}/%{_bindir}/* %{buildroot}/${MPI_BIN}/
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch} 
done

rm %{buildroot}/%{_datadir}/%{name}-*/LICENSE_1_0.txt
rm -rf %{buildroot}/%{_datadir}/%{name}-*/docs/html/code
%fdupes %{buildroot}%{_prefix}

%check
. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  make -C ${mpi:-serial} tests.examples
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%ldconfig_scriptlets libs

%files
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/%{name}/
%{_libdir}/lib*.so.*

%files examples
%doc README.rst
%license LICENSE_1_0.txt
%{_bindir}/*

%files openmpi
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/openmpi*/lib/lib*.so.*
%{_libdir}/openmpi*/lib/%{name}

%files openmpi-examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/openmpi*/bin/*

%files openmpi-devel
%{_includedir}/%{name}
%{_libdir}/openmpi*/lib/pkgconfig/*.pc
%{_libdir}/openmpi*/lib/cmake/HPX
%{_libdir}/openmpi*/lib/bazel
%{_libdir}/openmpi*/lib/lib*.a
%{_libdir}/openmpi*/lib/lib*.so*

%files mpich
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/mpich*/lib/lib*.so.*
%{_libdir}/mpich*/lib/%{name}

%files mpich-examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/mpich*/bin/*

%files mpich-devel
%{_includedir}/%{name}
%{_libdir}/mpich*/lib/pkgconfig/*.pc
%{_libdir}/mpich*/lib/cmake/HPX
%{_libdir}/mpich*/lib/bazel
%{_libdir}/mpich*/lib/lib*.a
%{_libdir}/mpich*/lib/lib*.so*

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/HPX
%{_libdir}/bazel
%{_libdir}/lib*.a
%{_libdir}/lib*.so*

%changelog
* Fri Nov 09 2018 Patrick Diehl <patrickdiehl@lsu.edu> - 1.2-0.1.rc1
- Initial Release of HPX 1.2
