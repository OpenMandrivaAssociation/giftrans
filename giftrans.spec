%define debug_package %nil

Summary: 	Convert transparent GIFs into non-transparent GIFs
Name: 		giftrans
Version: 	1.12.2
Release: 	31
License: 	BSD
Group: 		Graphics
Url:		ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/
Source0: 	%{name}-%{version}.tar.bz2
Patch0:		giftrans-1.12.2-operator.patch
Patch1:		giftrans-1.12.2-cleanup.patch
Patch2:		giftrans-1.12.2-warnings.patch
Requires: rgb

%description
Giftrans will convert an existing GIF87 file to GIF89 format. In other
words, Giftrans can make one color in a .gif image (normally the
background) transparent.

Install the giftrans package if you need a quick, small, one-purpose
graphics program to make transparent .gifs out of existing .gifs.

%prep
%setup -q
%apply_patches

%build
gcc -Dvoidd=void -Wall $RPM_OPT_FLAGS -DRGBTXT=\"%{_datadir}/X11/rgb.txt\" -s -o giftrans giftrans.c

%install
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

