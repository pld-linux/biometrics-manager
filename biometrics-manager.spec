#
Summary:	Graphical frontend for pam_bioapi enrollment.
Name:		biometrics-manager
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://pam-bioapi.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	a6bc4a8629ad6ed1fa3d497a2c5cd415
Patch0:		%{name}-docdir.patch
URL:		http://code.google.com/p/pam-bioapi/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libglade2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is graphical frontend for pam_bioapi enrollment.
It using gnome (glade) libs.

%prep
%setup -q
%patch0 -p1

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/pam.d/%{name}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%{_desktopdir}/fingerprint-manager.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade/fingerprint-manager.glade
%{_datadir}/%{name}/glade/hands.png
%{_iconsdir}/gnome/*/devices/fingerprint.png
