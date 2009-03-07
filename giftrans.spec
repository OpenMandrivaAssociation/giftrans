Summary: 	Convert transparent GIFs into non-transparent GIFs
Name: 		giftrans
Version: 	1.12.2
Release: 	%mkrel 20
License: 	BSD
Group: 		Graphics
URL:		ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/
Source0: 	%name-%version.tar.bz2
Patch0:		giftrans-1.12.2-operator.patch
Patch1:		giftrans-1.12.2-cleanup.patch
Patch2:		giftrans-1.12.2-warnings.patch
Buildroot: 	%_tmppath/%name-%{version}-buildroot
Requires: rgb

%description
Giftrans will convert an existing GIF87 file to GIF89 format. In other
words, Giftrans can make one color in a .gif image (normally the
background) transparent.

Install the giftrans package if you need a quick, small, one-purpose
graphics program to make transparent .gifs out of existing .gifs.

%prep
%setup -q
%patch0 -p1 -b .operator
%patch1 -p1
%patch2 -p1

%build
gcc -Dvoidd=void -Wall $RPM_OPT_FLAGS -DRGBTXT=\"%_datadir/X11/rgb.txt\" -s -o giftrans giftrans.c

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%_bindir/%{name}
install -m644 %{name}.1 -D $RPM_BUILD_ROOT%_mandir/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT
 

%files
%defattr(-,root,root)
%_bindir/%name
%_mandir/man1/%{name}.1*

