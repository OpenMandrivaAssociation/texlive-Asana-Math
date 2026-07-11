%global tl_name asana-math
%global tl_revision 76895

Name:		texlive-%{tl_name}
Epoch:		1
Version:	000.962
Release:	%{tl_revision}.1
Summary:	A font to typeset maths in Xe(La)TeX and Lua(La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/Asana-Math
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asana-math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asana-math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Asana-Math font is an OpenType font that includes almost all
mathematical Unicode symbols and it can be used to typeset mathematical
text with any software that can understand the MATH OpenType table
(e.g., XeTeX 0.997 and Microsoft Word 2007). The font is beta software.
Typesetting support for use with LaTeX is provided by the fontspec and
unicode-math packages.

