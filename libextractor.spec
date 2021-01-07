%define major 2
%define common_major 1
%define libname %mklibname extractor %{major}
%define libcommon %mklibname extractor_common %{common_major}
%define devname %mklibname extractor -d

Summary:	Library used to extract meta-data from files
Name:		libextractor
Version:	1.10
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://www.gnunet.org/libextractor/
Source0:	http://ftpmirror.gnu.org/libextractor/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	gettext-devel
BuildRequires:	libtool-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(rpm)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

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

%files -f %{name}.lang
%{_bindir}/extract
%{_mandir}/man1/extract.1.*
%{_mandir}/man3/libextractor.3.*
%{_infodir}/libextractor.info.*

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Libextractor library used to extract meta-data from files 
Group:		System/Libraries

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

%files -n %{libname}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/%{name}%{major}

#----------------------------------------------------------------------------

%package -n	%{libcommon}
Summary:	Libextractor library for common functions
Group:		System/Libraries

%description -n	%{libcommon}
Common function library of libextractor.

%files -n %{libcommon}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/%{name}_common.so.%{common_major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Libextractor library headers and development libraries
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libcommon} = %{version}-%{release}
Obsoletes:	%{_lib}extractor-static-devel < 1.1

%description -n	%{devname}
Development files and headers for libextractor.

%files -n %{devname}
%doc ChangeLog NEWS COPYING README AUTHORS
%{_libdir}/%{name}.so
%{_libdir}/%{name}_common.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--disable-static \
	--disable-rpath \
	--enable-exiv2 \
	--disable-ffmpeg \
	--with-plugindirname=%{name}%{major}

%make_build

%install
%make_install

%find_lang %{name}
