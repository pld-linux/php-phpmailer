Summary:	Full featured email transfer class for PHP
Summary(pl.UTF-8):	W pełni funkcjonalna klasa PHP do przesyłania e-maili
Name:		phpmailer
Version:	2.0.0
Release:	0.1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phpmailer/PHPMailer_v%{version}.tar.gz
# Source0-md5:	1fba7b3b8f67197c371da2f791d517de
URL:		http://phpmailer.codeworxtech.com/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	/usr/share/php/%{name}

%description
PHP email transport class featuring multiple file attachments, SMTP
servers, CCs, BCCs, HTML messages, and word wrap, and more. It can
send email via sendmail, PHP mail(), or with SMTP. Methods are based
on the popular AspEmail active server component.

%description -l pl.UTF-8
Klasa PHP do przesyłania e-mail obsługująca wiele załączników
plikowych, serwery SMTP, CC, BCC, wiadomości HTML, zawijanie linii
itp. Potrafi wysyłać pocztę przez sendmaila, funkcją PHP mail() albo
poprzez SMTP. Metody są oparte na popularnym komponencie AspEmail.

%package phpdoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -n PHPMailer_v%{version}

find '(' -name '*.php' -o -name '*.html' -o -name '*.txt' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/language
cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a language/*.php $RPM_BUILD_ROOT%{_appdir}/language

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a phpdoc/* $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt README LICENSE docs/*
%{_appdir}

%files phpdoc
%defattr(644,root,root,755)
%{_docdir}/%{name}
