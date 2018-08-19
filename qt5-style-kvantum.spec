%define oname Kvantum

Name:           qt5-style-kvantum
Version:        0.10.8
Release:        1
License:        GPLv3+
Summary:        SVG-based Qt5 theme engine plus a config tool and extra themes
Group:          System/Libraries
URL:            https://github.com/tsujan/Kvantum
Source0:        https://github.com/tsujan/Kvantum/archive/%{oname}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5X11Extras)

%description
Kvantum is an SVG-based theme engine for Qt4/Qt5, KDE and LXQt,
with an emphasis on elegance, usability and practicality.

%prep
%setup -q -n %{oname}-%{version}

%build
cd %{oname}
%cmake_qt5
%make

%install
cd %{oname}
%makeinstall_std -C build

%files
%{_bindir}/kvantummanager
%{_bindir}/kvantumpreview
%{_qt5_plugindir}/styles/libkvantum.so
%{_datadir}/Kvantum
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/color-schemes
%{_datadir}/kde4/apps/color-schemes
%{_iconsdir}/hicolor/scalable/apps/kvantum.svg
%{_datadir}/themes
%lang(eo) %{_datadir}/kvantummanager/translations/kvantummanager_eo.qm
%lang(pl) %{_datadir}/kvantummanager/translations/kvantummanager_pl.qm
%lang(eo) %{_datadir}/kvantumpreview/translations/kvantumpreview_eo.qm
