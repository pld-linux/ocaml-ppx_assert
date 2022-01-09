#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Assert-like extension nodes that raise useful errors on failure
Summary(pl.UTF-8):	Węzły rozszerzenia w stylu assert, podnoszące przydatne błędy przy niepowodzeniu
Name:		ocaml-ppx_assert
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_assert/tags
Source0:	https://github.com/janestreet/ppx_assert/archive/v%{version}/ppx_assert-%{version}.tar.gz
# Source0-md5:	0887501620f6988de659b669b7741209
URL:		https://github.com/janestreet/ppx_assert
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_cold-devel >= 0.14
BuildRequires:	ocaml-ppx_cold-devel < 0.15
BuildRequires:	ocaml-ppx_compare-devel >= 0.14
BuildRequires:	ocaml-ppx_compare-devel < 0.15
BuildRequires:	ocaml-ppx_here-devel >= 0.14
BuildRequires:	ocaml-ppx_here-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Assert-like extension nodes that raise useful errors on failure.

This package contains files needed to run bytecode executables using
ppx_assert library.

%description -l pl.UTF-8
Węzły rozszerzenia w stylu assert, podnoszące przydatne błędy przy
niepowodzeniu.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_assert.

%package devel
Summary:	Assert-like extension nodes that raise useful errors on failure - development part
Summary(pl.UTF-8):	Węzły rozszerzenia w stylu assert, podnoszące przydatne błędy przy niepowodzeniu - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_cold-devel >= 0.14
Requires:	ocaml-ppx_compare-devel >= 0.14
Requires:	ocaml-ppx_here-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_assert library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_assert.

%prep
%setup -q -n ppx_assert-%{version}

%build
dune build --release --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_assert/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_assert/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_assert

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_assert
%attr(755,root,root) %{_libdir}/ocaml/ppx_assert/ppx.exe
%{_libdir}/ocaml/ppx_assert/META
%{_libdir}/ocaml/ppx_assert/*.cma
%dir %{_libdir}/ocaml/ppx_assert/runtime-lib
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_assert/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_assert/runtime-lib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_assert/*.cmi
%{_libdir}/ocaml/ppx_assert/*.cmt
%{_libdir}/ocaml/ppx_assert/*.cmti
%{_libdir}/ocaml/ppx_assert/*.mli
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.cmti
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.cmt
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_assert/ppx_assert.a
%{_libdir}/ocaml/ppx_assert/*.cmx
%{_libdir}/ocaml/ppx_assert/*.cmxa
%{_libdir}/ocaml/ppx_assert/runtime-lib/ppx_assert_lib.a
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_assert/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_assert/dune-package
%{_libdir}/ocaml/ppx_assert/opam
