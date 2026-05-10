Summary: Fork of canonical/lxd-ui for use with Incus
Name: incus-ui-canonical
Version: 0.19.9
Release: %autorelease
License: GPL-3.0
URL: https://github.com/zabbly/incus-ui-canonical

%global debug_package %{nil}

Source0: https://github.com/zabbly/%{name}/archive/refs/tags/incus-%{version}.tar.gz
Source1: %{name}-%{version}-nm-dev.tgz
Source2: %{name}-%{version}-bundled-licenses.txt

BuildRequires: yarnpkg
BuildRequires: nodejs-npm
BuildRequires: nodejs-devel

%description
LXD-UI is a browser frontend for LXD. It enables easy and accessible container and virtual machine management. Targets small and large scale private clouds.

%prep
%autosetup -C
cp %{SOURCE2} .

%build
# Setup bundled node modules
mkdir -p node_modules
tar -C node_modules --strip-components=1 -xzf %{SOURCE1}
# build
yarn build

%install
mkdir -p %{buildroot}%{_datadir}/incus-ui-canonical
cp -a build/ui/. %{buildroot}%{_datadir}/incus-ui-canonical

%files
%license LICENSE %{name}-%{version}-bundled-licenses.txt
%doc README.md
%{_datadir}/incus-ui-canonical

%changelog
%autochangelog
