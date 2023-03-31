Name:		texlive-Asana-Math
Version:	59629
Release:	2
Summary:	A font to typeset maths in Xe(La)TeX and Lua(La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/Asana-Math
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asana-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asana-math.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/opentype/public/asana-math
%{_texmfdistdir}/fonts/truetype/public/asana-math
%doc %{_texmfdistdir}/doc/fonts/asana-math

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
