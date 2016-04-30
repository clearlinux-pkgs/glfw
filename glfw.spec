#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glfw
Version  : 3.1.2
Release  : 4
URL      : https://github.com/glfw/glfw/archive/3.1.2.tar.gz
Source0  : https://github.com/glfw/glfw/archive/3.1.2.tar.gz
Summary  : A multi-platform library for OpenGL, window and input
Group    : Development/Tools
License  : Zlib
Requires: glfw-lib
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xrandr)

%description
# GLFW
## Introduction
GLFW is a free, Open Source, multi-platform library for OpenGL and OpenGL ES
application development.  It provides a simple, platform-independent API for
creating windows and contexts, reading input, handling events, etc.

%package dev
Summary: dev components for the glfw package.
Group: Development
Requires: glfw-lib
Provides: glfw-devel

%description dev
dev components for the glfw package.


%package lib
Summary: lib components for the glfw package.
Group: Libraries

%description lib
lib components for the glfw package.


%prep
%setup -q -n glfw-3.1.2

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DLIB_SUFFIX=64
make V=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/glfw/glfw3Config.cmake
/usr/lib64/cmake/glfw/glfw3ConfigVersion.cmake
/usr/lib64/cmake/glfw/glfwTargets-noconfig.cmake
/usr/lib64/cmake/glfw/glfwTargets.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/GLFW/glfw3.h
/usr/include/GLFW/glfw3native.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
