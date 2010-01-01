#
# Conditional build:
%bcond_without	opengl	# with OpenGL (reason yet unknown)
%bcond_without	ruby	# embed Ruby
%bcond_with	gtk	# seems to be broken :]
#
Summary:	A sound editor modelled loosely after Emacs
Summary(pl.UTF-8):	Edytor plików dźwiękowych wzorowany na Emacsie
Name:		snd
Version:	7
Release:	1
License:	LGPL
Vendor:		CCRMA/Music Stanford University
Group:		Applications/Sound
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}-%{version}.tar.gz
# Source0-md5:	bb5882fda1be527cd0b6dcae31e081c9
Patch0:		%{name}-ac.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www-ccrma.stanford.edu/software/snd/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_opengl:BuildRequires:	gtkglext-devel}
%{?with_gtk:BuildRequires:	gtk+2-devel}
%{?with_guile:BuildRequires:	guile-devel}
%if %{with ruby}
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snd is a sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd. It can accommodate any
number of sounds each with any number of channels, and can be
customized and extended using Guile or Ruby.

%description -l pl.UTF-8
Snd jest edytorem plików dzwiękowych wzorowanym na Emacsie i
nieodżałowanym Dpysnd z PDP-10. Potrafi obsługiwać dowolną liczbę
plików z dowolną liczbą kanałów i może być rozbudowywany za pomocą
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
	%{?with_gtk:--with-gtk} \
	--with-ladspa \
	%{?with_ruby:--with-ruby} \
	%{?with_opengl:--with-gl} \
	%{!?with_guile:--without-guile}

%{__make} \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.Snd *.html *.png *.scm *.rb tutorial
%attr(755,root,root) %{_bindir}/snd
%{_mandir}/man1/*
