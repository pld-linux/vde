Summary:	VDE: Virtual Distributed Ethernet
Summary(pl):	VDE: Wirtualny Rozproszony Ethernet
Name:		vde
Version:	1.5.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourgeforge.net/vde/%{name}-%{version}.tgz
URL:		http://sourceforge.net/projects/vde/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDE: Virtual Distributed Ethernet. It creates the abstraction of a
virtual ethernet: a single vde can be accessed by virtual and real
computers.

%description -l pl
VDE: Wirtualny Rozproszony Ethernet. Narzêdzie to tworzy abstrakcyjny
wirtualny ethernet - pojedynczy vde mo¿e byæ dostêpny z wirtualnych
jak i rzeczywistych komputerów.

%prep
%setup -q 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README TODO
#%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man8/%{name}.*
