%define upstream_name    Padre-Plugin-Catalyst
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Devel)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Padre)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


