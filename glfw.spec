#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glfw
Version  : 3.2.1
Release  : 5
URL      : https://github.com/glfw/glfw/archive/3.2.1.tar.gz
Source0  : https://github.com/glfw/glfw/archive/3.2.1.tar.gz
Summary  : A multi-platform library for OpenGL, window and input
Group    : Development/Tools
License  : BSD-3-Clause
Requires: glfw-lib = %{version}-%{release}
Requires: glfw-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules wayland
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)

%description
# GLFW
[![Build status](https://travis-ci.org/glfw/glfw.svg?branch=master)](https://travis-ci.org/glfw/glfw)
[![Build status](https://ci.appveyor.com/api/projects/status/0kf0ct9831i5l6sp/branch/master?svg=true)](https://ci.appveyor.com/project/elmindreda/glfw)
[![Coverity Scan](https://scan.coverity.com/projects/4884/badge.svg)](https://scan.coverity.com/projects/glfw-glfw)

%package dev
Summary: dev components for the glfw package.
Group: Development
Requires: glfw-lib = %{version}-%{release}
Provides: glfw-devel = %{version}-%{release}

%description dev
dev components for the glfw package.


%package lib
Summary: lib components for the glfw package.
Group: Libraries
Requires: glfw-license = %{version}-%{release}

%description lib
lib components for the glfw package.


%package license
Summary: license components for the glfw package.
Group: Default

%description license
license components for the glfw package.


%prep
%setup -q -n glfw-3.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547752326
mkdir -p clr-build
pushd clr-build
%cmake .. -DLIB_SUFFIX=64
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1547752326
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glfw
cp COPYING.txt %{buildroot}/usr/share/package-licenses/glfw/COPYING.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GLFW/glfw3.h
/usr/include/GLFW/glfw3native.h
/usr/lib64/cmake/glfw3/glfw3Config.cmake
/usr/lib64/cmake/glfw3/glfw3ConfigVersion.cmake
/usr/lib64/cmake/glfw3/glfw3Targets-relwithdebinfo.cmake
/usr/lib64/cmake/glfw3/glfw3Targets.cmake
/usr/lib64/libglfw.so
/usr/lib64/pkgconfig/glfw3.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libglfw.so.3
/usr/lib64/libglfw.so.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glfw/COPYING.txt
