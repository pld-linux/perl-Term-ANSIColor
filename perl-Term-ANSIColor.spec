#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ANSIColor
Summary:	Term::ANSIColor - color screen output using ANSI escape sequences
Summary(pl):	Term::ANSIColor - kolorowe wy¶wietlanie przy u¿yciu sekwencji ANSI
Name:		perl-Term-ANSIColor
Version:	1.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	660522d9d16c9dc823a768509b53632b
URL:		http://www.eyrie.org/~eagle/software/ansicolor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-ANSIColor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module is a simple and convenient interface to the ANSI
terminal escape sequences for color (from ECMA-48, also included in
ISO 6429). The color sequences are provided in two forms, either as
constants for each color or via a function that takes the names of
colors and returns the appropriate escape codes or wraps them around
the provided text. The non-color text style codes from ANSI X3.64
(bold, dark, underline, and reverse), which were also included in
ECMA-48 and ISO 6429, are also supported.

%description -l pl
Ten modu³ Perla to prosty i wygodny interfejs do sekwencji
terminalowych ANSI s³u¿±cych do ustawiania kolorów (zdefiniowanych w
EMCA-48, w³±czonych tak¿e do ISO 6429). Sekwencje kolorów s±
udostêpniane na dwa sposoby - jako sta³e dla ka¿dego koloru oraz jako
funkcja przyjmuj±ca nazwy kolorów i zwracaj±ca odpowiednie kody
lub wstawiaj±ca je w podany tekst. Obs³ugiwane s± tak¿e kody stylu
tekstu nie zwi±zane z kolorami (pogrubienie, pociemnienie,
podkre¶lenie, negatyw) zgodnie ze standardem ANSI X3.64 (w³±czonym
tak¿e w ECMA-48 i ISO 6429).

%prep
%setup -q -n %{pnam}-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/Term/ANSIColor.pm
%{_mandir}/man3/*
