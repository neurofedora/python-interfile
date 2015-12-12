%global modname interfile

Name:           python-%{modname}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Pyhon module for read/write/parse interfile

# https://github.com/spedemon/interfile/pull/3
# not license text in PyPi archive
License:        BSD
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/i/%{modname}/%{modname}-%{version}.tar.gz
# https://github.com/spedemon/interfile/commit/098b985f04032b65a7c361bc2f943ce237d453ee
Patch0:         0001-Removed-dependence-from-Python-Petlink.patch

BuildArch:      noarch

%description
Interfile is a Python module module that reads, writes and parses files in the
interfile data format. The interfile file format is a format utilized for the
storage of data related to Positron Emission Tomography (PET) and to
Single Photon Emission Computed Tomography (SPECT), such as sinograms and
volumetric imaging data.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python2-simplewrap
Requires:       python2-simplewrap

%description -n python2-%{modname}
Interfile is a Python module module that reads, writes and parses files in the
interfile data format. The interfile file format is a format utilized for the
storage of data related to Positron Emission Tomography (PET) and to
Single Photon Emission Computed Tomography (SPECT), such as sinograms and
volumetric imaging data.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  /usr/bin/2to3
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-simplewrap
Requires:       python3-simplewrap

%description -n python3-%{modname}
Interfile is a Python module module that reads, writes and parses files in the
interfile data format. The interfile file format is a format utilized for the
storage of data related to Positron Emission Tomography (PET) and to
Single Photon Emission Computed Tomography (SPECT), such as sinograms and
volumetric imaging data.

Python 3 version.

%prep
%setup -qc
mv %{modname}-%{version} python2
pushd python2
rm -rf *.egg-info
%patch0 -p1
popd

cp -a python2 python3
2to3 --write --nobackups python3

%build
pushd python2
  %py2_build
popd

pushd python3
  %py3_build
popd

%install
pushd python2
  %py2_install
popd

pushd python3
  %py3_install
popd

%check
pushd python2
  %{__python2} setup.py test
popd

pushd python3
  %{__python2} setup.py test
popd

%files -n python2-%{modname}
%doc python2/README.rst
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc python3/README.rst
%{python3_sitelib}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.1-1
- Initial package
