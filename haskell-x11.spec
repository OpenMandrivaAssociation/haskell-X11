%define module X11

Name: haskell-%{module}
Version: 1.4.6.1
Release: %mkrel 3
Summary: A binding to the X11 graphics library
Group: Development/Other
License: BSD3
Url: https://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{module}
Source: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{module}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell-macros
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: libx11-devel
BuildRequires: libxinerama-devel
BuildRequires: x11-proto-devel
Requires: ghc
Requires(preun): ghc
Requires(post): ghc

%description
A Haskell binding to the X11 graphics library.

The binding is a direct translation of the C binding; for
documentation of these calls, refer to "The Xlib Programming
Manual", available online at <http://tronche.com/gui/x/xlib/>.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%{_docdir}/%{module}-%{version}/*
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot
