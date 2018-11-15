Name:           hpx
Version:        1.2.0
Release:        2%{?dist}
Summary:        General Purpose C++ Runtime System
License:        Boost
URL:            http://stellar.cct.lsu.edu/tag/hpx/
Source0:        http://stellar.cct.lsu.edu/files/%{name}_%{version}.tar.gz
Patch0:         https://github.com/STEllAR-GROUP/hpx/pull/3551.patch
#hpx has no support for
# https://github.com/STEllAR-GROUP/hpx/issues/3511
ExcludeArch: s390x
# https://github.com/STEllAR-GROUP/hpx/issues/3509
ExcludeArch: armv7hl

BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gperftools-devel
BuildRequires:  boost-devel
BuildRequires:  hwloc-devel
BuildRequires:  cmake
BuildRequires:  fdupes


%global hpx_desc \
HPX is a general purpose C++ runtime system for parallel and distributed \
applications of any scale. \
\
The goal of HPX is to create a high quality, freely available, \
open source implementation of the ParalleX model for conventional systems, \
such as classic Linux based Beowulf clusters or multi-socket highly parallel \
SMP nodes. At the same time, we want to have a very modular and well designed \
runtime system architecture which would allow us to port our implementation \
onto new computer system architectures. We want to use real world applications\
to drive the development of the runtime system, coining out required \
functionality and converging onto a stable API which will provide a smooth \
migration path for developers. The API exposed by HPX is modeled after the \
interfaces defined by the C++11 ISO standard and adheres to the \
programming guidelines used by the Boost collection of C++ libraries.

%description
%{hpx_desc}

This package contains the libraries

%package examples
Summary: HPX examples
Requires:       hpx = %{version}-%{release}

%description examples
%{hpx_desc}

This package contains the examples

%package devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx = %{version}-%{release}

%description devel
%{hpx_desc}

This package contains development headers and libraries

%package mpich
Summary:        HPX MPICH libraries
Requires:       mpich
BuildRequires:  mpich-devel

%description mpich
%{hpx_desc}

This package contains the libraries

%package mpich-examples
Summary: HPX MPICH examples
Requires:       mpich
Requires:       hpx-mpich = %{version}-%{release}
BuildRequires:  mpich-devel

%description mpich-examples
%{hpx_desc}

This package contains the examples

%package mpich-devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx-mpich = %{version}-%{release}

%description mpich-devel
%{hpx_desc}.

This package contains development headers and libraries


%package openmpi
Summary:        HPX Open MPI libraries
Requires:       openmpi
BuildRequires:  openmpi-devel

%description openmpi
%{hpx_desc}

This package contains the libraries

%package openmpi-examples
Summary: HPX Open MPI examples
Requires:       openmpi
Requires:       hpx-openmpi = %{version}-%{release}
BuildRequires:  openmpi-devel

%description openmpi-examples
%{hpx_desc}.

This package contains the examples


%package openmpi-devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx-openmpi = %{version}-%{release}

%description openmpi-devel
%{hpx_desc}

This package contains development headers and libraries

%prep
%setup -n %{name}_%{version} -q
%patch0 -p1

%build
# use generic context for these archs
%ifarch aarch64 s390x armv7hl
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

# ppc64 do not have enough memory
%ifarch ppc64le
%global _smp_mflags -j1
%endif

. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  mkdir -p ${mpi:-serial}
  pushd ${mpi:-serial}
  test -n "${mpi}" && export CC=mpicc && export CXX=mpicxx
  %{cmake} ${mpi:+-DHPX_WITH_PARCELPORT_MPI=ON} -DLIB=${MPI_LIB:-%{_lib}} %{?cmake_opts:%{cmake_opts}} ..
  %make_build
  test -n "${mpi}" && unset CC CXX
  popd
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
# do serial install last due to move of executables to _bindir
. /etc/profile.d/modules.sh
for mpi in openmpi mpich '' ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch} && mkdir -p %{buildroot}/${MPI_BIN}
  pushd ${mpi:-serial}
  %make_install
  sed -i '1s@env python@python2@' %{buildroot}/%{_bindir}/{hpx*.py,hpxcxx}  %{buildroot}${MPI_LIB:-%{_libdir}}/cmake/HPX/templates/hpx{cxx,run.py}.in
  chmod +x  %{buildroot}${MPI_LIB:-%{_libdir}}/cmake/HPX/templates/hpx{cxx,run.py}.in
  popd
  pushd %{buildroot}/%{_bindir}
  # rename executable with too generic names
  for exe in  *; do
    test -n '${exe##hpx*}' && mv "${exe}" "hpx_${exe}"
  done
  popd
  test -n "${mpi}" && mv %{buildroot}/%{_bindir}/* %{buildroot}/${MPI_BIN}/
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

rm %{buildroot}/%{_datadir}/%{name}/LICENSE_1_0.txt
%fdupes %{buildroot}%{_prefix}

%check
. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  make -C ${mpi:-serial} tests.examples
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%ldconfig_scriptlets

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
* Thu Nov 15 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-2
- Added upstream patch 3551.patch to fix build on i686

* Wed Nov 14 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-1
- Version bump to hpx-1.2.0

* Fri Nov 09 2018 Patrick Diehl <patrickdiehl@lsu.edu> - 1.2-0.1.rc1
- Initial Release of HPX 1.2_rc1
