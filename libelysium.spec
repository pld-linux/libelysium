%define  ver 0.2.6
%define  rel 1

Summary: Elysium GNU/Linux Utilities Library
Name: libelysium
Version: %ver
Release: %rel
Copyright: LGPL
Group: System/Libraries
Source: %{name}-%{ver}.tar.gz
BuildRoot: /var/tmp/%{name}-%{PACKAGE_VERSION}-root
Obsoletes: encompass-uri

%description
Utility library for applications in the Elysium GNU/Linux distribution.

%package devel
Summary: Elysium GNU/Linux Utilities Library Development Files
Group: System/Libraries/Development
Requires: %{name} = %{PACKAGE_VERSION}
Requires: glib-devel
Obsoletes: encompass-uri-devel

%description devel
Libraries and includes files used for developing Elysium GNU/Linux applications

%prep
%setup

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if ! grep %{prefix}/lib /etc/ld.so.conf > /dev/null ; then
  echo "%{prefix}/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)
%{_prefix}/lib/lib*.so
%{_prefix}/include/libelysium/*.h
%{_prefix}/lib/*Conf.sh

%changelog

* Wed Oct 03 2001 Rodney Dawes <dobey@free.fr>
- Initial libelysium spec file (renamed library from encompass-uri)
