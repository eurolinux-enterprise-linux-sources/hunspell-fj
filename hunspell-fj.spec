Name: hunspell-fj
Summary: Fijian hunspell dictionaries
Version: 1.2
Release: 7%{?dist}
Group: Applications/Text
#Source: http://www.foss.usp.ac.fj/OOo_fj/OOo_fj_FJ.zip
Source: http://releases.mozilla.org/pub/mozilla.org/addons/12115/fijian_spelling_dictionary-%{version}-fx+tb+sm.xpi
URL: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPLv2+ or MPLv1.1
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Fijian hunspell dictionaries.

%prep
%setup -q -c

%build
cd dictionaries
for i in README_fj_FJ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
chmod -x fj_FJ.*

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/fj_FJ.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/fj.aff
cp -p dictionaries/fj_FJ.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/fj.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc dictionaries/README_fj_FJ.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Caolán McNamara <caolanm@redhat.com> - 1.2-3
- Resolves: rhbz#734218 remove executable flags

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 07 2010 Caolán McNamara <caolanm@redhat.com> - 1.2-1
- latest version

* Wed Apr 07 2010 Caolán McNamara <caolanm@redhat.com> - 0.20090521-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050811-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20050811-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050811-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 01 2008 Caolán McNamara <caolanm@redhat.com> - 0.20050811-1
- initial version
