%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	Tabular
Summary:	Getopt::Tabular perl module
Summary(pl):	Modu³ perla Getopt::Tabular
Name:		perl-Getopt-Tabular
Version:	0.3
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Tabular - table-driven argument parsing for Perl.

%description -l pl
Modu³ perla Getopt::Tabular.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README demo
%{perl_sitelib}/Getopt/Tabular.pm
%{_mandir}/man3/*
