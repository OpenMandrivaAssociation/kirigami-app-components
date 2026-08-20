Name:		kirigami-app-components
Version:	1.0.2
Release:	1
Source0:	https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Summary:	Kirigami addons for full-featured KDE applications
URL:		https://invent.kde.org/libraries/kirigami-app-components
License:	LGPLv2+
Group:		System/Libraries
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6KirigamiPlatform)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	qml(org.kde.ki18n)

%description
Kirigami addons and modules needed to write a full-featured KDE
application, such as configurable keyboard shortcuts and standard
actions.

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description devel
Header files and CMake config for %{name}.

%files
%{_libdir}/libKirigamiActionCollection.so.*
%{_qtdir}/qml/org/kde/kirigami/actioncollection

%files devel
%{_includedir}/KF6/Kirigami/ActionCollection
%{_libdir}/libKirigamiActionCollection.so
%{_libdir}/cmake/KF6KirigamiAppComponents
