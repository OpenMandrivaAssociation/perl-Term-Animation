%define module  Term-Animation
%define name	perl-%{module}
%define version 2.4
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	ASCII sprite animation framework 
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Curses)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module provides a framework to produce sprite animations using ASCII art.
Each ASCII 'sprite' is given one or more frames, and placed into the animation
as an 'animation object'. An animation object can have a callback routine that
controls the position and frame of the object.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/*/*


