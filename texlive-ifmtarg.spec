# revision 19363
# category Package
# catalog-ctan /macros/latex/contrib/ifmtarg
# catalog-date 2010-07-10 16:47:23 +0200
# catalog-license lppl
# catalog-version 1.2a
Name:		texlive-ifmtarg
Version:	1.2a
Release:	1
Summary:	If-then-else command for processing potentially empty arguments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifmtarg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmtarg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmtarg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifmtarg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive ifmtarg package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifmtarg/ifmtarg.sty
%doc %{_texmfdistdir}/doc/latex/ifmtarg/README
%doc %{_texmfdistdir}/doc/latex/ifmtarg/ifmtarg.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifmtarg/ifmtarg.ins
%doc %{_texmfdistdir}/source/latex/ifmtarg/ifmtarg.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
