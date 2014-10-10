%define upstream_name    Crypt-MySQL
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Emulate MySQL PASSWORD() function
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Crypt::MySQL emulates MySQL PASSWORD() SQL function, without
libmysqlclient. You can compare encrypted passwords, without real MySQL
environment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2
+ Revision: 680855
- mass rebuild

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 573812
- import perl-Crypt-MySQL

