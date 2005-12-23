Summary:	VDE: Virtual Distributed Ethernet
Summary(pl):	VDE: wirtualny rozproszony ethernet
Name:		vde
Version:	1.5.9
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/vde/%{name}-%{version}.tar.gz
# Source0-md5:	13337f2317a51a8c441503a0b0c908ac
Patch0:		%{name}-DESTDIR.patch
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT

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
