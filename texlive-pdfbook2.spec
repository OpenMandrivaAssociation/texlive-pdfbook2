%global tl_name pdfbook2
%global tl_revision 76924
%global tl_bin_links pdfbook2:%{_texmfdistdir}/scripts/pdfbook2/pdfbook2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Create booklets from PDF files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/pdfbook2
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfbook2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfbook2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pdfbook2.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This python program creates print-ready PDF files from some input PDF
files for booklet printing. The resulting files need to be printed in
landscape/long edge double sided printing. The default paper format
depends on the locale and is chosen by pdfjam. It can be chosen using
the --paper option. Before the pdf is composed, the input file is
cropped to the relevant area in order to discard unnecessary white
spaces. In this process, all pages are cropped to the same dimensions.
Extra margins can be defined at the edges of the booklet and in the
middle where the binding occurs. The output is written to INPUT-
book.pdf. Existing files will be overwritten. All input files are
processed separately.

