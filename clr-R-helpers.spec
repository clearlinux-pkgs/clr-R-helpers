Name:           clr-R-helpers
Version:        1
Release:        13
License:        GPL-2.0
Summary:        Helper files for R support
Url:            https://01.org/
Group:          base
Requires:	R 
Requires:	R-dev
Requires:	R-testthat
Requires: 	R-knitr
Requires:	R-crayon
Requires: 	R-R6
Requires: 	R-digest
Requires: 	R-magrittr
Requires: 	R-praise
Requires:	R-testit
Requires:	R-stringr

%description
Helper files for R support

%prep

%build
%install
mkdir -p %{buildroot}/usr/bin
ln -s R %{buildroot}/usr/bin/r


%files
/usr/bin/r