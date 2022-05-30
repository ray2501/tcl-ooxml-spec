%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define packagename ooxml

Name:          tcl-ooxml
Summary:       ECMA-376 Office Open XML File Formats for Tcl
Version:       1.6.1
Release:       0
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        %{packagename}-version-%{version}.tar.gz
URL:           https://github.com/aschoepe/ooxml
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.6.7
Requires:      tcl >= 8.6.7
Requires:      tclvfs >= 1.4.2
Requires:      tdom >= 0.9.0
BuildRoot:     %{buildroot}

%description
This package contains several commands to edit Excel files.
Read and Write Office Open XML "XLSX" since Excel 2007.

%prep
%setup -q -n %{packagename}-version-%{version}

%build
%{__autoconf}
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{_libdir}
make

%install
make pkglibdir=%{buildroot}%tcl_noarchdir/%{packagename}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%tcl_noarchdir/%{packagename}%{version}

%changelog

