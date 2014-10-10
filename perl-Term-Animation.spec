%define upstream_name    Term-Animation
%define upstream_version 2.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	ASCII sprite animation framework 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Curses)

BuildArch:	noarch

%description
This module provides a framework to produce sprite animations using ASCII art.
Each ASCII 'sprite' is given one or more frames, and placed into the animation
as an 'animation object'. An animation object can have a callback routine that
controls the position and frame of the object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Term
%{_mandir}/*/*

%changelog
* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.600.0-1mdv2011.0
+ Revision: 649175
- update to new version 2.6

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.400.0-1mdv2011.0
+ Revision: 505274
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.4-6mdv2010.0
+ Revision: 430555
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.4-5mdv2009.0
+ Revision: 258486
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.4-4mdv2009.0
+ Revision: 246513
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.4-2mdv2008.1
+ Revision: 136713
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.4-1mdv2007.0
+ Revision: 100400
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.2-1mdv2007.1
+ Revision: 84307
- new version
- Import perl-Term-Animation

* Fri Sep 09 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-2mdk
- fix buildrequires (Luca Olivetti <luca@ventoso.org>)

* Thu Sep 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-1mdk
- first mdk release

