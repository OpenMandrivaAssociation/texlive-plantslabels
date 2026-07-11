%global tl_name plantslabels
%global tl_revision 29803

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Write labels for plants
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/plantslabels
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plantslabels.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plantslabels.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a command \plant, which has three mandatory and
seven optional argument. The package uses the labels

