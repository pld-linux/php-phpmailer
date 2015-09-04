%define		pkgname	phpmailer
%define		php_min_version 5.2.4
%include	/usr/lib/rpm/macros.php
Summary:	Full featured email transfer class for PHP
Summary(pl.UTF-8):	W pełni funkcjonalna klasa PHP do przesyłania e-maili
Name:		php-%{pkgname}
Version:	5.2.12
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://github.com/PHPMailer/PHPMailer/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	5c2d02e6fc4a61c9ba8b20810b564b1c
URL:		https://github.com/PHPMailer/PHPMailer
%{?with_tests:BuildRequires:    %{php_name}-cli}
BuildRequires:	php-pear-PhpDocumentor
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.663
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Suggests:	php(hash)
Suggests:	php(mbstring)
Suggests:	php(openssl)
Obsoletes:	phpmailer
# Gmail XOAUTH2 authentication
#Suggests:	php-league-oauth2-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{pkgname}
%define		_phpdocdir	%{_docdir}/phpdoc

# exclude optional php dependencies
%define		_noautophp	php-openssl php-mbstring php-filter php-hash

# bad depsolver
%define		_noautoreq_pear extras/ntlm_sasl_client.php PHPMailerAutoload.php

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
%setup -q -n PHPMailer-%{version}%{?subver:-%{subver}}

%if "%{pld_release}" == "ac"
# requires php5.3
rm test/bootstrap.php
%endif

%build
# syntax lint
for a in $(find -name '*.php' -o -name '*.inc'); do
	php -n -l $a
done

rm -rf phpdoc
phpdoc --title 'PHPMailer version %{version}' --target phpdoc --defaultpackagename PHPMailer \
	--directory . --ignore test/,examples/,extras/,test_script/,language/,phpdoc/ --sourcecode

# copy images, phpdoc is likely buggy not doing itself
sdir=%{php_pear_dir}/data/PhpDocumentor/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/media/images
install -d phpdoc/media/images
cp -p $sdir/Constant.png phpdoc/media/images
cp -p $sdir/Variable.png phpdoc/media/images

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_appdir}/language}

ln -s %{_appdir}/class.phpmailer.php $RPM_BUILD_ROOT%{php_data_dir}
ln -s %{_appdir}/PHPMailerAutoload.php $RPM_BUILD_ROOT%{php_data_dir}

cp -p class.*.php PHPMailerAutoload.php $RPM_BUILD_ROOT%{_appdir}
# language: translations of error messages
cp -p language/*.php $RPM_BUILD_ROOT%{_appdir}/language

# extras: htmlfilter.php, ntlm_sasl_client.php, EasyPeasyICS.php
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
%doc README.md changelog.md docs/*
# public interfaces
%{php_data_dir}/PHPMailerAutoload.php
%{php_data_dir}/class.phpmailer.php

%dir %{_appdir}
%{_appdir}/PHPMailerAutoload.php
%{_appdir}/class.oauth.php
%{_appdir}/class.phpmailer.php
%{_appdir}/class.phpmaileroauth.php
%{_appdir}/class.pop3.php
%{_appdir}/class.smtp.php
%dir %{_appdir}/language
%lang(am) %{_appdir}/language/phpmailer.lang-am.php
%lang(ar) %{_appdir}/language/phpmailer.lang-ar.php
%lang(az) %{_appdir}/language/phpmailer.lang-az.php
%lang(be) %{_appdir}/language/phpmailer.lang-be.php
%lang(bg) %{_appdir}/language/phpmailer.lang-bg.php
%lang(ca) %{_appdir}/language/phpmailer.lang-ca.php
%lang(ch) %{_appdir}/language/phpmailer.lang-ch.php
%lang(cs) %{_appdir}/language/phpmailer.lang-cz.php
%lang(da) %{_appdir}/language/phpmailer.lang-dk.php
%lang(de) %{_appdir}/language/phpmailer.lang-de.php
%lang(el) %{_appdir}/language/phpmailer.lang-el.php
%lang(eo) %{_appdir}/language/phpmailer.lang-eo.php
%lang(es) %{_appdir}/language/phpmailer.lang-es.php
%lang(et) %{_appdir}/language/phpmailer.lang-et.php
%lang(fa) %{_appdir}/language/phpmailer.lang-fa.php
%lang(fi) %{_appdir}/language/phpmailer.lang-fi.php
%lang(fo) %{_appdir}/language/phpmailer.lang-fo.php
%lang(fr) %{_appdir}/language/phpmailer.lang-fr.php
%lang(gl) %{_appdir}/language/phpmailer.lang-gl.php
%lang(he) %{_appdir}/language/phpmailer.lang-he.php
%lang(hr) %{_appdir}/language/phpmailer.lang-hr.php
%lang(hu) %{_appdir}/language/phpmailer.lang-hu.php
%lang(id) %{_appdir}/language/phpmailer.lang-id.php
%lang(it) %{_appdir}/language/phpmailer.lang-it.php
%lang(ja) %{_appdir}/language/phpmailer.lang-ja.php
%lang(ka) %{_appdir}/language/phpmailer.lang-ka.php
%lang(ko) %{_appdir}/language/phpmailer.lang-ko.php
%lang(lt) %{_appdir}/language/phpmailer.lang-lt.php
%lang(lv) %{_appdir}/language/phpmailer.lang-lv.php
%lang(ms) %{_appdir}/language/phpmailer.lang-ms.php
%lang(nb) %{_appdir}/language/phpmailer.lang-no.php
%lang(nl) %{_appdir}/language/phpmailer.lang-nl.php
%lang(pl) %{_appdir}/language/phpmailer.lang-pl.php
%lang(pt) %{_appdir}/language/phpmailer.lang-pt.php
%lang(pt_BR) %{_appdir}/language/phpmailer.lang-br.php
%lang(ro) %{_appdir}/language/phpmailer.lang-ro.php
%lang(ru) %{_appdir}/language/phpmailer.lang-ru.php
%lang(sk) %{_appdir}/language/phpmailer.lang-sk.php
%lang(sl) %{_appdir}/language/phpmailer.lang-sl.php
%lang(sr) %{_appdir}/language/phpmailer.lang-sr.php
%lang(sv) %{_appdir}/language/phpmailer.lang-se.php
%lang(tr) %{_appdir}/language/phpmailer.lang-tr.php
%lang(uk) %{_appdir}/language/phpmailer.lang-uk.php
%lang(vi) %{_appdir}/language/phpmailer.lang-vi.php
%lang(zh) %{_appdir}/language/phpmailer.lang-zh.php
%lang(zh_CN) %{_appdir}/language/phpmailer.lang-zh_cn.php

%dir %{_appdir}/extras
%{_appdir}/extras/README.md
%{_appdir}/extras/EasyPeasyICS.php
%{_appdir}/extras/htmlfilter.php
%{_appdir}/extras/ntlm_sasl_client.php

%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{pkgname}
