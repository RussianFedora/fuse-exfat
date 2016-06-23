Name:           fuse-exfat
Summary:        Free exFAT file system implementation
Summary(ru):    Свободная имплементация файловой системы exFAT
Version:        1.2.4
Release:        1%{?dist}

License:        GPLv2+
Group:          System Environment/Base
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/fuse-exfat-%{version}.tar.gz
URL:            https://github.com/relan/exfat

BuildRequires:  pkgconfig(fuse)


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
%configure
%make_build

%install
%make_install INSTALL="install -p"


%files
%license COPYING
%{_sbindir}/mount.exfat-fuse
%{_sbindir}/mount.exfat
%{_mandir}/man8/mount.exfat-fuse.8*

%changelog
* Thu Jun 23 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.4-1
- Clean spec
- Update to 1.2.4

* Wed Mar 30 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1
- Update to 1.2.3

* Sat Nov 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Dec 20 2014 TingPing <tingping@tingping.se> - 1.1.0-1
- Update to 1.1.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Mar 20 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.1-1.R
- update to 1.0.1

* Mon Jan 21 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-1.R
- update to 1.0.0

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
