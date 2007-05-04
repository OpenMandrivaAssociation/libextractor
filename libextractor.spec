%define	name	libextractor
%define	version	0.5.18
%define	release	%mkrel 1

%define realname extractor

%define major 1
%define libname %mklibname %{realname} %major
%define libnamedev %mklibname %{realname} %major -d


Summary: Libextractor library used to extract meta-data from files
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: System/Libraries
URL: http://www.gnunet.org/libextractor/
Source: http://www.gnunet.org/libextractor/download/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libltdl-devel

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
Summary: Libextractor library used to extract meta-data from files 
Group: Development/Other
Provides: lib%{name} = %{version}

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
Summary: Libextractor library headers and development libraries
Group: Development/Other
Requires: %{libname} = %{version}
Provides: lib%{name}-devel = %{version}
Provides: libextractor-devel

%description -n %{libnamedev}
libextractor devel files


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 

%build
  
./configure --prefix=%_prefix --mandir=%_mandir --datadir=%_datadir --libdir=%_libdir

make

%install

%makeinstall

%find_lang %name

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname} -f %name.lang
%defattr(-,root,root)
%{_libdir}/*.so.*
%_mandir/man1/*
%_mandir/man3/*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/%name/*.so
%{_libdir}/%name/*.*a
%{_includedir}/*
%{_bindir}/*
%{_libdir}/pkgconfig/*


