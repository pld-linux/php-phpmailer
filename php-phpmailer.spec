# TODO:
# - better requires with proper php modules.
Summary:	Full featured email transfer class for PHP
Summary(pl.UTF-8):	W pełni funkcjonalna klasa PHP do przesyłania e-maili
Name:		phpmailer
Version:	2.2.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phpmailer/phpMailer_v%{version}.tar.gz
# Source0-md5:	9f9e9bca95fb11eee2d3e892778319d1
URL:		http://phpmailer.codeworxtech.com/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# _phpdocdir / php_docdir / phpdoc_dir ?
%define		_phpdocdir		%{_docdir}/phpdoc

%define		_appdir			%{php_data_dir}/%{name}

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
Requires:	php-dirs

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q -c

find '(' -name '*.php' -o -name '*.html' -o -name '*.txt' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir}/language,%{_phpdocdir}/%{name}}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a language/*.php $RPM_BUILD_ROOT%{_appdir}/language
cp -a phpdoc/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt README LICENSE docs/*
%dir %{_appdir}
%{_appdir}/class.phpmailer.php
%{_appdir}/class.pop3.php
%{_appdir}/class.smtp.php

%dir %{_appdir}/language
%{_appdir}/language/phpmailer.lang-en.php
%lang(br) %{_appdir}/language/phpmailer.lang-br.php
%lang(ca) %{_appdir}/language/phpmailer.lang-ca.php
%lang(cz) %{_appdir}/language/phpmailer.lang-cz.php
%lang(de) %{_appdir}/language/phpmailer.lang-de.php
%lang(dk) %{_appdir}/language/phpmailer.lang-dk.php
%lang(es) %{_appdir}/language/phpmailer.lang-es.php
%lang(et) %{_appdir}/language/phpmailer.lang-et.php
%lang(fi) %{_appdir}/language/phpmailer.lang-fi.php
%lang(fo) %{_appdir}/language/phpmailer.lang-fo.php
%lang(fr) %{_appdir}/language/phpmailer.lang-fr.php
%lang(hu) %{_appdir}/language/phpmailer.lang-hu.php
%lang(it) %{_appdir}/language/phpmailer.lang-it.php
%lang(ja) %{_appdir}/language/phpmailer.lang-ja.php
%lang(nl) %{_appdir}/language/phpmailer.lang-nl.php
%lang(no) %{_appdir}/language/phpmailer.lang-no.php
%lang(pl) %{_appdir}/language/phpmailer.lang-pl.php
%lang(ro) %{_appdir}/language/phpmailer.lang-ro.php
%lang(ru) %{_appdir}/language/phpmailer.lang-ru.php
%lang(se) %{_appdir}/language/phpmailer.lang-se.php
%lang(tr) %{_appdir}/language/phpmailer.lang-tr.php

%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}
