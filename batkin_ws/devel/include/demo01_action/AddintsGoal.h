// Generated by gencpp from file demo01_action/AddintsGoal.msg
// DO NOT EDIT!


#ifndef DEMO01_ACTION_MESSAGE_ADDINTSGOAL_H
#define DEMO01_ACTION_MESSAGE_ADDINTSGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace demo01_action
{
template <class ContainerAllocator>
struct AddintsGoal_
{
  typedef AddintsGoal_<ContainerAllocator> Type;

  AddintsGoal_()
    : num(0)  {
    }
  AddintsGoal_(const ContainerAllocator& _alloc)
    : num(0)  {
  (void)_alloc;
    }



   typedef int32_t _num_type;
  _num_type num;





  typedef boost::shared_ptr< ::demo01_action::AddintsGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::demo01_action::AddintsGoal_<ContainerAllocator> const> ConstPtr;

}; // struct AddintsGoal_

typedef ::demo01_action::AddintsGoal_<std::allocator<void> > AddintsGoal;

typedef boost::shared_ptr< ::demo01_action::AddintsGoal > AddintsGoalPtr;
typedef boost::shared_ptr< ::demo01_action::AddintsGoal const> AddintsGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::demo01_action::AddintsGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::demo01_action::AddintsGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::demo01_action::AddintsGoal_<ContainerAllocator1> & lhs, const ::demo01_action::AddintsGoal_<ContainerAllocator2> & rhs)
{
  return lhs.num == rhs.num;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::demo01_action::AddintsGoal_<ContainerAllocator1> & lhs, const ::demo01_action::AddintsGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace demo01_action

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::demo01_action::AddintsGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::demo01_action::AddintsGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::demo01_action::AddintsGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::demo01_action::AddintsGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::demo01_action::AddintsGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::demo01_action::AddintsGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::demo01_action::AddintsGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "54b3c80efd6fae6e6ffff8a4b9facd69";
  }

  static const char* value(const ::demo01_action::AddintsGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x54b3c80efd6fae6eULL;
  static const uint64_t static_value2 = 0x6ffff8a4b9facd69ULL;
};

template<class ContainerAllocator>
struct DataType< ::demo01_action::AddintsGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "demo01_action/AddintsGoal";
  }

  static const char* value(const ::demo01_action::AddintsGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::demo01_action::AddintsGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# 1.目标数据变量\n"
"int32 num\n"
;
  }

  static const char* value(const ::demo01_action::AddintsGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::demo01_action::AddintsGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.num);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AddintsGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::demo01_action::AddintsGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::demo01_action::AddintsGoal_<ContainerAllocator>& v)
  {
    s << indent << "num: ";
    Printer<int32_t>::stream(s, indent + "  ", v.num);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEMO01_ACTION_MESSAGE_ADDINTSGOAL_H
