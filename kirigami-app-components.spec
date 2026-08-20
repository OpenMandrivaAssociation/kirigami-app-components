%define libname %mklibname KirigamiActionCollection
%define devname %mklibname KirigamiActionCollection -d

Name:		kirigami-app-components
Version:	1.0.2
Release:	2
Source0:	https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Summary:	Kirigami addons for full-featured KDE applications
URL:		https://invent.kde.org/libraries/kirigami-app-components
License:	LGPLv2+
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
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

%package -n %{libname}
Summary:	Kirigami ActionCollection library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Shared ActionCollection library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
%rename		kirigami-app-components-devel

%description -n %{devname}
Header files and CMake config for %{name}.

%files
%{_qtdir}/qml/org/kde/kirigami/actioncollection

%files -n %{libname}
%{_libdir}/libKirigamiActionCollection.so.*

%files -n %{devname}
%{_includedir}/KF6/Kirigami/ActionCollection
%{_libdir}/libKirigamiActionCollection.so
%{_libdir}/cmake/KF6KirigamiAppComponents
