%{?scl:%scl_package jnr-constants}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}jnr-constants
Version:        0.8.8
Release:        3.1%{?dist}
Summary:        Java Native Runtime constants 
License:        ASL 2.0
URL:            http://github.com/jnr/%{pkg_name}/
Source0:        https://github.com/jnr/%{pkg_name}/archive/%{version}.tar.gz
Source1:        MANIFEST.MF
Patch0:         add-manifest.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.sonatype.oss:oss-parent:pom:)

%description
Provides java values for common platform C constants (e.g. errno).

%package javadoc
Summary:        Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{pkg_name}-%{version}
cp %{SOURCE1} .
%patch0
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%mvn_file : %{pkg_name}/%{pkg_name} %{pkg_name} constantine
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_datadir}/java/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Aug 20 2015 Mat Booth <mat.booth@redhat.com> - 0.8.8-3.1
- Fix unowned directories

* Thu Jun 25 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8.8-3
- Get junit from scl_prefix_java_common.

* Thu Jun 25 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8.8-2
- SCL-ize the package

* Thu Jun 25 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8.8-1
- Initial import from rawhide.
