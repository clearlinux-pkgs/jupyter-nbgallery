#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter-nbgallery
Version  : 0.2.4
Release  : 3
URL      : http://pypi.debian.net/jupyter-nbgallery/jupyter-nbgallery-0.2.4.tar.gz
Source0  : http://pypi.debian.net/jupyter-nbgallery/jupyter-nbgallery-0.2.4.tar.gz
Summary  : Jupyter extensions to add nbgallery integration
Group    : Development/Tools
License  : MIT
Requires: jupyter-nbgallery-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the jupyter-nbgallery package.
Group: Default

%description python
python components for the jupyter-nbgallery package.


%prep
%setup -q -n jupyter-nbgallery-0.2.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488815501
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488815501
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
