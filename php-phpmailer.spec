%define		pkgname	phpmailer
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Full featured email transfer class for PHP
Summary(pl.UTF-8):	W pełni funkcjonalna klasa PHP do przesyłania e-maili
Name:		php-%{pkgname}
Version:	5.2.4
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://phpmailer.apache-extras.org.codespot.com/files/PHPMailer_%{version}.tgz
# Source0-md5:	c990db0d0859599eafa4338ce90154a7
Patch0:		paths.patch
URL:		http://code.google.com/a/apache-extras.org/p/phpmailer/
#BuildRequires:	php-pear-PhpDocumentor
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Suggests:	php(mbstring)
Suggests:	php(openssl)
Obsoletes:	phpmailer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{pkgname}
%define		_phpdocdir	%{_docdir}/phpdoc

# exclude optional php dependencies
%define		_noautophp	php-openssl php-mbstring php-filter

# bad depsolver
%define		_noautoreq_pear ntlm_sasl_client.php

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp}

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
%setup -q -n PHPMailer_%{version}%{?subver:-%{subver}}
%patch0 -p1

%undos -f php,html,txt README LICENSE

mv docs/phpdoc .

%if 0
%build
phpdoc --title 'PHPMailer version %{version}' --target phpdoc --defaultpackagename PHPMailer -f 'class.*.php'
# nuke smarty cache
rm -rf phpdoc/????????????????????????????????
rm -rf phpdoc/*/????????????????????????????????

# copy images, phpdoc is likely buggy not doing itself
sdir=%{php_pear_dir}/data/PhpDocumentor/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/media/images
install -d phpdoc/media/images
cp -a $sdir/Constant.png phpdoc/media/images
cp -a $sdir/Variable.png phpdoc/media/images
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/language

cp -p class.phpmailer.php $RPM_BUILD_ROOT%{php_data_dir}
# plugins: for smtp and pop before smtp auth
cp -p class.{smtp,pop3}.php  $RPM_BUILD_ROOT%{_appdir}
# language: translations of error messages
cp -p language/*.php $RPM_BUILD_ROOT%{_appdir}/language

# extras: htmlfilter.php, ntlm_sasl_client.php
cp -a extras $RPM_BUILD_ROOT%{_appdir}

# examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# api doc
install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}
cp -a phpdoc/* $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}

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
%lang(sk) %{_appdir}/language/phpmailer.lang-sk.php
%lang(sv) %{_appdir}/language/phpmailer.lang-se.php
%lang(tr) %{_appdir}/language/phpmailer.lang-tr.php
%lang(zh) %{_appdir}/language/phpmailer.lang-zh.php
%lang(zh_CN) %{_appdir}/language/phpmailer.lang-zh_cn.php

%dir %{_appdir}/extras
%{_appdir}/extras/class.html2text.inc
%{_appdir}/extras/htmlfilter.php
%{_appdir}/extras/ntlm_sasl_client.php

%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{pkgname}
