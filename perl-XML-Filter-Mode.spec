#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-Mode
Summary:	XML::Filter::Mode - filter out all chunks not in the current mode
Summary(pl):	XML::Filter::Mode - odfiltrowywanie fragmentów spoza aktualnego trybu
Name:		perl-XML-Filter-Mode
Version:	0.02
Release:	1
License:	BSD or Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09369387b622557e7815166fbef21d91
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Machines
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Filter::Mode Perl module filters portions of documents based on a
"mode" attribute.

%description -l pl
Modu³ Perla XML::Filter::Mode s³u¿y do odfiltrowywania fragmentów
dokumentów na podstawie atrybutu "mode".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
