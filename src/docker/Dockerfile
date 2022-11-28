FROM ros:noetic

LABEL Maintainer="Kota Kondo <kkondo@mit.edu>" \
      Description="Ubuntu 20.04, ROS Noetic for EDG-TEAM"

RUN apt-get update && \
      apt-get upgrade -y && \
      apt-get install -q -y --no-install-recommends git tmux vim apt-utils && \
      apt-get install -q -y --no-install-recommends wget && \
      apt-get install ros-noetic-catkin && \
      apt-get autoremove -y && \
      apt-get install python3-pip -y && \
      apt-get install python3-scipy -y && \
      pip3 install -U bagpy && \
      pip3 install --upgrade numpy && \
      pip3 install python-dateutil==2.8.2 && \
	pip3 install scipy && \
      apt install libzmqpp-dev -y && \
      apt-get clean && \
      apt-get install psmisc && \
      rm -rf /var/lib/apt/lists/*

# the code below is the replacement of "RUN bash src/edg_team/install_and_compile.sh"
#INSTALL CGAL v4.14.2
##########################################
RUN apt-get update && apt-get install python-is-python3 libgmp3-dev libmpfr-dev libarmadillo-dev libeigen3-dev -y

#INSTALL python-catkin-tools (to be able to use catkin build)
##########################################
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
RUN wget http://packages.ros.org/ros.key -O - |  apt-key add -
RUN apt-get update && apt-get install python3-catkin-tools -y

# install EDG TEAM
RUN mkdir -p /home/kota/edg_team_ws/
# RUN git clone https://github.com/kotakondo/EDG-TEAM.git
COPY EDG-TEAM /home/kota/edg_team_ws/EDG-TEAM
RUN DEBIAN_FRONTEND=noninteractive rosdep install --from-paths /home/kota/edg_team_ws/EDG-TEAM/src --ignore-src -r -y
WORKDIR /home/kota/edg_team_ws/EDG-TEAM
RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd /home/kota/edg_team_ws/EDG-TEAM; catkin_make'
RUN echo source /opt/ros/noetic/setup.bash >> ~/.bashrc
RUN echo source /home/kota/edg_team_ws/EDG-TEAM/devel/setup.bash >> ~/.bashrc
RUN echo 'alias cb="catkin build"' >> ~/.bashrc && \
      echo 'alias gs="git status"' >> ~/.bashrc && \
      echo 'alias gp="git push"' >> ~/.bashrc && \
      echo 'alias kr="killall -9 gazebo & killall -9 gzserver  & killall -9 gzclient & pkill -f panther & pkill -f gazebo_ros & pkill -f spawn_model & pkill -f gzserver & pkill -f gzclient  & pkill -f static_transform_publisher &  killall -9 multi_robot_node & killall -9 roscore & killall -9 rosmaster & pkill edg_team_node & pkill -f tracker_predictor & pkill -f swarm_traj_planner & pkill -f dynamic_obstacles & pkill -f rosout & pkill -f behavior_selector_node & pkill -f rviz & pkill -f rqt_gui & pkill -f perfect_tracker & pkill -f edg_team_commands & pkill -f dynamic_corridor & tmux kill-server & pkill -f perfect_controller & pkill -f publish_in_gazebo"' >> ~/.bashrc && \
      echo 'alias py="python"' >> ~/.bashrc && \
      echo 'alias rvmd="roscd edg_team && cd rviz_cfgs && rosrun rviz rviz -d edg_team.rviz"' >> ~/.bashrc && \
      echo 'alias tks="tmux kill-server"' >> ~/.bashrc
RUN mkdir -p /home/kota/data/edg_team
