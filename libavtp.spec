%global commit0 9482c1143d2bca1303c4c0eeff30674eb468d357
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%define _legacy_common_support 1

Name:           libavtp
Version:        0.1.0
Release:        1%{dist}
Summary:        Audio Video Transport Protocol (AVTP) Support Library
License:        BSD
Group:          Development/Libraries
URL:            https://github.com/AVnu/libavtp.git
Source0:        https://github.com/Avnu/libavtp/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  gcc-c++ 

%description
An implementation of Audio Video Transport Protocol (AVTP) as specified
in IEEE 1722-2016.


%package devel
Summary:        Header files for the Audio/Video Transport Protocol support library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require libavtp.

%prep
%autosetup -n libavtp-%{commit0}

%build
%meson
%meson_build

%install
%meson_install

%files 
%{_libdir}/libavtp.so.0
%{_libdir}/libavtp.so.0.*

%files devel
%doc README.md
%license LICENSE
%{_includedir}/*.h
%{_libdir}/libavtp.so
%{_libdir}/pkgconfig/avtp.pc

%changelog

* Fri May 29 2020 David Va <davidva AT tuta DOT io> 0.1.0-1 
- Initial build
