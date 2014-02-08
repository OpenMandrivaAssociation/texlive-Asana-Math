# revision 27228
# category Package
# catalog-ctan /fonts/Asana-Math
# catalog-date 2012-06-11 11:02:36 +0200
# catalog-license ofl
# catalog-version 000.949
Name:		texlive-Asana-Math
Version:	000.949
Release:	2
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


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 000.949-1
+ Revision: 813327
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 000.947-2
+ Revision: 749352
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 000.947-1
+ Revision: 717859
- texlive-Asana-Math
- texlive-Asana-Math
- texlive-Asana-Math
- texlive-Asana-Math
- texlive-Asana-Math
- texlive-Asana-Math

