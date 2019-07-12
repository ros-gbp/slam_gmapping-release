Name:           ros-melodic-gmapping
Version:        1.4.0
Release:        1%{?dist}
Summary:        ROS gmapping package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/gmapping
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-openslam-gmapping
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-catkin >= 0.5.68
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-openslam-gmapping
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-tf

%description
This package contains a ROS wrapper for OpenSlam's Gmapping. The gmapping
package provides laser-based SLAM (Simultaneous Localization and Mapping), as a
ROS node called slam_gmapping. Using slam_gmapping, you can create a 2-D
occupancy grid map (like a building floorplan) from laser and pose data
collected by a mobile robot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Jul 12 2019 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.4.0-1
- Autogenerated by Bloom

* Fri Jul 12 2019 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.3.10-1
- Autogenerated by Bloom

