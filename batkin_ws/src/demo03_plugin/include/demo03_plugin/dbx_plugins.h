#ifndef DBX_PLUGINS_H_
#define DBX_PLUGINS_H_
#include "demo03_plugin/dbx_base.h"

namespace dbx_plugins_ns
{
  class Triangle : public polygon_base::RegularPolygon
  {
    public:
      Triangle(){
        side_length = 0.0;
      }
      void init(double side_length)
      {
        this->side_length = side_length;
      }
      double getlength()
      {
        return side_length * 3;
      }

    private:
      double side_length;
  };

  class Square : public polygon_base::RegularPolygon
  {
    private:
      double side_length;

    public:
      Square(){
        side_length = 0.0;
      }
      void init(double side_length)
      {
        this->side_length = side_length;
      }
      double getlength()
      {
        return side_length * 4;
      }

  };
};
#endif
