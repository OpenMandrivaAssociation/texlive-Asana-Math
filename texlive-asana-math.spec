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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Asana-Math font is an OpenType font that includes almost all
mathematical Unicode symbols and it can be used to typeset mathematical
text with any software that can understand the MATH OpenType table
(e.g., XeTeX 0.997 and Microsoft Word 2007). The font is beta software.
Typesetting support for use with LaTeX is provided by the fontspec and
unicode-math packages.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/doc/fonts/asana-math
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/opentype/public/asana-math
%dir %{_datadir}/texmf-dist/fonts/truetype/public/asana-math
%doc %{_datadir}/texmf-dist/doc/fonts/asana-math/FontLog.txt
%doc %{_datadir}/texmf-dist/doc/fonts/asana-math/README
%{_datadir}/texmf-dist/fonts/opentype/public/asana-math/Asana-Math.otf
%{_datadir}/texmf-dist/fonts/truetype/public/asana-math/ASANA.TTC
