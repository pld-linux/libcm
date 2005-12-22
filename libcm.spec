Summary:	Composite Manager library
Name:		libcm
Version:	0.0.13
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.daimi.au.dk/~sandmann/%{name}-%{version}.tar.gz
# Source0-md5:	e5f157950cdece940a9e6a7d137e4214
URL:		http://www.daimi.au.dk/~sandmann/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite Manager library

%package devel
Summary:	Header files for Composite Manager library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Composite Manager library.

%package static
Summary:	Static Composite Manager library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Composite Manager library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cm
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
