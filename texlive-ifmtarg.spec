# revision 19363
# category Package
# catalog-ctan /macros/latex/contrib/ifmtarg
# catalog-date 2010-07-10 16:47:23 +0200
# catalog-license lppl
# catalog-version 1.2a
Name:		texlive-ifmtarg
Version:	1.2a
Release:	8
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-2
+ Revision: 752693
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-1
+ Revision: 718699
- texlive-ifmtarg
- texlive-ifmtarg
- texlive-ifmtarg
- texlive-ifmtarg

