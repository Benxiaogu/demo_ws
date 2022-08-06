#ifndef DBX_BASE_H_
#define DBX_BASE_H_

namespace polygon_base
{
  class RegularPolygon
  {
    protected:
      RegularPolygon(){}

    public:
      virtual void init(double side_length) = 0;
      virtual double getlength() = 0;

  };
};
#endif
