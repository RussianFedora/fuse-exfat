Name:       fuse-exfat
Summary:    Free exFAT file system implementation
Summary(ru):Свободная имплементация файловой системы exFAT
Version:    0.9.8
Release:    1%{?dist}

License:    GPLv3+
Group:      System Environment/Base
Source0:    http://exfat.googlecode.com/files/fuse-exfat-%{version}.tar.gz
URL:        http://code.google.com/p/exfat/

BuildRequires:  fuse-devel >= 2.6
BuildRequires:  scons
BuildRequires:  gzip

Requires:   fuse >= 2.6

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%description -l ru
Данный драйвер является первой свободной имплементацией файловой системы
exFAT с поддержкой записи. exFAT это простая файловая система, созданная
Microsoft. Она предназначена для замены FAT32 и снимает некоторые её
ограничения. exFAT - стандартная файловая система для карт памяти SDXC.

%prep
%setup -q

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
scons install DESTDIR=$RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8/
install -m 0644 -p fuse/mount.exfat-fuse.8 $RPM_BUILD_ROOT/usr/share/man/man8


%files
%doc COPYING
%{_sbindir}/mount.exfat-fuse
%{_sbindir}/mount.exfat
%{_mandir}/man8/mount.exfat-fuse.8*

%changelog
* Sun Aug 12 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.8-1.R
- update to 0.9.8

* Tue Mar 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.7-1.R
- update to 0.9.7

* Tue Jan 17 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.6-1.R
- update to 0.9.6

* Thu Jul  7 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.5-1.R
- update to 0.9.5

* Thu Mar 17 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.4-3.1
- bump release for rebuild

* Thu Mar 17 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.9.4-2
- Cosmetic changes

* Sat Mar  5 2011 Andrew Nayenko <resver@gmail.com> - 0.9.4-1
- Updated to 0.9.4.
- Pass DESTDIR as argument instead of environment variable.

* Sat Sep 25 2010 Andrew Nayenko <resver@gmail.com> - 0.9.3-1
- Updated to 0.9.3.

* Sat Jul 24 2010 Andrew Nayenko <resver@gmail.com> - 0.9.2-1
- Updated to 0.9.2.
- Changed summary according to the main site.
- Added man page installation.

* Sat Jun 12 2010 Andrew Nayenko <resver@gmail.com> - 0.9.1-1
- Updated to 0.9.1.

* Mon Feb 22 2010 Andrew Nayenko <resver@gmail.com> - 0.9.0-1
- Initial package for Fedora.
