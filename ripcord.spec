%global         debug_package %{nil}
%global         __strip /bin/true

Summary:        Alternative desktop chat client for Slack (and Discord)
Name:           ripcord
Version:        0.4.29
Release:        11%{dist}

License:        Redistributable, no modification permitted
URL:            https://cancel.fm/ripcord
Source0:        https://cancel.fm/dl/Ripcord-%{version}-x86_64.AppImage
Source1:        fm.cancel.Ripcord.metainfo.xml
Source2:        redistribution.txt
ExclusiveArch:  x86_64

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Ripcord is a desktop chat client for services like Slack and Discord.
It provides a traditional compact desktop interface designed for power users.

%prep
%autosetup -c -T
cp %{SOURCE2} .

%build
chmod +x %{SOURCE0}
%{SOURCE0} --appimage-extract

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_libdir}/ripcord/
mkdir -p %{buildroot}/%{_datadir}/{applications,pixmaps,metainfo}/
cp -R squashfs-root/{Ripcord,translations,twemoji.ripdb} %{buildroot}/%{_libdir}/ripcord/
chmod 0755 %{buildroot}/%{_libdir}/ripcord/translations/
install -p -m 0644 squashfs-root/Ripcord_Icon.png %{buildroot}/%{_datadir}/pixmaps/
%if 0%{?fedora} && 0%{?fedora} > 39
sed -i 's@libsodium.so.18@libsodium.so.26@' %{buildroot}/%{_libdir}/ripcord//Ripcord
%else
sed -i 's@libsodium.so.18@libsodium.so.23@' %{buildroot}/%{_libdir}/ripcord//Ripcord
%endif
chrpath -d %{buildroot}/%{_libdir}/ripcord//Ripcord
strip %{buildroot}/%{_libdir}/ripcord/Ripcord
printf "#!/bin/bash\nenv RIPCORD_ALLOW_UPDATES=0 %{_libdir}/ripcord/Ripcord\n" > %{buildroot}/%{_bindir}/Ripcord
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/fm.cancel.Ripcord.metainfo.xml

# use reverse DNS for desktop file
mv squashfs-root/Ripcord.desktop fm.cancel.Ripcord.desktop

desktop-file-install                                                                 \
 --set-key=Exec --set-value='env RIPCORD_ALLOW_UPDATES=0 %{_libdir}/ripcord/Ripcord' \
 --dir=%{buildroot}/%{_datadir}/applications                                         \
 fm.cancel.Ripcord.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/fm.cancel.Ripcord.metainfo.xml


%files
%attr(755, root, root) %{_bindir}/Ripcord
%{_libdir}/ripcord/
%{_datadir}/applications/fm.cancel.Ripcord.desktop
%{_metainfodir}/fm.cancel.Ripcord.metainfo.xml
%{_datadir}/pixmaps/Ripcord_Icon.png
%license redistribution.txt

%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 03 2024 Jan200101 <sentrycraft123@gmail.com> - 0.4.29-10
- Update metainfo and desktop file to use reverse DNS
- Replace summary with text from website

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 18 2023 Leigh Scott <leigh123linux@gmail.com> - 0.4.29-7
- Fix build for f40+

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Jun 20 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.29-4
- add metainfo and missing dependency

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.29-1
- Update to version 0.4.29

* Wed Feb 03 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 15:29:37 CET 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.28-1
- Update to version 0.4.28

* Sat Nov 14 21:32:29 CET 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.27-1
- Update to version 0.4.27

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.26-1
- Update to version 0.4.26

* Fri May 22 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.25-1
- Update to version 0.4.25

* Sat Mar 14 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.24-1
- Update to version 0.4.24

* Wed Feb 19 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.23-1
- Update to version 0.4.23

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4.22-1
- Update to version 0.4.22

* Wed Jan 01 2020 Jan Drogehoff <sentrycraft123@gmail.com> - 0.4.21-4
- replace bin symlink with a wrapper to disable automatic updates

* Mon Dec 30 2019 Jan Drogehoff <sentrycraft123@gmail.com> - 0.4.21-3
- replace patchelf with sed and chrpath as suggested by leigh scott

* Mon Dec 30 2019 Jan Drogehoff <sentrycraft123@gmail.com> - 0.4.21-2
- Use improved spec made by leigh scott and add license

* Sun Dec 29 2019 Jan Drogehoff <sentrycraft123@gmail.com> - 0.4.21-1
- Initial build using version 0.4.21


