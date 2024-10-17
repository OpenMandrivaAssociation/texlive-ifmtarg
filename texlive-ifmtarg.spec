Name:		texlive-ifmtarg
Version:	47544
Release:	2
Summary:	If-then-else command for processing potentially empty arguments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ifmtarg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmtarg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmtarg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmtarg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ifmtarg package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifmtarg/ifmtarg.sty
%doc %{_texmfdistdir}/doc/latex/ifmtarg/README
%doc %{_texmfdistdir}/doc/latex/ifmtarg/ifmtarg.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifmtarg/ifmtarg.ins
%doc %{_texmfdistdir}/source/latex/ifmtarg/ifmtarg.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
