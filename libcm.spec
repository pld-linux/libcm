Summary:	Composite Manager library
Summary(pl.UTF-8):	Biblioteka Composite Manager
Name:		libcm
Version:	0.1.1
Release:	4
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libcm/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	a975d0a913dd882c0a93487b534782bc
URL:		https://www.gnome.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.7
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite Manager library.

%description -l pl.UTF-8
Biblioteka Composite Manager.

%package devel
Summary:	Header files for Composite Manager library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Composite Manager
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	glib2-devel >= 1:2.12.7
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXtst-devel

%description devel
Header files for Composite Manager library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Composite Manager.

%package static
Summary:	Static Composite Manager library
Summary(pl.UTF-8):	Statyczna biblioteka Composite Manager
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Composite Manager library.

%description static -l pl.UTF-8
Statyczna biblioteka Composite Manager.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libcm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcm.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcm.so
%{_includedir}/cm
%{_pkgconfigdir}/cm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcm.a
