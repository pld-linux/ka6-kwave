#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kwave
Summary:	Sound editor
Name:		ka6-%{kaname}
Version:	25.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	41dcfa2a62cd06abdd7572d5810f4fee
URL:		http://www.kde.org/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-svg
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Multimedia-devel
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel >= 0.3.0
BuildRequires:	cmake >= 3.20
BuildRequires:	fftw3-devel
BuildRequires:	flac-c++-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-karchive-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kservice-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel >= 0.1.3
BuildRequires:	ninja
BuildRequires:	opus-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	%{name}-data = %{version}-%{release}
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kwave is a sound editor built on the KDE Frameworks 5.

%description -l pl.UTF-8
Kwave to edytor dźwięku zbudowany na bazie KDE Frameworks 5.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwave
%ghost %{_libdir}/libkwave.so.2?
%{_libdir}/libkwave.so.*.*
%ghost %{_libdir}/libkwavegui.so.2?
%{_libdir}/libkwavegui.so.*.*
%dir %{_libdir}/qt6/plugins/kwave
%{_libdir}/qt6/plugins/kwave/about.so
%{_libdir}/qt6/plugins/kwave/amplifyfree.so
%{_libdir}/qt6/plugins/kwave/band_pass.so
%{_libdir}/qt6/plugins/kwave/codec_ascii.so
%{_libdir}/qt6/plugins/kwave/codec_audiofile.so
%{_libdir}/qt6/plugins/kwave/codec_flac.so
%{_libdir}/qt6/plugins/kwave/codec_mp3.so
%{_libdir}/qt6/plugins/kwave/codec_ogg.so
%{_libdir}/qt6/plugins/kwave/codec_wav.so
%{_libdir}/qt6/plugins/kwave/debug.so
%{_libdir}/qt6/plugins/kwave/export_k3b.so
%{_libdir}/qt6/plugins/kwave/fileinfo.so
%{_libdir}/qt6/plugins/kwave/goto.so
%{_libdir}/qt6/plugins/kwave/insert_at.so
%{_libdir}/qt6/plugins/kwave/lowpass.so
%{_libdir}/qt6/plugins/kwave/newsignal.so
%{_libdir}/qt6/plugins/kwave/noise.so
%{_libdir}/qt6/plugins/kwave/normalize.so
%{_libdir}/qt6/plugins/kwave/notch_filter.so
%{_libdir}/qt6/plugins/kwave/pitch_shift.so
%{_libdir}/qt6/plugins/kwave/playback.so
%{_libdir}/qt6/plugins/kwave/record.so
%{_libdir}/qt6/plugins/kwave/reverse.so
%{_libdir}/qt6/plugins/kwave/samplerate.so
%{_libdir}/qt6/plugins/kwave/saveblocks.so
%{_libdir}/qt6/plugins/kwave/selectrange.so
%{_libdir}/qt6/plugins/kwave/sonagram.so
%{_libdir}/qt6/plugins/kwave/stringenter.so
%{_libdir}/qt6/plugins/kwave/volume.so
%{_libdir}/qt6/plugins/kwave/zero.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/org.kde.kwave.desktop
%{_datadir}/kwave
%{_datadir}/metainfo/org.kde.kwave.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/org.kde.kwave.svg*
