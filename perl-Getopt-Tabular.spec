%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Getopt-Tabular perl module
Summary(pl):	Modu³ perla Getopt-Tabular
Name:		perl-Getopt-Tabular
Version:	0.3
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-Tabular-%{version}.tar.gz
Patch:		perl-Getopt-Tabular-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Getopt-Tabular - table-driven argument parsing for Perl. 

%description -l pl
Modu³ perla Getopt-Tabular.

%prep
%setup -q -n Getopt-Tabular-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Getopt/Tabular
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz demo

%{perl_sitelib}/Getopt/Tabular.pm
%{perl_sitearch}/auto/Getopt/Tabular

%{_mandir}/man3/*
