%define debug_package %nil

Summary: 	Convert transparent GIFs into non-transparent GIFs
Name: 		giftrans
Version: 	1.12.2
Release: 	%mkrel 26
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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.12.2-24mdv2011.0
+ Revision: 664832
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12.2-23mdv2011.0
+ Revision: 605456
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12.2-22mdv2010.1
+ Revision: 522727
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.12.2-21mdv2010.0
+ Revision: 424879
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.12.2-20mdv2009.1
+ Revision: 351206
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.12.2-19mdv2009.0
+ Revision: 221072
- rebuild

* Fri Mar 28 2008 Götz Waschk <waschk@mandriva.org> 1.12.2-18mdv2008.1
+ Revision: 190854
- drop patch 3
- fix path of rgb.txt (bug #35065)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.12.2-17mdv2008.1
+ Revision: 150108
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 1.12.2-16mdv2008.0
+ Revision: 91252
- rebuild for 2008


* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.12.2-15mdv2007.0
+ Revision: 114510
- Import giftrans

* Sun Jan 28 2007 G�tz Waschk <waschk@mandriva.org> 1.12.2-15mdv2007.1
- unpack patches

* Thu May 18 2006 Jerome Soyer <saispo@mandriva.org> 1.12.2-15mdk
- Rebuild for new xorg
- Use mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.12.2-14mdk
- Rebuild

