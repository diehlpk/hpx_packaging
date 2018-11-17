#
# spec file for package hpx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Christoph Junghans
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# See https://github.com/STEllAR-GROUP/hpx/issues/3509
ExcludeArch: %arm
# See https://github.com/STEllAR-GROUP/hpx/issues/3510
ExcludeArch: ppc64
ExcludeArch: ppc64le

%define mpi_implem openmpi2
%ifarch ppc64
%define mpi_implem openmpi
%endif
%if  0%{?sle_version} == 120300 && 0%{?is_opensuse}
%define mpi_implem openmpi
%endif
%if 0%{?sle_version} == 120400 && !0%{?is_opensuse}
%define mpi_implem openmpi
%endif

Name:           hpx
Version:        1.2.0
Release:        0
Summary:        General Purpose C++ Runtime System
Group:          Productivity/Networking/Other
License:        BSL-1.0
URL:            http://stellar.cct.lsu.edu/tag/hpx/
Source0:        http://stellar.cct.lsu.edu/files/%{name}_%{version}.tar.gz
#PATCH-FIX-UPSTREAM 3551.patch, fix build on i586, https://github.com/STEllAR-GROUP/hpx/pull/3551
Patch0:         https://github.com/STEllAR-GROUP/hpx/pull/3551.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  openmpi-devel
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gperftools-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
%ifarch aarch64 s390x armv7hl ppc64
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_thread-devel
%endif
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  hwloc-devel
BuildRequires:  %{mpi_implem}
BuildRequires:  %{mpi_implem}-devel
BuildRequires:  cmake
BuildRequires:  fdupes

%description
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

%package devel
Summary:    Development headers and libraries for hpx
Group:      Development/Libraries/C and C++
Requires:   hpx = %{version}-%{release}

%description devel
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

This package contains development headers and libraries for hpx

%package -n libhpx1
Summary:        Libraries for the hpx package
Group:          System/Libraries

%description -n libhpx1
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

This package contains libraries for the hpx package.

%prep
%setup -n %{name}_%{version} -q
%patch0 -p1

%build
%ifarch aarch64 s390x armv7hl ppc64
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

. %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
%{cmake} -DLIB=%{_lib} %{?cmake_opts:%{cmake_opts}}
make # no _smp_mflags to save memory

%install
make -C build install DESTDIR=%{buildroot}
rm %{buildroot}/%{_datadir}/%{name}/LICENSE_1_0.txt
%fdupes %{buildroot}%{_prefix}

sed -i '1s@env @@' %{buildroot}/%{_bindir}/{hpx*.py,hpxcxx} %{buildroot}/%{_libdir}/cmake/HPX/templates/hpx{cxx,run.py}.in
chmod +x %{buildroot}/%{_libdir}/cmake/HPX/templates/hpx{cxx,run.py}.in

%check
# full testsuite takes too much memory just run tests.examples in 1.2.0
. %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:${LD_LIBRARY_PATH}" make -C build tests.examples

%post -n libhpx1 -p /sbin/ldconfig
%postun -n libhpx1 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE_1_0.txt
%{_bindir}/*

%files -n libhpx1
%defattr(-,root,root,-)
%license LICENSE_1_0.txt
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/lib*.so.*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/%{name}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/HPX
%{_libdir}/bazel

%changelog
