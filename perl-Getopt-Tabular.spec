%include	/usr/lib/rpm/macros.perl
%define		pdir	Getopt
%define		pnam	Tabular
Summary:	Getopt::Tabular - table-driven argument parsing for Perl
Summary(pl):	Getopt::Tabular - przetwarzanie argumentów z tabeli w Perlu
Name:		perl-Getopt-Tabular
Version:	0.3
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5b24ed68318a749df3930d25b13dd436
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt::Tabular is a Perl module for table-driven argument parsing,
vaguely inspired by John Ousterhout's Tk_ParseArgv.

%description -l pl
Getopt::Tabular jest modu³em Perla do przetwarzania argumentów z
tabeli, nieznacznie zainspirowanym przez Tk_ParseArgv Johna
Ousterhouta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README demo
%{perl_vendorlib}/Getopt/Tabular.pm
%{_mandir}/man3/*
