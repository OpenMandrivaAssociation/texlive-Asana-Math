# revision 31750
# category Package
# catalog-ctan /fonts/Asana-Math
# catalog-date 2013-09-22 21:43:13 +0200
# catalog-license ofl
# catalog-version 000.951
Name:		texlive-Asana-Math
Version:	000.951
Release:	4
Summary:	A font to typeset maths in Xe(La)TeX and Lua(La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/Asana-Math
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Asana-Math.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Asana-Math.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Asana-Math font is an OpenType font that includes almost
all mathematical Unicode symbols and it can be used to typeset
mathematical text with any software that can understand the
MATH OpenType table (e.g., XeTeX 0.997 and Microsoft Word
2007). The font is beta software. Typesetting support for use
with LaTeX is provided by the fontspec and unicode-math
packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/Asana-Math/Asana-Math.otf
%{_texmfdistdir}/fonts/truetype/public/Asana-Math/Asana-Math.ttf
%doc %{_texmfdistdir}/doc/fonts/Asana-Math/FontLog.txt
%doc %{_texmfdistdir}/doc/fonts/Asana-Math/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
