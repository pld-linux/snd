
%bcond_without	ruby	# embed Rubby
%bcond_without	gl	# with opengl (reason yet unknown)

Summary:	A sound editor modelled loosely after Emacs
Summary(pl):	Edytor plików dzwiêkowych wzorowany na Emacsie
Name:		snd
Version:	7
Release:	1
License:	LGPL
Group:		Applications/Sound
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}-%{version}.tar.gz
# Source0-md5:	bb5882fda1be527cd0b6dcae31e081c9
Patch0:		%{name}-ac.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www-ccrma.stanford.edu/software/snd/
Vendor:		CCRMA/Music Stanford University
#%{?with_ruby:BuildRequires:	ruby-devel}
%{?with_ruby:BuildRequires:	ruby}
%{?with_gl:BuildRequires:	gtkglext-devel}
%{?with_guile:BuildRequires:	guile-devel}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snd is a sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd. It can accommodate any
number of sounds each with any number of channels, and can be
customized and extended using Guile or Ruby.

%description -l pl
Snd jest edytorem plików dzwiêkowych wzorowanym na Emacsie i
nieod¿a³owanym Dpysnd z PDP-10. Potrafi obs³ugiwaæ dowoln± liczbê
plików z dowoln± liczb± kana³ów i mo¿e byæ rozbudowywany za pomoc±
Guile lub Ruby.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-alsa \
	--with-gtk \
	--with-ladspa \
	%{?with_ruby:--with-ruby} \
	--with-gl \
	%{?without_guile:--without-guile}

%{__make} \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_bindir}
#install snd $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.Snd *.html *.png *.scm *.rb tutorial/
%attr(755,root,root) %{_bindir}/snd
%{_mandir}/man1/*
