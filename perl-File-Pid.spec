#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-File-Pid
Version  : 1.01
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/C/CW/CWEST/File-Pid-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CW/CWEST/File-Pid-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-pid-perl/libfile-pid-perl_1.01-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-Pid-license = %{version}-%{release}
Requires: perl-File-Pid-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor::Fast)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
File::Pid - Pid File Manipulation
SYNOPSIS
use File::Pid;

my $pidfile = File::Pid->new({
file => '/some/file.pid',
});

$pidfile->write;

if ( my $num = $pidfile->running ) {
die "Already running: $num\n";
}

%package dev
Summary: dev components for the perl-File-Pid package.
Group: Development
Provides: perl-File-Pid-devel = %{version}-%{release}
Requires: perl-File-Pid = %{version}-%{release}

%description dev
dev components for the perl-File-Pid package.


%package license
Summary: license components for the perl-File-Pid package.
Group: Default

%description license
license components for the perl-File-Pid package.


%package perl
Summary: perl components for the perl-File-Pid package.
Group: Default
Requires: perl-File-Pid = %{version}-%{release}

%description perl
perl components for the perl-File-Pid package.


%prep
%setup -q -n File-Pid-1.01
cd %{_builddir}
tar xf %{_sourcedir}/libfile-pid-perl_1.01-2.debian.tar.xz
cd %{_builddir}/File-Pid-1.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Pid-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Pid
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Pid/c7cc5229fd3f8db8bf5627b1453f3d91bf8dcfcc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Pid.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Pid/c7cc5229fd3f8db8bf5627b1453f3d91bf8dcfcc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
