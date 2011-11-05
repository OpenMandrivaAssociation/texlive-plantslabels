# revision 17831
# category Package
# catalog-ctan /macros/latex/contrib/plantslabels
# catalog-date 2010-04-14 18:13:33 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-plantslabels
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a command \plant, which has three mandatory
and seven optional argument. The package uses the labels.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
