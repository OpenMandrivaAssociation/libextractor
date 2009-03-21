%define realname extractor

%define major 1
%define libname %mklibname %{realname} %{major}
%define libnamedev %mklibname %{realname} -d

Summary:	Libextractor library used to extract meta-data from files
Name:		libextractor
Version:	0.5.22
Release:	%mkrel 2
License:	BSD
Group:		System/Libraries
URL:		http://www.gnunet.org/libextractor/
Source:		http://www.gnunet.org/libextractor/download/%{name}-%{version}.tar.gz
Conflicts:	%{mklibname extractor 1} < 0.5.19a-2
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	libltdl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libmpeg2dec-devel
BuildRequires:	libflac-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgsf-devel
# Does not support librpm4.6
#BuildRequires:	librpm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%package -n %{libname}
Summary:	Libextractor library used to extract meta-data from files 
Group:		Development/Other
Conflicts:	%{mklibname -d extractor 1} < 0.5.19a-2
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
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

%package -n %{libnamedev}
Summary:	Libextractor library headers and development libraries
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	libextractor-devel = %{version}-%{release}
Obsoletes:	%mklibname -d extractor 1

%description -n %{libnamedev}
Development files and headers for libextractor.

%prep
%setup -q 

%build
export CFLAGS="${CFLAGS} -lgthread-2.0"

%configure2_5x \
	--disable-rpath \
	--enable-exiv2 \
	--disable-ffmpeg

%make -j1

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%post
%_install_info extractor

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%preun
%_remove_install_info extractor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_infodir}/extractor.info.*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/%{name}

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
