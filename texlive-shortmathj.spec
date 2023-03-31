Name:		texlive-shortmathj
Version:	54407
Release:	2
Summary:	Automatically shortify titles of mathematical journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shortmathj
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shortmathj.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shortmathj.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small dummy package just contains a simple list of full
and short journal names aswritten in AMS standard:
https://mathscinet.ams.org/msnhtml/serials.pdf

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/shortmathj
%doc %{_texmfdistdir}/doc/latex/shortmathj

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
