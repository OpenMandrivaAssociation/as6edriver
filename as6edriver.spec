%define name	as6edriver
%define version	0.5
%define release	%mkrel 3

Name: 		%{name}
Version:	%{version}
Release: 	%{release}
Summary: 	Linux driver for the Artec AS6E parallel port interface scanner
URL: 		http://as6edriver.sourceforge.net/
Group:		Graphics
License: 	GPL
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	glibc-devel
Epoch: 1
ExclusiveArch: x86_64 %{ix86}

%description
The as6edriver is a driver for the Artec AS6E parallel port
interface scanner. It is still in development, but it seems to
work for most people.
Version 0.4.2 updated the driver for SANE version 1.0.3 and 
2.4 series kernels. As of version 0.3, it works in EPP mode, 
cutting scan times roughly in half!

SANE is now supported and included in sane packages.

%prep
%setup -q 

%build
%configure
%make

%install
mkdir -p %{buildroot}/{%{_sysconfdir},%{_bindir}}
install -m 755 as6edriver/as6edriver %{buildroot}/%{_bindir}
#install -m 644 as6e.conf %{buildroot}/%{_sysconfdir}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL README USE
%attr(4755,root,root) %{_bindir}/as6edriver
#%config(noreplace) %{_sysconfdir}/as6e.conf

