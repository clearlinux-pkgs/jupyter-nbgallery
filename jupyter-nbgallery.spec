#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter-nbgallery
Version  : 0.2.6
Release  : 21
URL      : https://files.pythonhosted.org/packages/69/8e/8839220b78f65674939ad863da591b811ec4c3abf5e2e27f3658249917cc/jupyter-nbgallery-0.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/8e/8839220b78f65674939ad863da591b811ec4c3abf5e2e27f3658249917cc/jupyter-nbgallery-0.2.6.tar.gz
Summary  : Jupyter extensions to add nbgallery integration
Group    : Development/Tools
License  : MIT
Requires: jupyter-nbgallery-python = %{version}-%{release}
Requires: jupyter-nbgallery-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Overview
This Jupyter extension enables integration with [nbgallery](https://nbgallery.github.io).  More information is available [here](https://github.com/nbgallery/nbgallery/blob/master/docs/jupyter_integration.md) in the nbgallery github project.

%package python
Summary: python components for the jupyter-nbgallery package.
Group: Default
Requires: jupyter-nbgallery-python3 = %{version}-%{release}

%description python
python components for the jupyter-nbgallery package.


%package python3
Summary: python3 components for the jupyter-nbgallery package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter-nbgallery package.


%prep
%setup -q -n jupyter-nbgallery-0.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552068454
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
