%define upstream_name    Padre-Plugin-Catalyst
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst plugin for Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/Padre-Plugin-Catalyst-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(File::ShareDir::Install)
BuildRequires:	perl(Catalyst::Devel)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Pluggable::Object)
BuildRequires:	perl(Padre)

BuildArch:	noarch

%description
Once you enable this Plugin under Padre, you'll get a brand new menu with
the following options:

'New Catalyst Application'
    This options lets you create a new Catalyst application.

'Create new...'
    The Catalyst helper lets you automatically create stub classes for your
    application's MVC components. With this menu option not only can you
    select your component's name but also its type. For instance, if you
    select "create new view" and have the the Catalyst::Helper::View::TT
    manpage module installed on your system, the "TT" type will be
    available for you).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 653609
- rebuild for updated spec-helper

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 570115
- skip tests
- update to 0.09

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 493587
- update to 0.08

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 474744
- update to 0.07

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 472244
- update to 0.06

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 439420
- update to 0.05

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 395168
- update to 0.04

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 381302
- adding missing buildrequires:
- import perl-Padre-Plugin-Catalyst


* Sat May 30 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


