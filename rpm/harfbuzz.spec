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

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%autogen --disable-static

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        NEWS AUTHORS README

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post icu -p /sbin/ldconfig
%postun icu -p /sbin/ldconfig

%files
%license COPYING
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

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
