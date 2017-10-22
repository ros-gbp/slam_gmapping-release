Name:           ros-indigo-gmapping
Version:        1.3.9
Release:        0%{?dist}
Summary:        ROS gmapping package

Group:          Development/Libraries
License:        CreativeCommons-by-nc-sa-2.0
URL:            http://ros.org/wiki/gmapping
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-openslam-gmapping
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-openslam-gmapping
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-tf

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Oct 22 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.3.9-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.3.8-0
- Autogenerated by Bloom

* Sat Jul 04 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.3.7-0
- Autogenerated by Bloom

