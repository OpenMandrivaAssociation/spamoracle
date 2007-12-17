Name: spamoracle
Version: 1.4
Release: %mkrel 4
Group: Networking/Mail
Summary: Spam filter based on statistical analysis of e-mail contents
License: GPL
Url: http://pauillac.inria.fr/~xleroy/software.html#spamoracle
Source: http://pauillac.inria.fr/~xleroy/software/spamoracle-%version.tar.bz2
BuildRequires: ocaml
Requires: procmail

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


