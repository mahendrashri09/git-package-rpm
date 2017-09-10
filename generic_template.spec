Name:           
Version:        1.1
Release:        1%{?dist}
Summary:        Build an RPM from the git repository

Group:          Development/Libraries
License:        Proprietary
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:          noarch

%description
Packaging the git repo into an rpm

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p  $RPM_BUILD_ROOT/usr/local/
cp -a * $RPM_BUILD_ROOT/usr/local/
install -m 0755 -d $RPM_BUILD_ROOT


%clean
rm -rf %{buildroot}


%files
/usr/local/
%defattr(-,root,root,-)
%doc

