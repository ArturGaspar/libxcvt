Name:       libxcvt
Version:    0.1.2
Release:    1%{?dist}
Summary:    VESA CVT standard timing modelines generator implementation
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/libxcvt
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  meson >= 0.40.0

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/cvt
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libxcvt.pc

%files doc
%license COPYING
%{_mandir}/man1/cvt.1*
