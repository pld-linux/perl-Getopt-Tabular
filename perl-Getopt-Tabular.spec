%include	/usr/lib/rpm/macros.perl
Summary:	Getopt-Tabular perl module
Summary(pl):	Modu³ perla Getopt-Tabular
Name:		perl-Getopt-Tabular
Version:	0.3
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-Tabular-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-Tabular - table-driven argument parsing for Perl.

%description -l pl
Modu³ perla Getopt-Tabular.

%prep
%setup -q -n Getopt-Tabular-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz demo
%{perl_sitelib}/Getopt/Tabular.pm
%{_mandir}/man3/*
