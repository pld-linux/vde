Summary:	VDE: Virtual Distributed Ethernet
Summary(pl):	VDE: Wirtualny Rozproszony Ethernet
Name:		vde
Version:	1.5.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/vde/%{name}-%{version}.tgz
# Source0-md5:	f89a958a6997114b46abd66c00e217c8
URL:		http://sourceforge.net/projects/vde/
BuildRequires:	sed >= 4.0
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

sed -i -e 's/-O3/$(OPT)/' Makefile
sed -i -e 's/CFLAGS=/&$(OPT) /' slirpvde/Makefile
sed -i -e '/^ALL/iCFLAGS=$(OPT)' qemu/Makefile
sed -i -e '/^BIN_DIR/iCFLAGS=$(OPT)' vdetaplib/Makefile
sed -i -e 's,ln -s \$(DESTDIR)\$(BIN_DIR)/,ln -s ,' qemu/Makefile

rm -f qemu/{vdeq.o,vdeq}

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}

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
