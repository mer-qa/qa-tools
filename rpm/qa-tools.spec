Name:       qa-tools
Summary:    Test tools for QA
Version:    0.0.1
Release:    1
Group:      Development/Tools
License:    GPLv2
URL:        https://github.com/mer-qa/qa-tools
Source0:    %{name}-%{version}.tar.gz

%description
Tools for handling on device QA testing

%prep
%setup -q -n %{name}-%{version}

%build
make %{?jobs:-j%jobs}

%install
%make_install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/sbin/reboot-tool
