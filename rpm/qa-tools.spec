Name:       qa-tools
Summary:    Test tools for QA
Version:    0.0.1
Release:    1
License:    GPLv2
URL:        https://github.com/mer-qa/qa-tools
Source0:    %{name}-%{version}.tar.gz

%description
Tools for handling on device QA testing.

%package hooks
Summary: First startup hooks for QA
BuildArch: noarch
BuildRequires: oneshot
Requires: oneshot
Requires(post): /usr/bin/ssu
Requires: ssu
Requires: jolla-preload-ambiences-default-ambience
%{_oneshot_requires_post}
# Removed in JB#49024 / JB#35113
Obsoletes: jolla-firstsession-qa <= 0.50

%description hooks
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/sbin/reboot-tool

%files hooks
%defattr(-,root,root,-)
%{_oneshotdir}/*
%{_sysconfdir}/sysctl.d/*
%{_sysconfdir}/sailjail/config/*.conf
%{_sysconfdir}/mce/*.conf

%post hooks
if [ "$1" -eq 1 ]; then
    %{_bindir}/add-oneshot 10-enable-qa-repo 11-set-default-locale 14-enable-core-dumping
    %{_bindir}/add-oneshot --late 12-disable-als 13-set-max-brightness
    %{_bindir}/add-oneshot --new-users 09-disable-startup-wizard 18-set-first-boot-dconf 19-set-time-format-dconf 20-disable-hints-and-tips-dconf
fi
