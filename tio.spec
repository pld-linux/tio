Summary:	A simple serial device I/O tool
Name:		tio
Version:	3.8
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	a5ba7e11324c8355cf4e3e1f9f61b82e
URL:		https://github.com/tio/tio
BuildRequires:	glib2-devel
BuildRequires:	linux-libc-headers >= 7:2.6.20
BuildRequires:	lua-devel >= 5.1
BuildRequires:	meson >= 0.53.2
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tio is a simple serial device tool which features a straightforward
command-line and configuration file interface to easily connect to
serial TTY devices for basic I/O operations.

%package -n bash-completion-tio
Summary:	bash-completion for tio
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-tio
bash-completion for tio.

%prep
%setup -q

%build
%meson \
	-Dbashcompletiondir=%{bash_compdir}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/tio
%{_mandir}/man1/tio.1*

%files -n bash-completion-tio
%defattr(644,root,root,755)
%{bash_compdir}/tio
