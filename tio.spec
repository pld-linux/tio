Summary:	A simple serial device I/O tool
Name:		tio
Version:	1.46
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	49b0af6ecc124193a4b50f3a81368708
URL:		https://github.com/tio/tio
BuildRequires:	inih-devel
BuildRequires:	linux-libc-headers >= 7:2.6.20
BuildRequires:	meson >= 0.53.2
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tio is a simple serial device tool which features a straightforward
command-line and configuration file interface to easily connect to
serial TTY devices for basic I/O operations.

%prep
%setup -q

%build
%meson build \
	-Dbashcompletiondir=%{bash_compdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/tio
%{_mandir}/man1/tio.1*
# %{bash_compdir}/%{name}
