# revision 17831
# category Package
# catalog-ctan /macros/latex/contrib/plantslabels
# catalog-date 2010-04-14 18:13:33 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-plantslabels
Version:	1.0
Release:	3
Summary:	Write labels for plants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plantslabels
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plantslabels.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plantslabels.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command \plant, which has three mandatory
and seven optional argument. The package uses the labels.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/plantslabels/plantslabels.sty
%doc %{_texmfdistdir}/doc/latex/plantslabels/README
%doc %{_texmfdistdir}/doc/latex/plantslabels/doc/pdf/plantslabels.pdf
%doc %{_texmfdistdir}/doc/latex/plantslabels/doc/tex/Makefile
%doc %{_texmfdistdir}/doc/latex/plantslabels/doc/tex/perso.ist
%doc %{_texmfdistdir}/doc/latex/plantslabels/doc/tex/plantslabels.forlisting
%doc %{_texmfdistdir}/doc/latex/plantslabels/doc/tex/plantslabels.tex
%doc %{_texmfdistdir}/doc/latex/plantslabels/example/pdf/example.pdf
%doc %{_texmfdistdir}/doc/latex/plantslabels/example/tex/cactus.eps
%doc %{_texmfdistdir}/doc/latex/plantslabels/example/tex/example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754976
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719272
- texlive-plantslabels
- texlive-plantslabels
- texlive-plantslabels
- texlive-plantslabels

