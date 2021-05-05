# NOTE: when updating spec, adjust particular proto versions!

# whole package version
%define	ver		2021.4
# package release
%define	rel		1
# subpackage versions (see .pc files) # last standalone spec EVR as comment
%define	applewm_ver	1.4.2		# 1.2.0-1
%define	bigreqs_ver	1.1.2		# 1.1.2-2
%define	composite_ver	0.4.2		# 0.4.2-2
%define	damage_ver	1.2.1		# 1.2.1-2
%define	dmx_ver		2.3.1		# 2.3.1-2
%define	dpms_ver	1.2		# (1.1, but part of xext 1:7.3.0-2)
%define	dri2_ver	2.8		# 2.8-2
%define	dri3_ver	1.2		# 1.0-2
%define	evie_ver	1.1.1		# evieext-1.1.1-2
%define	fixes_ver	5.0		# 5.0-2
%define	fontcache_ver	0.1.3		# 0.1.3-2
%define	fonts_ver	2.1.3		# 2.1.3-2
%define	gl_ver		1.4.17		# 1.4.17-2
%define	input_ver	2.3.2		# 2.3.2-1
%define	kb_ver		1.0.7		# 1.0.7-1
%define	lg3d_ver	5.0		# (none)
%define	present_ver	1.2		# 1.1-1
%define	print_ver	1.0.5		# 1.0.5-2
%define	randr_ver	1.6.0		# 1.5.0-1
%define	record_ver	1.14.2		# 1.14.2-2
%define	render_ver	0.11.1		# 0.11.1-2
%define	resource_ver	1.2.0		# 1.2.0-2
%define	scrnsaver_ver	1.2.3		# 1.2.2-2
%define	trap_ver	3.4.3		# 3.4.3-3
%define	video_ver	2.3.3		# 2.3.3-1
%define	windowswm_ver	1.0.4		# 1.0.4-2
%define	xcalibrate_ver	0.1.0		# (none)
%define	xcmisc_ver	1.2.2		# 1.2.2-2
%define	xext_ver	7.3.0		# 1:7.3.0-2
%define	xf86bigfont_ver	1.2.0		# 1.2.0-2
%define	xf86dga_ver	2.1		# 2.1-3
%define	xf86dri_ver	2.1.1		# 2.1.1-2
%define	xf86misc_ver	0.9.3		# 0.9.3-2
%define	xf86rush_ver	1.1.2		# 1.1.2-3
%define	xf86vidmode_ver	2.3.1		# 2.3.1-2
%define	xinerama_ver	1.2.1		# 1.2.1-2
%define	x_ver		7.0.33		# 7.0.31-1
%define	xproxymng_ver	1.0.3		# xproxymanagementprotocol-1.0.3-3

# Conditional build:
%bcond_without	foreign		# foreign OS protocols (applewm, windowswm)
%bcond_without	legacy		# legacy protocols (XCalibrate, evie, fontcache, lg3d, print, trap, xf86misc, xf86rush, xproxymng)

Summary:	Header files of X Window System Unified Protocol
Summary(pl.UTF-8):	Pliki nagłówkowe zunifikowanego protokołu systemu X Window
Name:		xorg-proto-xorgproto
Version:	%{ver}
Release:	%{ver}.%{rel}
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/xorgproto-%{ver}.tar.bz2
# Source0-md5:	fb7593911f90727adc03d731e286c685
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libxslt-progs
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the headers and specification documents defining
the core protocol and (many) extensions for the X Window System.

%description -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i dokumenty ze specyfikacją
definiującą podstawowy protokół oraz wiele rozszerzeń systemu X
Window.

%package -n xorg-proto-applewmproto-devel
Summary:	AppleWM extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia AppleWM
Version:	%{applewm_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-applewmproto-devel
AppleWM extension headers.

%description -n xorg-proto-applewmproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia AppleWM.

%package -n xorg-proto-bigreqsproto-devel
Summary:	Big Requests extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Big Requests
Version:	%{bigreqs_ver}
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-bigreqsproto-devel
Big Requests extension headers.

%description -n xorg-proto-bigreqsproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Big Requests.

%package -n xorg-proto-compositeproto-devel
Summary:	Composite extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Composite
Version:	%{composite_ver}
Requires:	xorg-proto-fixesproto-devel = %{fixes_ver}-%{release}
Obsoletes:	compositeext

%description -n xorg-proto-compositeproto-devel
Composite extension headers.

%description -n xorg-proto-compositeproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Composite.

%package -n xorg-proto-damageproto-devel
Summary:	Damage extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Damage
Version:	%{damage_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-fixesproto-devel = %{fixes_ver}-%{release}
Obsoletes:	damageext

%description -n xorg-proto-damageproto-devel
Damage extension headers.

%description -n xorg-proto-damageproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Damage.

%package -n xorg-proto-dmxproto-devel
Summary:	DMX extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia DMX
Version:	%{dmx_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-dmxproto-devel
DMX (Distributed Multihead X) extension defines a protocol for clients
to access a front-end proxy X server that controls multiple back-end X
servers making up a large display.

%description -n xorg-proto-dmxproto-devel -l pl.UTF-8
Rozszerzenie DMX (Distributed Multihead X) definiuje protokół
pozwalający klientom na dostęp do frontendowego serwera proxy X
sterującego wieloma backendowymi serwerami X tworzącymi duży ekran.

%package -n xorg-proto-dri2proto-devel
Summary:	DRI2 extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia DRI2
Version:	%{dri2_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-dri2proto-devel
DRI2 (Direct Rendering Infrastructure 2) extension headers.

%description -n xorg-proto-dri2proto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia DRI2 (Direct Rendering Infrastructure
2).

%package -n xorg-proto-dri3proto-devel
Summary:	DRI3 extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia DRI3
Version:	%{dri3_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-dri3proto-devel
DRI3 (Direct Rendering Infrastructure 3) extension headers.

%description -n xorg-proto-dri3proto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia DRI3 (Direct Rendering Infrastructure
3).

%package -n xorg-proto-evieproto-devel
Summary:	EvIE extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia EvIE
Version:	%{evie_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	xorg-proto-evieext-devel < 1.1.1-3

%description -n xorg-proto-evieproto-devel
Extended Visual Information Extension (XEVIE) defines a protocol for a
client to determine information about core X visuals beyond what the
core protocol provides.

%description -n xorg-proto-evieproto-devel -l pl.UTF-8
Rozszerzenie XEVIE (Extended Visual Information Extension) definiuje
protokół pozwalający klientowi poznać informacje o poszczególnych
ekranach X ukrytych za protokołem.

%package -n xorg-proto-fixesproto-devel
Summary:	X Fixes extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia X Fixes
Version:	%{fixes_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xextproto-devel = 1:%{xext_ver}-%{release}
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	fixesext

%description -n xorg-proto-fixesproto-devel
Header files and documentation for the XFIXES extension.

%description -n xorg-proto-fixesproto-devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do rozszerzenia XFIXES.

%package -n xorg-proto-fontcacheproto-devel
Summary:	Fontcache extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Fontcache
Version:	%{fontcache_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-fontcacheproto-devel
Fontcache extension headers.

%description -n xorg-proto-fontcacheproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Fontcache.

%package -n xorg-proto-fontsproto-devel
Summary:	Fonts extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Fonts
Version:	%{fonts_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-fontsproto-devel
Fonts extension headers.

%description -n xorg-proto-fontsproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Fonts.

%package -n xorg-proto-glproto-devel
Summary:	GLX extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia GLX
Version:	%{gl_ver}
Group:		X11/Development/Libraries
# <GL/glxint.h> needs <X11/X*.h> and <GL/gl.h>
Requires:	OpenGL-devel
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-glproto-devel
GLX (OpenGL) extension headers.

%description -n xorg-proto-glproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia GLX (OpenGL).

%package -n xorg-proto-inputproto-devel
Summary:	Input extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Input
Version:	%{input_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-inputproto-devel
Input extension headers.

%description -n xorg-proto-inputproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Input.

%package -n xorg-proto-kbproto-devel
Summary:	KB extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia KB
Version:	%{kb_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-kbproto-devel
KB (XKEYBOARD) extension headers.

%description -n xorg-proto-kbproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia KB (XKEYBOARD).

%package -n xorg-proto-lg3dproto-devel
Summary:	LGE extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia LGE
Version:	%{lg3d_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-lg3dproto-devel
LGE extension headers.

%description -n xorg-proto-lg3dproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia LGE.

%package -n xorg-proto-presentproto-devel
Summary:	Present extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Present
Version:	%{present_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-presentproto-devel
Present extension headers.

%description -n xorg-proto-presentproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Present.

%package -n xorg-proto-printproto-devel
Summary:	Xprint extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xprint
Version:	%{print_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-printproto-devel
Xprint extension to the X11 protocol is (now deprecated) portable,
network-transparent printing system.

%description -n xorg-proto-printproto-devel -l pl.UTF-8
Rozszerzenie Xprint protokołu X11 jest (teraz już przestarzałym)
systemem drukowania przezroczystym względem sieci.

%package -n xorg-proto-randrproto-devel
Summary:	RandR extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozrzerzenia RandR
Version:	%{randr_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	randrext

%description -n xorg-proto-randrproto-devel
RandR extension headers.

The X Resize, Rotate and Reflect Extension, called RandR for short,
brings the ability to resize, rotate and reflect the root window of a
screen. It is based on the X Resize and Rotate Extension as specified
in the Proceedings of the 2001 Usenix Technical Conference [RANDR].

%description -n xorg-proto-randrproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia RandR.

Rozszerzenie X Resize, Rotate and Reflect (w skrócie RandR) daje
możliwość zmiany rozmiaru, obrotu i odbicia głównego okna ekranu. Jest
oparte na rozszerzeniu X Resize and Rotate opisanym w protokołach
konferencji 2001 Usenix Technical Conference [RANDR].

%package -n xorg-proto-recordproto-devel
Summary:	Record extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Record
Version:	%{record_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	recordext

%description -n xorg-proto-recordproto-devel
Record extension headers.

%description -n xorg-proto-recordproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Record.

%package -n xorg-proto-renderproto-devel
Summary:	RENDER extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia RENDER
Version:	%{render_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	render
Obsoletes:	renderext

%description -n xorg-proto-renderproto-devel
X Rendering (RENDER) extension headers.

%description -n xorg-proto-renderproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia X Rendering (RENDER).

%package -n xorg-proto-resourceproto-devel
Summary:	Resource extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Resource
Version:	%{resource_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	resourceext

%description -n xorg-proto-resourceproto-devel
Resource extension headers.

%description -n xorg-proto-resourceproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Resource.

%package -n xorg-proto-scrnsaverproto-devel
Summary:	ScrnSaver extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia ScrnSaver
Version:	%{scrnsaver_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-scrnsaverproto-devel
ScrnSaver extension headers.

%description -n xorg-proto-scrnsaverproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia ScrnSaver.

%package -n xorg-proto-trapproto-devel
Summary:	Trap extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Trap
Version:	%{trap_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Requires:	xorg-lib-libXt-devel

%description -n xorg-proto-trapproto-devel
Trap extension headers.

%description -n xorg-proto-trapproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Trap.

%package -n xorg-proto-videoproto-devel
Summary:	Video extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Video
Version:	%{video_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-videoproto-devel
Video (XVideo) extension headers.

%description -n xorg-proto-videoproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Video (XVideo).

%package -n xorg-proto-windowswmproto-devel
Summary:	WindowsWM extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia WindowsWM
Version:	%{windowswm_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-windowswmproto-devel
WindowsWM extension headers provide the definition of the WindowsWM
extension to the X11 protocol, used for coordination between an X11
server and the Microsoft Windows native window manager.

%description -n xorg-proto-windowswmproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia WindowsWM udostępniają definicję
rozszerzenia WindowsWM do protokołu X11, służącego do współpracy
między serwerem X11 a natywnym zarządcą okien Microsoft Windows.

%package -n xorg-proto-xcalibrateproto-devel
Summary:	XCalibrate extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XCalibrate
Version:	%{xcalibrate_ver}
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-xcalibrateproto-devel
XCalibrate extension headers.

%description -n xorg-proto-xcalibrateproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia XCalibrate.

%package -n xorg-proto-xcmiscproto-devel
Summary:	XCMisc extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XCMisc
Version:	%{xcmisc_ver}
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-xcmiscproto-devel
XCMisc extension headers.

%description -n xorg-proto-xcmiscproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia XCMisc.

%package -n xorg-proto-xextproto-devel
Summary:	XExt extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzeń XExt
Version:	%{xext_ver}
Epoch:		1
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Provides:	xorg-proto-dpmsproto-devel = %{dpms_ver}-%{release}
Suggests:	xorg-lib-libXext-devel >= 1:1.1
Obsoletes:	xextensions

%description -n xorg-proto-xextproto-devel
Header files for X protocol extensions, covering:
- DOUBLE-BUFFER
- DPMS
- Extended-Visual-Information
- Generic Event Extension
- LBX
- MIT-SHM
- MIT-SUNDRY-NONSTANDARD
- Multi-Buffering
- SECURITY
- SHAPE
- SYNC
- TOG-CUP
- XC-APPGROUP
- XTEST

%description -n xorg-proto-xextproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzeń protokołu X, obejmujące:
- DOUBLE-BUFFER
- DPMS
- Extended-Visual-Information
- Generic Event Extension
- LBX
- MIT-SHM
- MIT-SUNDRY-NONSTANDARD
- Multi-Buffering
- SECURITY
- SHAPE
- SYNC
- TOG-CUP
- XC-APPGROUP
- XTEST

%package -n xorg-proto-xf86bigfontproto-devel
Summary:	XF86BigFont extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86BigFont
Version:	%{xf86bigfont_ver}
# reset epoch after xext
Epoch:		0
Group:		X11/Development/Libraries
Requires:	xorg-proto-fontsproto-devel = %{fonts_ver}-%{release}

%description -n xorg-proto-xf86bigfontproto-devel
XF86BigFont extension headers.

%description -n xorg-proto-xf86bigfontproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia XF86BigFont.

%package -n xorg-proto-xf86dgaproto-devel
Summary:	XF86DGA extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86DGA
Version:	%{xf86dga_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-xf86dgaproto-devel
XF86DGA extension headers.

%description -n xorg-proto-xf86dgaproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia XF86DGA.

%package -n xorg-proto-xf86driproto-devel
Summary:	XF86DRI extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86DRI
Version:	%{xf86dri_ver}
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-xf86driproto-devel
XF86DRI (XFree86 Direct Rendering Infrastructure) extension defines a
protocol to allow user applications to access the video hardware
without requiring data to be passed through the X server.

%description -n xorg-proto-xf86driproto-devel -l pl.UTF-8
Rozszerzenie XF86DRI (XFree86 Direct Rendering Infrastructure)
definiuje protokół pozwalający aplikacjom użytkownika na dostęp do
sprzętu wyświetlającego obraz bez potrzeby przekazywania danych
poprzez serwer X.

%package -n xorg-proto-xf86miscproto-devel
Summary:	XFree86-Misc extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XFree86-Misc
Version:	%{xf86misc_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-xf86miscproto-devel
This package includes the protocol definitions of the "XFree86-Misc"
extension to the X11 protocol. The "XFree86-Misc" extension is
supported by the XFree86 X server and versions of the Xorg X server
prior to Xorg 1.6.

%description -n xorg-proto-xf86miscproto-devel -l pl.UTF-8
Ten pakiet zawiera definicje protokołu rozszerzenia "XFree86-Misc"
do protokołu X11. Rozszerzenie to jest obsługiwane przez serwer X
XFree86 oraz serwer X Xorg w wersji wcześniejszej niż Xorg 1.6.

%package -n xorg-proto-xf86rushproto-devel
Summary:	XF86Rush extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86Rush
Version:	%{xf86rush_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-videoproto-devel = %{video_ver}-%{release}

%description -n xorg-proto-xf86rushproto-devel
XF86Rush extension headers.

%description -n xorg-proto-xf86rushproto-devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia XF86Rush.

%package -n xorg-proto-xf86vidmodeproto-devel
Summary:	XF86VidMode extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia XF86VidMode
Version:	%{xf86vidmode_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}

%description -n xorg-proto-xf86vidmodeproto-devel
XF86VidMode (XFree86 Video Mode) extension defines a protocol for
dynamically configuring modelines and gamma.

%description -n xorg-proto-xf86vidmodeproto-devel -l pl.UTF-8
Rozszerzenie XF86VidMode (XFree86 Video Mode) definiuje protokół do
dynamicznej konfiguracji linii opisujących tryb (modeline) oraz
korekcji gamma.

%package -n xorg-proto-xineramaproto-devel
Summary:	Xinerama extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xinerama
Version:	%{xinerama_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	panoramixext
Obsoletes:	xorg-proto-panoramixproto-devel

%description -n xorg-proto-xineramaproto-devel
Xinerama is an X extension that allows multiple physical screens
controlled by a single X server to appear as a single screen.

%description -n xorg-proto-xineramaproto-devel -l pl.UTF-8
Xinerama to rozszerzenie X pozwalające na sterowanie wieloma
fizycznymi ekranami przez pojedynczy serwer X tak, że stają się
jednym ekranem.

%package -n xorg-proto-xproto-devel
Summary:	X protocol and ancillary headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu X i pomocnicze
Version:	%{x_ver}
Group:		X11/Development/Libraries
Requires:	filesystem >= 3.0-32
Obsoletes:	xproto

%description -n xorg-proto-xproto-devel
X protocol and ancillary headers.

%description -n xorg-proto-xproto-devel -l pl.UTF-8
Pliki nagłówkowe protokołu X i pomocnicze.

%package -n xorg-proto-xproxymngproto-devel
Summary:	X Proxy Management Protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu X Proxy Management
Version:	%{xproxymng_ver}
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel = %{x_ver}-%{release}
Obsoletes:	xorg-proto-xproxymanagementprotocol-devel < 1.0.3-4

%description -n xorg-proto-xproxymngproto-devel
X Proxy Management Protocol headers.

The Proxy Management Protocol is an ICE based protocol that provides a
way for application servers to easily locate proxy services available
to them.

%description -n xorg-proto-xproxymngproto-devel -l pl.UTF-8
Pliki nagłówkowe protokołu X Proxy Management.

Proxy Management Protocol to oparty na ICE protokół pozwalający
serwerom aplikacji lokalizować w prosty sposób dostępne dla nich
usługi proxy.

%prep
%setup -q -n xorgproto-%{ver}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--host=%{_host} \
	--build=%{_host} \
%endif
	%{?with_legacy:--enable-legacy} \
	--without-fop

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with legacy}
# moved to libX11 >= 1.6.9
%{__rm} $RPM_BUILD_ROOT%{_includedir}/X11/extensions/XKBgeom.h
# moved to libXvMC >= 1.0.12
%{__rm} $RPM_BUILD_ROOT%{_includedir}/X11/extensions/vldXvMC.h
%endif

%if %{without foreign}
%{__rm} $RPM_BUILD_ROOT%{_includedir}/X11/extensions/{applewm,windowswm}*.h
%{__rm} $RPM_BUILD_ROOT%{_npkgconfigdir}/{applewmproto,windowswmproto}.pc
%endif

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/{bigreqsproto,fontsproto,kbproto,recordproto,scrnsaverproto,xcmiscproto,xextproto,xorgproto,xproto}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with foreign}
%files -n xorg-proto-applewmproto-devel
%defattr(644,root,root,755)
%doc COPYING-applewmproto
%{_includedir}/X11/extensions/applewm*.h
%{_npkgconfigdir}/applewmproto.pc
%endif

%files -n xorg-proto-bigreqsproto-devel
%defattr(644,root,root,755)
%doc COPYING-bigreqsproto specs/bigreqsproto/bigreq.html
%{_includedir}/X11/extensions/bigreqs*.h
%{_npkgconfigdir}/bigreqsproto.pc

%files -n xorg-proto-compositeproto-devel
%defattr(644,root,root,755)
%doc COPYING-compositeproto compositeproto.txt
%{_includedir}/X11/extensions/composite*.h
%{_npkgconfigdir}/compositeproto.pc

%files -n xorg-proto-damageproto-devel
%defattr(644,root,root,755)
%doc COPYING-damageproto damageproto.txt
%{_includedir}/X11/extensions/damage*.h
%{_npkgconfigdir}/damageproto.pc

%files -n xorg-proto-dmxproto-devel
%defattr(644,root,root,755)
%doc COPYING-dmxproto
%{_includedir}/X11/extensions/dmx*.h
%{_npkgconfigdir}/dmxproto.pc

%files -n xorg-proto-dri2proto-devel
%defattr(644,root,root,755)
%doc COPYING-dri2proto dri2proto.txt
%{_includedir}/X11/extensions/dri2*.h
%{_npkgconfigdir}/dri2proto.pc

%files -n xorg-proto-dri3proto-devel
%defattr(644,root,root,755)
%doc COPYING-dri3proto dri3proto.txt
%{_includedir}/X11/extensions/dri3proto.h
%{_npkgconfigdir}/dri3proto.pc

%if %{with legacy}
%files -n xorg-proto-evieproto-devel
%defattr(644,root,root,755)
%doc COPYING-evieproto
%{_includedir}/X11/extensions/Xeviestr.h
%{_includedir}/X11/extensions/evieproto.h
%{_npkgconfigdir}/evieproto.pc
%endif

%files -n xorg-proto-fixesproto-devel
%defattr(644,root,root,755)
%doc COPYING-fixesproto fixesproto.txt
%{_includedir}/X11/extensions/xfixes*.h
%{_npkgconfigdir}/fixesproto.pc

%if %{with legacy}
%files -n xorg-proto-fontcacheproto-devel
%defattr(644,root,root,755)
%doc COPYING-fontcacheproto
%{_includedir}/X11/extensions/fontcach*.h
%{_npkgconfigdir}/fontcacheproto.pc
%endif

%files -n xorg-proto-fontsproto-devel
%defattr(644,root,root,755)
%doc COPYING-fontsproto specs/fontsproto/fsproto.html
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/FS.h
%{_includedir}/X11/fonts/FSproto.h
%{_includedir}/X11/fonts/font.h
%{_includedir}/X11/fonts/fontproto.h
%{_includedir}/X11/fonts/fontstruct.h
%{_includedir}/X11/fonts/fsmasks.h
%{_npkgconfigdir}/fontsproto.pc

%files -n xorg-proto-glproto-devel
%defattr(644,root,root,755)
%doc COPYING-glproto
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/glxtokens.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%{_npkgconfigdir}/glproto.pc

%files -n xorg-proto-inputproto-devel
%defattr(644,root,root,755)
%doc COPYING-inputproto
# specs/{XIproto.txt,XI2proto.txt}
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XIproto.h
%{_includedir}/X11/extensions/XI2.h
%{_includedir}/X11/extensions/XI2proto.h
%{_npkgconfigdir}/inputproto.pc

%files -n xorg-proto-kbproto-devel
%defattr(644,root,root,755)
%doc COPYING-kbproto specs/kbproto/{XKBproto-*.svg,xkbproto.html}
%{_includedir}/X11/extensions/XKB.h
%{_includedir}/X11/extensions/XKBproto.h
%{_includedir}/X11/extensions/XKBsrv.h
%{_includedir}/X11/extensions/XKBstr.h
%{_npkgconfigdir}/kbproto.pc

%if %{with legacy}
%files -n xorg-proto-lg3dproto-devel
%defattr(644,root,root,755)
%doc COPYING-lg3dproto
%{_includedir}/X11/extensions/lgewire.h
%{_npkgconfigdir}/lg3dproto.pc
%endif

%files -n xorg-proto-presentproto-devel
%defattr(644,root,root,755)
%doc COPYING-presentproto presentproto.txt
%{_includedir}/X11/extensions/present*.h
%{_npkgconfigdir}/presentproto.pc

%if %{with legacy}
%files -n xorg-proto-printproto-devel
%defattr(644,root,root,755)
%doc COPYING-printproto specs/printproto/xp_proto.ps
%{_includedir}/X11/extensions/Print*.h
%{_npkgconfigdir}/printproto.pc
%{_mandir}/man7/Xprint.7*
%endif

%files -n xorg-proto-randrproto-devel
%defattr(644,root,root,755)
%doc COPYING-randrproto randrproto.txt
%{_includedir}/X11/extensions/randr*.h
%{_npkgconfigdir}/randrproto.pc

%files -n xorg-proto-recordproto-devel
%defattr(644,root,root,755)
%doc COPYING-recordproto specs/recordproto/record.html
%{_includedir}/X11/extensions/record*.h
%{_npkgconfigdir}/recordproto.pc

%files -n xorg-proto-renderproto-devel
%defattr(644,root,root,755)
%doc COPYING-renderproto renderproto.txt
%{_includedir}/X11/extensions/render*.h
%{_npkgconfigdir}/renderproto.pc

%files -n xorg-proto-resourceproto-devel
%defattr(644,root,root,755)
%doc COPYING-resourceproto resproto.txt
%{_includedir}/X11/extensions/XResproto.h
%{_npkgconfigdir}/resourceproto.pc

%files -n xorg-proto-scrnsaverproto-devel
%defattr(644,root,root,755)
%doc COPYING-scrnsaverproto specs/scrnsaverproto/saver.html
%{_includedir}/X11/extensions/saver*.h
%{_npkgconfigdir}/scrnsaverproto.pc

%if %{with legacy}
%files -n xorg-proto-trapproto-devel
%defattr(644,root,root,755)
%doc COPYING-trapproto
%{_includedir}/X11/extensions/xtrap*.h
%{_npkgconfigdir}/trapproto.pc
%endif

%files -n xorg-proto-videoproto-devel
%defattr(644,root,root,755)
%doc COPYING-videoproto xv-protocol-v2.txt
%{_includedir}/X11/extensions/Xv.h
%{_includedir}/X11/extensions/Xvproto.h
%{_includedir}/X11/extensions/XvMC.h
%{_includedir}/X11/extensions/XvMCproto.h
%{_npkgconfigdir}/videoproto.pc

%if %{with foreign}
%files -n xorg-proto-windowswmproto-devel
%defattr(644,root,root,755)
%doc COPYING-windowswmproto
%{_includedir}/X11/extensions/windowswm*.h
%{_npkgconfigdir}/windowswmproto.pc
%endif

%if %{with legacy}
%files -n xorg-proto-xcalibrateproto-devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/xcalibrate*.h
%{_npkgconfigdir}/xcalibrateproto.pc
%endif

%files -n xorg-proto-xcmiscproto-devel
%defattr(644,root,root,755)
%doc COPYING-xcmiscproto specs/xcmiscproto/xc-misc.html
%{_includedir}/X11/extensions/xcmisc*.h
%{_npkgconfigdir}/xcmiscproto.pc

%files -n xorg-proto-xextproto-devel
%defattr(644,root,root,755)
%doc COPYING-xextproto specs/xextproto/{appgrp,dbe,dpms,evi,geproto,lbx,multibuf,security,shape,shm,sync,tog-cup,xtest}.html
%{_includedir}/X11/extensions/EVI*.h
%{_includedir}/X11/extensions/ag*.h
%{_includedir}/X11/extensions/cup*.h
%{_includedir}/X11/extensions/dbe*.h
%{_includedir}/X11/extensions/dpms*.h
%{_includedir}/X11/extensions/ge*.h
%{_includedir}/X11/extensions/lbx*.h
%{_includedir}/X11/extensions/mitmisc*.h
%{_includedir}/X11/extensions/multibuf*.h
%{_includedir}/X11/extensions/secur*.h
%{_includedir}/X11/extensions/shape*.h
%{_includedir}/X11/extensions/shm*.h
%{_includedir}/X11/extensions/sync*.h
%{_includedir}/X11/extensions/xtest*.h
%{_npkgconfigdir}/dpmsproto.pc
%{_npkgconfigdir}/xextproto.pc

%files -n xorg-proto-xf86bigfontproto-devel
%defattr(644,root,root,755)
%doc COPYING-xf86bigfontproto
%{_includedir}/X11/extensions/xf86bigf*.h
%{_npkgconfigdir}/xf86bigfontproto.pc

%files -n xorg-proto-xf86dgaproto-devel
%defattr(644,root,root,755)
%doc COPYING-xf86dgaproto
%{_includedir}/X11/extensions/xf86dga*.h
%{_npkgconfigdir}/xf86dgaproto.pc

%files -n xorg-proto-xf86driproto-devel
%defattr(644,root,root,755)
%doc COPYING-xf86driproto
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/xf86dri*.h
%{_npkgconfigdir}/xf86driproto.pc

%if %{with legacy}
%files -n xorg-proto-xf86miscproto-devel
%defattr(644,root,root,755)
%doc COPYING-xf86miscproto
%{_includedir}/X11/extensions/xf86mscstr.h
%{_includedir}/X11/extensions/xf86misc.h
%{_npkgconfigdir}/xf86miscproto.pc

%files -n xorg-proto-xf86rushproto-devel
%defattr(644,root,root,755)
%doc COPYING-xf86rushproto
%{_includedir}/X11/extensions/xf86rush*.h
%{_npkgconfigdir}/xf86rushproto.pc
%endif

%files -n xorg-proto-xf86vidmodeproto-devel
%defattr(644,root,root,755)
%doc COPYING-xf86vidmodeproto
%{_includedir}/X11/extensions/xf86vm*.h
%{_npkgconfigdir}/xf86vidmodeproto.pc

%files -n xorg-proto-xineramaproto-devel
%defattr(644,root,root,755)
%doc COPYING-xineramaproto
%{_includedir}/X11/extensions/panoramiXproto.h
%{_npkgconfigdir}/xineramaproto.pc

%files -n xorg-proto-xproto-devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING-x11proto README.md specs/SIAddresses/{IPv6,hostname,localuser}.md specs/xproto/x11protocol.html
%{_includedir}/X11/DECkeysym.h
%{_includedir}/X11/HPkeysym.h
%{_includedir}/X11/Sunkeysym.h
%{_includedir}/X11/X.h
%{_includedir}/X11/XF86keysym.h
%{_includedir}/X11/XWDFile.h
%{_includedir}/X11/Xalloca.h
%{_includedir}/X11/Xarch.h
%{_includedir}/X11/Xatom.h
%{_includedir}/X11/Xdefs.h
%{_includedir}/X11/Xfuncproto.h
%{_includedir}/X11/Xfuncs.h
%{_includedir}/X11/Xmd.h
%{_includedir}/X11/Xos.h
%{_includedir}/X11/Xos_r.h
%{_includedir}/X11/Xosdefs.h
%{_includedir}/X11/Xpoll.h
%{_includedir}/X11/Xproto.h
%{_includedir}/X11/Xprotostr.h
%{_includedir}/X11/Xthreads.h
%{_includedir}/X11/Xw32defs.h
%{_includedir}/X11/Xwindows.h
%{_includedir}/X11/Xwinsock.h
%{_includedir}/X11/ap_keysym.h
%{_includedir}/X11/keysym.h
%{_includedir}/X11/keysymdef.h
%dir %{_includedir}/X11/extensions
%{_npkgconfigdir}/xproto.pc

%if %{with legacy}
%files -n xorg-proto-xproxymngproto-devel
%defattr(644,root,root,755)
%doc COPYING-pmproto PM_spec
%dir %{_includedir}/X11/PM
%{_includedir}/X11/PM/PM*.h
%{_npkgconfigdir}/xproxymngproto.pc
%endif
