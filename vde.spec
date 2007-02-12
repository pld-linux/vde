Summary:	VDE: Virtual Distributed Ethernet
Summary(pl.UTF-8):	VDE: wirtualny rozproszony ethernet
Name:		vde
Version:	1.5.11
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	00f739390a86fa5860a269ca157ee0f6
URL:		http://sourceforge.net/projects/vde/
BuildRequires:	autoconf
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/vdeqemu
ln -sf vdeq $RPM_BUILD_ROOT%{_bindir}/vdeqemu

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libvdetap.so
%{_mandir}/man1/*.1*
