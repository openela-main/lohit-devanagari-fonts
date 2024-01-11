%global fontname lohit-devanagari
%global fontconf 65-1-%{fontname}.conf
%global fontconf1 59-%{fontname}.conf
%global metainfo io.pagure.lohit.devanagari.font.metainfo

Name:           %{fontname}-fonts
Version:        2.95.4
Release:        3%{?dist}
Summary:        Free Devanagari Script Font
Group:          User Interface/X
License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires:  ttfautohint
BuildRequires: python3-devel
Requires:       fontpackages-filesystem

%description
This package provides a free Devanagari Script TrueType/OpenType font.

%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-1-lohit-devanagari.conf

%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -m 0644 -p %{fontconf1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf1} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf1}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f *-%{fontname}.conf *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-devanagari.txt
%{_datadir}/metainfo/%{metainfo}.xml


%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.95.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.95.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 10 2017 Pravin Satpute <psatpute@redhat.com> - 2.95.4-1
- Upstream new release 2.95.4
- Update metainfo file and fixing minor fixes
- Removed patch, installing 59-lohit-devanagari.conf.
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 07 2017 Pravin Satpute <psatpute@redhat.com> - 2.95.3-1
- Added  BuildRequires: python2-devel.
- Resolves: #1423902 - FTBFS in rawhide.
- Migrated from fedorahosted to pagure.io.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.95.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.95.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 28 2015 Pravin Satpute <psatpute@redhat.com> - 2.95.2-1
- Resolves #1229183: Updates to Unicode 8.0
- Added U+0978, U+A8FC and U+A8FD

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.95.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Pravin Satpute <psatpute@redhat.com> - 2.95.1-2
- Resolves #1219451: No alias for Mangal fonts

* Wed Mar 25 2015 Pravin Satpute <psatpute@redhat.com> - 2.95.1-1
- Upstream release 2.95.1
- Update U+0960 shape as per patch from Shriramana Sharma. #1113968
- Changed hex id of i-matra (65514...65528,65531 65533) to 65537 onwards

* Mon Mar 02 2015 Pravin Satpute <psatpute@redhat.com> - 2.95.0-1
- Upstream latest release 2.95.0
- Added Latin from https://github.com/etunni/lohit-latin
- Updated sfd file with resolved issues regarding marathi locale (issue id on github: #46,#47)
- Feature file updated
- Resolves issue #https://github.com/pravins/lohit2/issues/11
- Added uni1cf5 and uni1cf6 characters
- Removed incorrect mapping for isigndeva.tha - AFDKO
- Removed control character from font

* Mon Oct 20 2014 Pravin Satpute <psatpute@redhat.com> - 2.94.0-4
- Added metainfo for gnome-software

* Fri Sep 05 2014 Pravin Satpute <psatpute@redhat.com> - 2.94.0-3
- Updated fontconf priority to handle clash with lohit-marathi #1138569

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.94.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Pravin Satpute <psatpute@redhat.com> - 2.94.0-1
- Upstream release 2.94.0 with enhancements and bug fixes.
- Positioning lookup clean-up.
- Improved grid fitting(GASP) table.
- Renamed anchors to DVAnchor.
- Using glyph reference (copy reference) instead of whole glyph points.
- Auto test integrated with Makefile ($make test).
- Added "Santali" language in font config file.
- Resolved #32: "सर्व्हिस does not render correctly"
- Resolved #33: "improper rendering for word : "मञ्यांच्या""

* Thu Dec 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.93.0-1
- Upstream release 2.93.0 with enhancements and bug fixes

* Thu Nov 07 2013 Pravin Satpute <psatpute@redhat.com> - 2.92.0-1
- Beta release 2.92.0 from upstream

* Thu Oct 03 2013 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Alpha upstream release of lohit-devanagari 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Changed fontconf priority

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-1
- Upstream release 2.5.2 and spec file cleanup

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-3
- Resoved bug #803308 and #799004

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Upstream new release with additional characters from Unicode 6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Tue Jul 19 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- Resolved: bug 722382

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- Resolved: bug 715090, patch from Bernard Massot <bmassot@free.fr>

* Tue May 24 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- Resolved: bug 702058, patch from Bernard Massot <bmassot@free.fr>

* Fri Mar 25 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- Upstream release 2.4.5
- Removed hinting instructions bug 682667

* Fri Mar 25 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-4
- Resolved: bug 682667

* Mon Feb 21 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- resolved bug 648423 and bug 670467

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release 2.4.4

* Fri Nov 26 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-8
- added nepali local support
- resolved bugs 648434, 648429, 648424, 648362

* Fri Oct 08 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-7
- fixed bug 641297
- added rupee symbol

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- fixed bug 578034

* Thu Feb 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- done changes as per review comments bug 559936 

* Fri Jan 29 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- first release
- decided to keep only one font for all languages using devanagari script
