%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Full featured email transfer class for PHP
Summary(pl.UTF-8):	W pełni funkcjonalna klasa PHP do przesyłania e-maili
Name:		php-phpmailer
Version:	5.2.0
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://phpmailer.apache-extras.org.codespot.com/files/PHPMailer_%{version}.tgz
# Source0-md5:	aed567b80e6a3b3175d4ce27f3a9a243
Patch0:		paths.patch
Patch1:		phpmailer-update-et.patch
URL:		http://code.google.com/a/apache-extras.org/p/phpmailer/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-pcre
Suggests:	php-mbstring
Suggests:	php-openssl
Obsoletes:	phpmailer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/phpmailer

# exclude optional php dependencies
%define		_noautophp	php-openssl php-mbstring php-filter

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

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

%prep
%setup -q -n PHPMailer_%{version}
%patch0 -p1
%patch1 -p1

find '(' -name '*.php' -o -name '*.html' -o -name '*.txt' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'
%{__sed} -i -e 's,\r$,,' README LICENSE

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/language

cp -a class.phpmailer.php $RPM_BUILD_ROOT%{php_data_dir}
# plugins: for smtp and pop before smtp auth
cp -a class.{smtp,pop3}.php  $RPM_BUILD_ROOT%{_appdir}
# language: translations of error messages
cp -a language/*.php $RPM_BUILD_ROOT%{_appdir}/language

# examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt README docs/*
%{php_data_dir}/class.phpmailer.php

%dir %{_appdir}
%{_appdir}/class.pop3.php
%{_appdir}/class.smtp.php
%dir %{_appdir}/language
%lang(ar) %{_appdir}/language/phpmailer.lang-ar.php
%lang(ca) %{_appdir}/language/phpmailer.lang-ca.php
%lang(ch) %{_appdir}/language/phpmailer.lang-ch.php
%lang(cs) %{_appdir}/language/phpmailer.lang-cz.php
%lang(da) %{_appdir}/language/phpmailer.lang-dk.php
%lang(de) %{_appdir}/language/phpmailer.lang-de.php
%lang(es) %{_appdir}/language/phpmailer.lang-es.php
%lang(et) %{_appdir}/language/phpmailer.lang-et.php
%lang(fi) %{_appdir}/language/phpmailer.lang-fi.php
%lang(fo) %{_appdir}/language/phpmailer.lang-fo.php
%lang(fr) %{_appdir}/language/phpmailer.lang-fr.php
%lang(hu) %{_appdir}/language/phpmailer.lang-hu.php
%lang(it) %{_appdir}/language/phpmailer.lang-it.php
%lang(ja) %{_appdir}/language/phpmailer.lang-ja.php
%lang(nb) %{_appdir}/language/phpmailer.lang-no.php
%lang(nl) %{_appdir}/language/phpmailer.lang-nl.php
%lang(pl) %{_appdir}/language/phpmailer.lang-pl.php
%lang(pt_BR) %{_appdir}/language/phpmailer.lang-br.php
%lang(ro) %{_appdir}/language/phpmailer.lang-ro.php
%lang(ru) %{_appdir}/language/phpmailer.lang-ru.php
%lang(sv) %{_appdir}/language/phpmailer.lang-se.php
%lang(tr) %{_appdir}/language/phpmailer.lang-tr.php
%lang(zh) %{_appdir}/language/phpmailer.lang-zh.php
%lang(zh_CN) %{_appdir}/language/phpmailer.lang-zh_cn.php

%{_examplesdir}/%{name}-%{version}
