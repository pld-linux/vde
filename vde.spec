Summary:	VDE: Virtual Distributed Ethernet
Summary(pl.UTF-8):	VDE: wirtualny rozproszony ethernet
Name:		vde
Version:	1.5.11
Release:	3
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	00f739390a86fa5860a269ca157ee0f6
Patch0:		%{name}-includes.patch
URL:		http://sourceforge.net/projects/vde/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDE: Virtual Distributed Ethernet. It creates the abstraction of a
virtual ethernet: a single vde can be accessed by virtual and real
computers.

%description -l pl.UTF-8
VDE: wirtualny rozproszony ethernet. Narzędzie to tworzy abstrakcyjny
wirtualny ethernet - pojedynczy vde może być dostępny z wirtualnych
jak i rzeczywistych komputerów.

%prep
%setup -q 
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure  \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT

# same directory, convert to relative symlink
ln -snf vdeq $RPM_BUILD_ROOT%{_bindir}/vdeqemu

# loadable module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvdetap.la

cp -p qemu/README README.qemu
cp -p slirpvde/README README.slirpvde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.qemu README.slirpvde qemu/qemu-vde-HOWTO
%attr(755,root,root) %{_bindir}/dpipe
%attr(755,root,root) %{_bindir}/slirpvde
%attr(755,root,root) %{_bindir}/vde_plug
%attr(755,root,root) %{_bindir}/vde_switch
%attr(755,root,root) %{_bindir}/vdeq
%attr(755,root,root) %{_bindir}/vdeqemu
%attr(755,root,root) %{_bindir}/vdetap
%attr(755,root,root) %{_libdir}/libvdetap.so
%{_mandir}/man1/dpipe.1*
%{_mandir}/man1/slirpvde.1*
%{_mandir}/man1/vde_plug.1*
%{_mandir}/man1/vde_switch.1*
%{_mandir}/man1/vdeq.1*
%{_mandir}/man1/vdetaplib.1*
