Summary:	Elysium GNU/Linux Utilities Library
Summary(pl):	Biblioteka narzêdziowa Elysium GNU/Linux
Name:		libelysium
Version:	0.3.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://elysium.zoned.net/libelysium/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	encompass-uri

%description
Utility library for applications in the Elysium GNU/Linux
distribution.

%description -l pl
Biblioteka narzêdziowa dla aplikacji w dystrybucji Elysium GNU/Linux.

%package devel
Summary:	Elysium GNU/Linux Utilities Library Development Files
Summary(pl):	Pliki dla programistów u¿ywaj±cych biblioteki narzêdziowej Elysium GNU/Linux
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib-devel
Obsoletes:	encompass-uri-devel

%description devel
Includes files used for developing Elysium GNU/Linux applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji Elysium GNU/Linux.

%package static
Summary:	Elysium GNU/Linux Utilities static library
Summary(pl):	Statyczna biblioteka narzêdziowa Elysium GNU/Linux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	encompass-uri-devel

%description static
Elysium GNU/Linux Utilities static library.

%description static -l pl
Statyczna biblioteka narzêdziowa Elysium GNU/Linux.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-1.0/libelysium
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
