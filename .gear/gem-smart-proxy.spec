%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname smart_proxy

Name:          gem-smart-proxy
Version:       5.0.1.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart-proxy
Vcs:           https://github.com/theforeman/smart-proxy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       settings.yml
Source2:       smart-proxy.service
Source3:       smart-proxy.conf
Source4:       puppetca_http_api.yml
Source5:       setup-rb-compat.rb
%define __setup_rb GEM_HOME=%ruby_gemhome %__ruby -r%SOURCE5 %ruby_bindir/setup-rb
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: curl
BuildRequires: gem(base64) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(facter) >= 0
BuildRequires: gem(gssapi) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(jwt) >= 0
BuildRequires: gem(logging) >= 0
BuildRequires: gem(logging-journald) >= 2.0
BuildRequires: gem(mocha) >= 1.10
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rb-inotify) >= 0
BuildRequires: gem(rb-kqueue) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(redfish_client) >= 0.8.0
BuildRequires: gem(rexml) >= 3.2
BuildRequires: gem(rkerberos) >= 0.1.1
BuildRequires: gem(rsec) >= 0
BuildRequires: gem(rubocop) >= 1.56.0
BuildRequires: gem(rubocop-performance) >= 1.5.2
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(ruby-libvirt) >= 0.6.0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rubyipmi) >= 0.12.1
BuildRequires: gem(sd_notify) >= 0.1
BuildRequires: gem(sinatra) >= 2.0
BuildRequires: gem(smart_proxy_discovery_image) >= 1.6.0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(webrick) >= 1.0
BuildRequires: gem(xmlrpc) >= 0.2
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(logging-journald) >= 3
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rsec) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(ruby-prof) >= 2
BuildConflicts: gem(sd_notify) >= 1
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(webrick) >= 2
BuildConflicts: gem(xmlrpc) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency ci_reporter >= 1.6.3,ci_reporter < 3
%ruby_use_gem_dependency mocha >= 1.10,mocha < 3
%ruby_use_gem_dependency rsec >= 0,rsec < 2
%ruby_use_gem_dependency rubocop >= 1.56.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.5.2,rubocop-performance < 2
%ruby_use_gem_dependency ruby-prof >= 0,ruby-prof < 2
%ruby_alias_names smart_proxy,smart-proxy
%ruby_regard_path_tokens templates
Requires:      curl
Requires:      railsctl >= 1.0.1-alt2
Requires:      ruby >= 3.0
Requires:      gem(base64) >= 0
Requires:      gem(json) >= 0
Requires:      gem(logging) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(rack) >= 2.0
Requires:      gem(rackup) >= 0
Requires:      gem(rexml) >= 3.2
Requires:      gem(sd_notify) >= 0.1
Requires:      gem(sinatra) >= 2.0
Requires:      gem(smart_proxy_discovery_image) >= 1.6.0
Requires:      gem(webrick) >= 1.0
Conflicts:     gem-smart-proxy-compat
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(sd_notify) >= 1
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(webrick) >= 2
Provides:      gem(smart_proxy) = 5.0.1.1

%ruby_use_gem_version smart_proxy:5.0.1.1

%description
Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy


%package       -n smart-proxy
Version:       5.0.1.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета smart_proxy
Group:         Other
BuildArch:     noarch

Requires:      gem(smart_proxy) = 5.0.1.1
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(smart_proxy_discovery_image) >= 1.6.0
Conflicts:     gem(concurrent-ruby) >= 2

%description   -n smart-proxy
RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet executable(s).

Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy

%description   -n smart-proxy -l ru_RU.UTF-8
Исполнямка для самоцвета smart_proxy.


%if_enabled    doc
%package       -n gem-smart-proxy-doc
Version:       5.0.1.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy) = 5.0.1.1

%description   -n gem-smart-proxy-doc
RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet documentation files.

Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy

%description   -n gem-smart-proxy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy.
%endif


%if_enabled    devel
%package       -n gem-smart-proxy-devel
Version:       5.0.1.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy) = 5.0.1.1
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(facter) >= 0
Requires:      gem(gssapi) >= 0
Requires:      gem(jwt) >= 0
Requires:      gem(logging-journald) >= 2.0
Requires:      gem(mocha) >= 1.10
Requires:      gem(pry) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rb-inotify) >= 0
Requires:      gem(rb-kqueue) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(redfish_client) >= 0.8.0
Requires:      gem(rkerberos) >= 0.1.1
Requires:      gem(rsec) >= 0
Requires:      gem(rubocop) >= 1.56.0
Requires:      gem(rubocop-performance) >= 1.5.2
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(ruby-libvirt) >= 0.6.0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(rubyipmi) >= 0.12.1
Requires:      gem(test-unit) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(xmlrpc) >= 0.2
Conflicts:     gem(ci_reporter) >= 3
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(logging-journald) >= 3
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rsec) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(ruby-prof) >= 2
Conflicts:     gem(xmlrpc) >= 1

%description   -n gem-smart-proxy-devel
RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet development package.

Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy

%description   -n gem-smart-proxy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

#TODO move to baltix
install -dm750 %buildroot%_logdir/smart-proxy \
               %buildroot%_sysconfdir/smart-proxy/config/settings.d \
               %buildroot%_runtimedir/smart-proxy \
               %buildroot%_localstatedir/smart-proxy/
install -m644 %SOURCE1 %buildroot%_sysconfdir/smart-proxy/config/
install -Dm644 %SOURCE2 %buildroot%_unitdir/smart-proxy.service
install -Dm644 %SOURCE3 %buildroot%_tmpfilesdir/smart-proxy.conf
ln -rvs %buildroot%ruby_gemlibdir/Gemfile %buildroot%_localstatedir/smart-proxy/Gemfile
cp -p config/settings.d/*.yml.example %buildroot%_sysconfdir/smart-proxy/config/settings.d
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/smart-proxy/config/settings.d/puppetca_http_api.yml

%check
env ALT_CHECK_GEM_HOME=%buildroot%ruby_gemhome BUNDLE_GEMFILE=%buildroot%ruby_gemlibdir/Gemfile %__ruby .setup/test.rb

%pre           -n smart-proxy
getent group puppet >/dev/null || %_sbindir/groupadd -r puppet
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _smartforeman >/dev/null || \
   %_sbindir/useradd -r -G puppet,foreman -d %_localstatedir/smart-proxy -s /bin/bash -c "Foreman" _smartforeman

%post          -n smart-proxy
rm -rf %_localstatedir/smart-proxy/Gemfile.lock
%post_service  smart-proxy

%preun         -n smart-proxy
%preun_service smart-proxy

%files
%doc README.md CHANGELOG Contributors LICENSE
%ruby_gemspec
%ruby_gemlibdir
%config(noreplace) %_sysconfdir/smart-proxy/config/settings.yml
%config(noreplace) %_sysconfdir/smart-proxy/config/settings.d/*.yml.example
%config(noreplace) %_sysconfdir/smart-proxy/config/settings.d/puppetca_http_api.yml

%files         -n smart-proxy
%doc README.md CHANGELOG Contributors LICENSE
%_bindir/smart-proxy
%_unitdir/smart-proxy.service
%_tmpfilesdir/smart-proxy.conf
%attr(750,_smartforeman,foreman) %_logdir/smart-proxy
%attr(751,_smartforeman,foreman) %_localstatedir/smart-proxy
%attr(751,_smartforeman,foreman) %_runtimedir/smart-proxy

%if_enabled    doc
%files         -n gem-smart-proxy-doc
%doc README.md CHANGELOG Contributors LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-smart-proxy-devel
%doc README.md CHANGELOG Contributors LICENSE
%endif


%changelog
* Tue Nov 10 2026 Pavel Skrylev <majioa@altlinux.org> 5.0.1.1-alt1
- ^ 3.19.2 -> 5.0.1.1
- + require smart_proxy_discovery_image in Gemfile and gem metadata
- ! retain ALT configuration and service integration

* Thu Oct 15 2026 Pavel Skrylev <majioa@altlinux.org> 3.19.2-alt2
- ! fixed deps for Gemfile, removed custom one

* Tue Oct 13 2026 Pavel Skrylev <majioa@altlinux.org> 3.19.2-alt1
- ^ 3.13.0 -> 3.19.2

* Thu Jan 23 2025 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.5.1 -> 3.13.0

* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt3.3
- ! dep to ruby-prof and psych

* Fri Apr 19 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt3.2
- + added dep to rackup
- ! relaxed dep to sinatra gem
- ! fixed service file

* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt3.1
- ! fixed dep to psych to equal or more than 4.0.4

* Mon Apr 10 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt3
- * using railsctl to run service

* Tue Feb 28 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt2
- ! runtime deps to smart_proxy_remote_execution_ssh and smart_proxy_ansible
- * since for now smart-proxy support not the daemonize with pid, change service
  fork type to "exec"

* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.4.0 -> 3.5.1
- ! fixed default smart-proxy.service file

* Fri Sep 16 2022 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- ^ 3.0.0 -> 3.4.0

* Wed Oct 20 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.5.0 -> 3.0.0

* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.1.0 -> 2.5.0

* Mon Nov 30 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2.1
- + requires dep to facter executable
- + explicitly the other required gems to Gemfile as a patch
- + conflicts to compat packages

* Thu Jul 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- + conf file to keep rights on some folders after reset
- + _smartforeman user with home of /var/lib/smart-proxy
- * moving config files to sysconf folder
- ! config dependent code
- ! config syntax

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0
- + _foreman user to puppet group

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt4
- + copy Gemfile to %%_localstatedir/smart-proxy
- + setup foreman user and groups
- - service dep out of the foreman
- ! service work dir

* Thu Jul 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt3
- + settings yamls

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- * dependencies by patch

* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
