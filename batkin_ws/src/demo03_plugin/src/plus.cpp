#include "pluginlib/class_list_macros.h"
#include "demo03_plugin/dbx_base.h"
#include "demo03_plugin/dbx_plugins.h"

PLUGINLIB_EXPORT_CLASS(dbx_plugins_ns::Triangle,polygon_base::RegularPolygon)
PLUGINLIB_EXPORT_CLASS(dbx_plugins_ns::Square,polygon_base::RegularPolygon)
