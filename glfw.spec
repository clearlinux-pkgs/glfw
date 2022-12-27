#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glfw
Version  : 3.3.8
Release  : 10
URL      : https://github.com/glfw/glfw/archive/3.3.8/glfw-3.3.8.tar.gz
Source0  : https://github.com/glfw/glfw/archive/3.3.8/glfw-3.3.8.tar.gz
Summary  : A multi-platform library for OpenGL, window and input
Group    : Development/Tools
License  : Zlib
Requires: glfw-lib = %{version}-%{release}
Requires: glfw-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules wayland
BuildRequires : extra-cmake-modules-data
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)

%description
# GLFW
[![Build status](https://github.com/glfw/glfw/actions/workflows/build.yml/badge.svg)](https://github.com/glfw/glfw/actions)
[![Build status](https://ci.appveyor.com/api/projects/status/0kf0ct9831i5l6sp/branch/master?svg=true)](https://ci.appveyor.com/project/elmindreda/glfw)
[![Coverity Scan](https://scan.coverity.com/projects/4884/badge.svg)](https://scan.coverity.com/projects/glfw-glfw)

%package dev
Summary: dev components for the glfw package.
Group: Development
Requires: glfw-lib = %{version}-%{release}
Provides: glfw-devel = %{version}-%{release}
Requires: glfw = %{version}-%{release}

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
%setup -q -n glfw-3.3.8
cd %{_builddir}/glfw-3.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672174326
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DLIB_SUFFIX=64
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1672174326
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glfw
cp %{_builddir}/glfw-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/glfw/55822a091dca212023dfde6e6fb53df49288dbd8
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
/usr/lib64/libglfw.so.3.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glfw/55822a091dca212023dfde6e6fb53df49288dbd8
