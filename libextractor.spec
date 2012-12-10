%define realname extractor

%define major 3
%define common_major 1
%define libname %mklibname %{realname} %{major}
%define libcommon %mklibname extractor_common %{common_major}
%define libnamedev %mklibname %{realname} -d
%define libnamedev_static %mklibname %{realname} -d -s

Summary:	Library used to extract meta-data from files
Name:		libextractor
Version:1.0.1
Release:	1
License:	BSD
Group:		System/Libraries
URL:		http://www.gnunet.org/libextractor/
Source0:	http://ftpmirror.gnu.org/libextractor/%{name}-%{version}.tar.gz
Patch0:		libextractor-0.6.2-rpm5.patch
Conflicts:	%{mklibname extractor 1} < 0.5.19a-2
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	pkgconfig(zlib)
BuildRequires:	bzip2-devel
BuildRequires:	libtool-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(rpm)
BuildRequires:	gettext-devel


%description
libextractor is a library used to extract meta-data from files of arbitrary 
type. It is designed to use helper-libraries to perform the actual extraction, 
and to be trivially extendable by linking against external extractors for 
additional file types. The goal is to provide developers of file-sharing 
networks or WWW-indexing bots with a universal library to obtain simple 
keywords to match against queries. libextractor contains a shell-command 
"extract" that, similar to the well-known "file" command, can extract meta-data
from a file and print the results to stdout. Currently, it supports the formats
HTML, PDF, PS, MP3, OGG, JPEG, GIF, PNG, RPM, ZIP, Real, QT and ASF. Also, 
various additional MIME types are detected.

%package -n	%{libname}
Summary:	Libextractor library used to extract meta-data from files 
Group:		System/Libraries
Conflicts:	%{mklibname -d extractor 1} < 0.5.19a-2

%description -n	%{libname}
libextractor is a library used to extract meta-data from files of arbitrary 
type. It is designed to use helper-libraries to perform the actual extraction, 
and to be trivially extendable by linking against external extractors for 
additional file types. The goal is to provide developers of file-sharing 
networks or WWW-indexing bots with a universal library to obtain simple 
keywords to match against queries. libextractor contains a shell-command 
"extract" that, similar to the well-known "file" command, can extract meta-data
from a file and print the results to stdout. Currently, it supports the formats
HTML, PDF, PS, MP3, OGG, JPEG, GIF, PNG, RPM, ZIP, Real, QT and ASF. Also, 
various additional MIME types are detected.

%package -n	%{libcommon}
Summary:        Libextractor library for common functions
Group:          System/Libraries

%description -n	%{libcommon}
Common function library of libextractor.

%package -n	%{libnamedev}
Summary:	Libextractor library headers and development libraries
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libcommon} = %{version}-%{release}
Provides:	libextractor-devel = %{version}-%{release}
Provides:	extractor-devel = %{version}-%{release}
Obsoletes:	%mklibname -d extractor 1

%description -n	%{libnamedev}
Development files and headers for libextractor.


%package -n	%{libnamedev_static}
Summary:	Libextractor library headers and development libraries
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libcommon} = %{version}-%{release}
Requires:	extractor-devel = %{version}-%{release}
Provides:	libextractor-static-devel = %{version}-%{release}
Provides:	extractor-static-devel = %{version}-%{release}

%description -n	%{libnamedev_static}
Development static libs for libextractor.

%prep
%setup -q 
%patch0 -p1 -b .rpm5~

%build
autoreconf -fi
%configure2_5x \
	--disable-rpath \
	--enable-exiv2 \
	--disable-ffmpeg \
	--with-plugindirname=%{name}%{major}

make
%install
%makeinstall_std

find %{buildroot} -name *.la -delete

%find_lang %{name}

%post
%_install_info libextractor

%preun
%_remove_install_info libextractor

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_infodir}/*

%files -n %{libname}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/%{name}%{major}

%files -n %{libcommon}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/%{name}_common.so.%{common_major}*

%files -n %{libnamedev}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/%{name}.so
%{_libdir}/%{name}_common.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n %{libnamedev_static}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/*.a
