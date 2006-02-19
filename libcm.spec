Summary:	Composite Manager library
Summary(pl):	Biblioteka Composite Manager
Name:		libcm
Version:	0.0.16
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.daimi.au.dk/~sandmann/%{name}-%{version}.tar.gz
# Source0-md5:	705488259eb99748216e42130b171053
Patch0:		%{name}-configure.patch
URL:		http://www.daimi.au.dk/~sandmann/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite Manager library.

%description -l pl
Biblioteka Composite Manager.

%package devel
Summary:	Header files for Composite Manager library
Summary(pl):	Pliki nag³ówkowe biblioteki Composite Manager
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXtst-devel

%description devel
Header files for Composite Manager library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Composite Manager.

%package static
Summary:	Static Composite Manager library
Summary(pl):	Statyczna biblioteka Composite Manager
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Composite Manager library.

%description static -l pl
Statyczna biblioteka Composite Manager.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
rm -f $RPM_BUILD_ROOT%{_bindir}/test

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
