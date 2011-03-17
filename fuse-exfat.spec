Name:		fuse-exfat
Summary:	Free exFAT file system implementation
Version:	0.9.4
Release:	3%{?dist}

License:	GPLv3+
Group:		System Environment/Base
Source0:	http://exfat.googlecode.com/files/fuse-exfat-%{version}.tar.gz
URL:		http://code.google.com/p/exfat/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	fuse-devel >= 2.6
BuildRequires:	scons
BuildRequires:	gzip

Requires:	fuse >= 2.6

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup -q

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
scons install DESTDIR=$RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8/
install -m 0644 -p fuse/mount.exfat-fuse.8 $RPM_BUILD_ROOT/usr/share/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
/sbin/mount.exfat-fuse
/sbin/mount.exfat
%{_mandir}/man8/mount.exfat-fuse.8*

%changelog
* Thu Mar 17 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.9.4-3
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
