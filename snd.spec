#
# Conditional build:
%bcond_without	gl	# with OpenGL (reason yet unknown)
%bcond_without	ruby	# embed Ruby
%bcond_with	gtk	# seems to be broken :]
#
Summary:	A sound editor modelled loosely after Emacs
Summary(pl):	Edytor plik�w d�wi�kowych wzorowany na Emacsie
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
BuildRequires:	alsa-devel
%{?with_gl:BuildRequires:	gtkglext-devel}
%{?with_gtk:BuildRequires:	gtk+2-devel}
%{?with_guile:BuildRequires:	guile-devel}
%{?with_ruby:BuildRequires:	ruby}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snd is a sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd. It can accommodate any
number of sounds each with any number of channels, and can be
customized and extended using Guile or Ruby.

%description -l pl
Snd jest edytorem plik�w dzwi�kowych wzorowanym na Emacsie i
nieod�a�owanym Dpysnd z PDP-10. Potrafi obs�ugiwa� dowoln� liczb�
plik�w z dowoln� liczb� kana��w i mo�e by� rozbudowywany za pomoc�
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
	%{?with_gl:--with-gl} \
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
