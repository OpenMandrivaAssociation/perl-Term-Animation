%define upstream_name    Term-Animation
%define upstream_version 2.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	ASCII sprite animation framework 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Curses)
# tests
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This module provides a framework to produce sprite animations using ASCII art.
Each ASCII 'sprite' is given one or more frames, and placed into the animation
as an 'animation object'. An animation object can have a callback routine that
controls the position and frame of the object.

%files
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/man3/*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
%make test
l
