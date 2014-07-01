Summary: A server daemon with D-Bus interface providing a server roles
Name: rolekit
Version: 0.0.1
Release: 1%{?dist}
URL: http://fedorahosted.org/rolekit
License: GPLv2+
Source0: https://fedorahosted.org/released/rolekit/%{name}-%{version}.tar.bz2
BuildArch: noarch
BuildRequires: gettext
BuildRequires: intltool
# glib2-devel is needed for gsettings.m4
BuildRequires: glib2, glib2-devel
BuildRequires: systemd-units
BuildRequires: docbook-style-xsl
Requires: dbus-python
Requires: python-slip-dbus
Requires: python-decorator
Requires: pygobject3-base
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
rolekit is a server daemon that provides a D-Bus interface and server roles.

%prep
%setup -q

%build
%configure

%install
make install DESTDIR=%{buildroot}

%find_lang %{name} --all-name

%post
%systemd_post rolekit.service

%preun
%systemd_preun rolekit.service

%postun
%systemd_postun_with_restart rolekit.service 


%files -f %{name}.lang
%doc COPYING README
%{_sbindir}/roled
%{_bindir}/rolectl
%defattr(-,root,root)
%dir %{_sysconfdir}/rolekit
%dir %{_sysconfdir}/rolekit/roles
%dir %{_prefix}/lib/rolekit
%dir %{_prefix}/lib/rolekit/roles
%config(noreplace) %{_sysconfdir}/sysconfig/rolekit
%{_unitdir}/rolekit.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/rolekit1.conf
%{_datadir}/polkit-1/actions/org.fedoraproject.Rolekit1.policy
%attr(0755,root,root) %dir %{python_sitelib}/rolekit
%attr(0755,root,root) %dir %{python_sitelib}/rolekit/config
%attr(0755,root,root) %dir %{python_sitelib}/rolekit/server
%attr(0755,root,root) %dir %{python_sitelib}/rolekit/server/io
%{python_sitelib}/rolekit/*.py*
%{python_sitelib}/rolekit/config/*.py*
%{python_sitelib}/rolekit/server/*.py*
%{python_sitelib}/rolekit/server/io/*.py*
%{_mandir}/man1/rolekitctl*.1*
%{_mandir}/man1/rolekit*.1*


%changelog
* Fri May 23 2014 Thomas Woerner <twoerner@redhat.com> 0.1-1
- initial package (proof of concept implementation)
