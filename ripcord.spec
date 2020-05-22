%global         debug_package %{nil}
%global         __strip /bin/true

Summary:        a lightweight chat client for Slack and Discord
Name:           ripcord
Version:        0.4.25
Release:        1%{dist}

License:        Redistributable, no modification permitted
URL:            https://cancel.fm/ripcord
Source0:        https://cancel.fm/dl/Ripcord-%{version}-x86_64.AppImage
Source1:        redistribution.txt
ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  chrpath

%description
Ripcord is a proprietary shareware client for Slack and Discord

%prep
%autosetup -c -T
cp %{SOURCE1} .

%build
chmod +x %{SOURCE0}
%{SOURCE0} --appimage-extract

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_libdir}/ripcord/
mkdir -p %{buildroot}/%{_datadir}/{applications,pixmaps}/
cp -R squashfs-root/{Ripcord,translations,twemoji.ripdb} %{buildroot}/%{_libdir}/ripcord/
chmod 0755 %{buildroot}/%{_libdir}/ripcord/translations/
install -p -m 0644 squashfs-root/Ripcord_Icon.png %{buildroot}/%{_datadir}/pixmaps/
sed -i 's@libsodium.so.18@libsodium.so.23@' %{buildroot}/%{_libdir}/ripcord//Ripcord
chrpath -d %{buildroot}/%{_libdir}/ripcord//Ripcord
strip %{buildroot}/%{_libdir}/ripcord/Ripcord
printf "#!/bin/bash\nenv RIPCORD_ALLOW_UPDATES=0 %{_libdir}/ripcord/Ripcord\n" > %{buildroot}/%{_bindir}/Ripcord

desktop-file-install                                                                 \
 --set-key=Exec --set-value='env RIPCORD_ALLOW_UPDATES=0 %{_libdir}/ripcord/Ripcord' \
 --dir=%{buildroot}/%{_datadir}/applications                                         \
 squashfs-root/Ripcord.desktop

%files
%attr(755, root, root) %{_bindir}/Ripcord
%{_libdir}/ripcord/
%{_datadir}/applications/Ripcord.desktop
%{_datadir}/pixmaps/Ripcord_Icon.png
%license redistribution.txt

%changelog
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


