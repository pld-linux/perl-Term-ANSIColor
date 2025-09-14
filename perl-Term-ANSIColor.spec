#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Term
%define		pnam	ANSIColor
Summary:	Term::ANSIColor - color screen output using ANSI escape sequences
Summary(pl.UTF-8):	Term::ANSIColor - kolorowe wyświetlanie przy użyciu sekwencji ANSI
Name:		perl-Term-ANSIColor
# NOTE: 5.01 in perl-modules 5.42
Version:	5.01
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5b097ce054447c649de4a022213349c6
URL:		https://www.eyrie.org/~eagle/software/ansicolor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Obsoletes:	perl-ANSIColor < 3.01
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

%description -l pl.UTF-8
Ten moduł Perla to prosty i wygodny interfejs do sekwencji
terminalowych ANSI służących do ustawiania kolorów (zdefiniowanych w
EMCA-48, włączonych także do ISO 6429). Sekwencje kolorów są
udostępniane na dwa sposoby - jako stałe dla każdego koloru oraz jako
funkcja przyjmująca nazwy kolorów i zwracająca odpowiednie kody
lub wstawiająca je w podany tekst. Obsługiwane są także kody stylu
tekstu nie związane z kolorami (pogrubienie, pociemnienie,
podkreślenie, negatyw) zgodnie ze standardem ANSI X3.64 (włączonym
także w ECMA-48 i ISO 6429).

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
%doc Changes LICENSE README.md THANKS TODO
%{perl_vendorlib}/Term/ANSIColor.pm
%{_mandir}/man3/Term::ANSIColor.3pm*
