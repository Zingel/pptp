Summary:	Point-to-Point Tunneling Protocol (PPTP) Client
Summary(pl):	Klient protoko�u PPTP (Point-to-Point Tunneling Protocol)
Name:		pptp-linux
Version:	1.5.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/pptpclient/%{name}-%{version}.tar.gz
# Source0-md5:	281ee37788bdf3260426eca56a9af858
Requires:	ppp >= 2.4.2
Provides:	pptp-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP. Allows connection to a PPTP based VPN as used by
employers and some cable and ADSL service providers. Requires MPPE
support in kernel.

%description -l pl
Klient PPTP - w�asno�ciowego protoko�u Point-to-Point Tunneling
Microsoftu. Umo�liwia ��czenie z siecami VPN opartymi o PPTP u�ywanymi
przez niekt�re firmy oraz dostarczycieli ��cz kablowych i ADSL. Wymaga
obsugi MPPE w j�drze.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}{/ppp,/pptp.d}}

install pptp.8 $RPM_BUILD_ROOT%{_mandir}/man8/pptp.8
install pptp $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO USING Documentation Reference
%attr(755,root,root) %{_sbindir}/pptp
%{_mandir}/man8/*
%attr(755,root,root) %{_sysconfdir}/pptp.d
