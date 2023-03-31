Name:		texlive-pdfbook2
Version:	53521
Release:	2
Summary:	Create booklets from PDF files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfbook2
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfbook2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfbook2.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This python program creates print-ready PDF files from some
input PDF files for booklet printing. The resulting files need
to be printed in landscape/long edge double sided printing. The
default paper format depends on the locale and is chosen by
pdfjam. It can be chosen using the --paper option. Before the
pdf is composed, the input file is cropped to the relevant area
in order to discard unnecessary white spaces. In this process,
all pages are cropped to the same dimensions. Extra margins can
be defined at the edges of the booklet and in the middle where
the binding occurs. The output is written to INPUT-book.pdf.
Existing files will be overwritten. All input files are
processed seperately.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/pdfbook2
%doc %{_texmfdistdir}/texmf-dist/doc/support/pdfbook2
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfbook2.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfbook2.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
