Name:		texlive-plantslabels
Version:	29803
Release:	1
Summary:	Write labels for plants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plantslabels
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plantslabels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plantslabels.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
