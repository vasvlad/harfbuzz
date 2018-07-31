Name:    harfbuzz
Version: 1.8.4
Release: 1
Summary: Text shaping library
License: MIT
URL:     http://freedesktop.org/wiki/Software/HarfBuzz
Source0: http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-%{version}.tar.bz2
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  ragel

%description
HarfBuzz is an implementation of the OpenType Layout engine.

%package devel
Summary:  Development files for Harfbuzz
Requires: %{name} = %{version}-%{release}

%description devel
Development package for the Harfbuzz library.

%package icu
Summary: Harfbuzz ICU support library
Requires: %{name} = %{version}-%{release}

%description    icu
Harfbuzz ICU support library.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%autogen --disable-static

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post icu -p /sbin/ldconfig
%postun icu -p /sbin/ldconfig

%files
%doc NEWS AUTHORS COPYING README
%{_libdir}/libharfbuzz.so.*
%{_libdir}/libharfbuzz-subset.so.*

%files devel
%{_bindir}/hb-view
%{_bindir}/hb-ot-shape-closure
%{_bindir}/hb-shape
%{_bindir}/hb-subset
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/libharfbuzz-subset.so
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_libdir}/cmake/harfbuzz/harfbuzz-config.cmake

%files icu
%{_libdir}/libharfbuzz-icu.so.*
