#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spyder-kernels
Version  : 2.0.2
Release  : 20
URL      : https://files.pythonhosted.org/packages/b4/e3/cd0352b58a2978c4221eccc9c9743265f140de8d33184a3cc4c439eb67dd/spyder-kernels-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/e3/cd0352b58a2978c4221eccc9c9743265f140de8d33184a3cc4c439eb67dd/spyder-kernels-2.0.2.tar.gz
Summary  : Jupyter kernels for Spyder's console
Group    : Development/Tools
License  : MIT
Requires: spyder-kernels-license = %{version}-%{release}
Requires: spyder-kernels-python = %{version}-%{release}
Requires: spyder-kernels-python3 = %{version}-%{release}
Requires: cloudpickle
Requires: decorator
Requires: ipykernel
Requires: ipython
Requires: pyzmq
Requires: wurlitzer
BuildRequires : buildreq-distutils3
BuildRequires : cloudpickle
BuildRequires : decorator
BuildRequires : ipykernel
BuildRequires : ipython
BuildRequires : jupyter_client
BuildRequires : pyzmq
BuildRequires : wurlitzer
Patch1: deps.patch

%description
# Jupyter kernels for the Spyder console
[![Windows status](https://github.com/spyder-ide/spyder-kernels/workflows/Windows%20tests/badge.svg)](https://github.com/spyder-ide/spyder-kernels/actions?query=workflow%3A%22Windows+tests%22)
[![Linux status](https://github.com/spyder-ide/spyder-kernels/workflows/Linux%20tests/badge.svg)](https://github.com/spyder-ide/spyder-kernels/actions?query=workflow%3A%22Linux+tests%22)
[![Macos status](https://github.com/spyder-ide/spyder-kernels/workflows/Macos%20tests/badge.svg)](https://github.com/spyder-ide/spyder-kernels/actions?query=workflow%3A%22Macos+tests%22)
[![codecov](https://codecov.io/gh/spyder-ide/spyder-kernels/branch/master/graph/badge.svg)](https://codecov.io/gh/spyder-ide/spyder-kernels/branch/master)

%package license
Summary: license components for the spyder-kernels package.
Group: Default

%description license
license components for the spyder-kernels package.


%package python
Summary: python components for the spyder-kernels package.
Group: Default
Requires: spyder-kernels-python3 = %{version}-%{release}

%description python
python components for the spyder-kernels package.


%package python3
Summary: python3 components for the spyder-kernels package.
Group: Default
Requires: python3-core
Provides: pypi(spyder_kernels)
Requires: pypi(cloudpickle)
Requires: pypi(decorator)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(pyzmq)
Requires: pypi(wurlitzer)

%description python3
python3 components for the spyder-kernels package.


%prep
%setup -q -n spyder-kernels-2.0.2
cd %{_builddir}/spyder-kernels-2.0.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620049753
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spyder-kernels
cp %{_builddir}/spyder-kernels-2.0.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/spyder-kernels/4d8c327cf6d4ba1ac22d4feb6df04672893016ef
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spyder-kernels/4d8c327cf6d4ba1ac22d4feb6df04672893016ef

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
