%define keepstatic 1
Name:    harfbuzz
Version: 8.1.1
Release: 1
Summary: Text shaping library
License: MIT
URL:     https://harfbuzz.github.io/
Source0: %{name}-%{version}.tar.bz2
#BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  ragel

%description
HarfBuzz is an implementation of the OpenType Layout engine.

%package devel
Summary:  Development files for Harfbuzz
Requires: %{name} = %{version}-%{release}
Requires: %{name}-icu = %{version}-%{release}

%package devel-static
Summary:  Development files for Harfbuzz
#Requires: %{name} = %{version}-%{release}
#Requires: %{name}-icu = %{version}-%{release}

%description devel
Development package for the Harfbuzz library.

%description devel-static
Development package for the Harfbuzz library.

%package icu
Summary:  Harfbuzz ICU support library
Requires: %{name} = %{version}-%{release}

%description icu
Harfbuzz ICU support library.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%autogen --enable-static --with-gobject=no --with-graphite2
%make_build

%install
%make_install

# Sometimes fuzzing tests can time out running under qemu on OBS
%ifarch %{ix86} x86_64
%check
make check
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post icu -p /sbin/ldconfig
%postun icu -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libharfbuzz.so.*
%{_libdir}/libharfbuzz-cairo.so.*
%{_libdir}/libharfbuzz-subset.so.*

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files devel
%defattr(-,root,root,-)
%doc NEWS AUTHORS README.md
%{_bindir}/hb-info
#%{_bindir}/hb-view
%{_bindir}/hb-ot-shape-closure
%{_bindir}/hb-shape
%{_bindir}/hb-subset
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/libharfbuzz-cairo.so
%{_libdir}/pkgconfig/harfbuzz-cairo.pc
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/libharfbuzz-subset.so
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_libdir}/cmake/harfbuzz/harfbuzz-config.cmake

%files icu
%defattr(-,root,root,-)
%{_libdir}/libharfbuzz-icu.so.*
