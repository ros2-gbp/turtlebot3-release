%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-turtlebot3-example
Version:        2.2.9
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS turtlebot3_example package

License:        Apache 2.0
URL:            http://turtlebot3.robotis.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-tf-transformations
Requires:       ros-jazzy-turtlebot3-msgs
Requires:       ros-jazzy-visualization-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-tf-transformations
BuildRequires:  ros-jazzy-turtlebot3-msgs
BuildRequires:  ros-jazzy-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package provides four basic examples for TurtleBot3 (i.e., interactive
marker, object detection, patrol and position control).

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Apr 16 2025 Pyo <pyo@robotis.com> - 2.2.9-1
- Autogenerated by Bloom

* Mon Apr 14 2025 Pyo <pyo@robotis.com> - 2.2.8-1
- Autogenerated by Bloom

