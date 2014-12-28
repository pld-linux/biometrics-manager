Summary:	Graphical frontend for pam_bioapi enrollment
Summary(pl.UTF-8):	Graficzny interfejs do rejestrowania pam_bioapi
Name:		biometrics-manager
Version:	0.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://pam-bioapi.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	a6bc4a8629ad6ed1fa3d497a2c5cd415
Patch0:		%{name}-docdir.patch
Patch1:		%{name}-use_hicolor.patch
URL:		http://code.google.com/p/pam-bioapi/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is graphical frontend for pam_bioapi enrollment. It uses GNOME
(glade) libs.

%description -l pl.UTF-8
Ten pakiet zawiera graficzny interfejs do rejestrowania pam_bioapi.
Wykorzystuje biblioteki GNOME (glade).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
/etc/pam.d/%{name}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%{_desktopdir}/fingerprint-manager.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/fingerprint-manager.glade
%{_datadir}/%{name}/glade/hands.png
%{_iconsdir}/hicolor/*/devices/fingerprint.png
