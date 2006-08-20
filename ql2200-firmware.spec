#
%define		nameprog ql2200

Summary:	Firmware for the QLogic %{nameprog} HBA
Summary(pl):	Firmware dla HBA QLogic %{nameprog}
Name:		%{nameprog}-firmware
Version:	2.02.08
Release:	0.1
License:	distributable
Group:		Base/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/%{nameprog}_fw.bin
# Source0-md5:	44567f365ce6f668c69c6c40279cd878
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the QLogic %{nameprog} driver.

%description -l pl
Ten pakiet zawiera firmware dla sterownika QLogic %{nameprog}.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/*
