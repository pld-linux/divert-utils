Summary:	An ethernet frame diverter for transparent www proxying bridge and more
Summary(pl):	Ethernetowy frame diverter dla transparentnego proxy www i wiêcej
Name:		divert-utils
Version:	0.221
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://diverter.sourceforge.net/EtherDivert/%{name}-%{version}.tar.gz
# Source0-md5:	027266c07c7e912f62801b5da3db105f
URL:		http://diverter.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
An ethernet frame diverter for transparent www proxying bridge and
more.

%description -l pl
Ethernetowy frame diverter dla transparentnego proxy www i wiêcej.

%prep
%setup -q

%build
%{__make} \
	DEBUG="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install divert			$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
