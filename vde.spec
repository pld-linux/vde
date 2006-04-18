Summary:	VDE: Virtual Distributed Ethernet
Summary(pl):	VDE: wirtualny rozproszony ethernet
Name:		vde
Version:	2.0.2
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	d97a8dbc72942c57542f50322b538a48
URL:		http://sourceforge.net/projects/vde/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Conflicts:	qemu >= 8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDE: Virtual Distributed Ethernet. It creates the abstraction of a
virtual ethernet: a single vde can be accessed by virtual and real
computers.

%description -l pl
VDE: wirtualny rozproszony ethernet. Narzêdzie to tworzy abstrakcyjny
wirtualny ethernet - pojedynczy vde mo¿e byæ dostêpny z wirtualnych
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

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/vdeqemu
ln -sf vdeq $RPM_BUILD_ROOT%{_bindir}/vdeqemu

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libvdetap.so
%{_mandir}/man1/*.1*
