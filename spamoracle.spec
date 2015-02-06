Name: spamoracle
Version: 1.4
Release: 10
Group: Networking/Mail
Summary: Spam filter based on statistical analysis of e-mail contents
License: GPL
Url: http://pauillac.inria.fr/~xleroy/software.html#spamoracle
Source: http://pauillac.inria.fr/~xleroy/software/spamoracle-%version.tar.bz2
BuildRequires: ocaml
Buildroot: %_tmppath/%name-%version-buildroot

%description
SpamOracle is a tool to help detect and filter away "spam"
(unsolicited commercial e-mail).  It proceeds by statistical analysis
of the words that appear in the e-mail, comparing the frequencies of
words with those found in a user-provided corpus of known spam and
known legitimate e-mail.  The classification algorithm is based on
Bayes' formula, and is described in Paul Graham's paper, "A plan for
spam", http://www.paulgraham.com/spam.html.

%prep
%setup -q

%build
%make

%install
rm -rf %buildroot
mkdir -p %buildroot/{%_bindir,%_mandir/{man1,man5}}
%makeinstall BINDIR=%buildroot/%_bindir MANDIR=%buildroot/%_mandir

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%_bindir/spamoracle
%_mandir/man1/spamoracle.1*
%_mandir/man5/spamoracle.conf.5*




%changelog
* Thu Sep 22 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-9mdv2012.0
+ Revision: 700801
- rebuild

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.4-8mdv2011.0
+ Revision: 445186
- rebuild

* Tue Jan 06 2009 Florent Monnier <blue_prawn@mandriva.org> 1.4-7mdv2009.1
+ Revision: 325808
- removed procmail dep (can be used with anything)

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.4-7mdv2009.0
+ Revision: 260916
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 252898
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Fri Nov 24 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-4mdv2007.0
+ Revision: 86893
- Import spamoracle

* Fri Nov 24 2006 Götz Waschk <waschk@mandriva.org> 1.4-4mdv2007.1
- rebuild

* Tue Nov 08 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-3mdk
- Rebuild

* Fri Nov 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.4-2mdk
- rebuild

