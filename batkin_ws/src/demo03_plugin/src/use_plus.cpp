#include "ros/ros.h"
#include "pluginlib/class_loader.h"
#include "demo03_plugin/dbx_base.h"
#include "demo03_plugin/dbx_plugins.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    pluginlib::ClassLoader<polygon_base::RegularPolygon> loader("demo03_plugin","polygon_base::RegularPolygon");

    boost::shared_ptr<polygon_base::RegularPolygon> san = loader.createInstance("dbx_plugins_ns::Triangle");
    san->init(10);
    double length = san->getlength();
    ROS_INFO("三角形周长:%.2f",length);

    boost::shared_ptr<polygon_base::RegularPolygon> si = loader.createInstance("dbx_plugins_ns::Square");
    si->init(10);
    double length2 = si->getlength();
    ROS_INFO("四边形边长:%.2f",length2);

    return 0;
}
