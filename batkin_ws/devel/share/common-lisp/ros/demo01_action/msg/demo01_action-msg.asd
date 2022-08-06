
(cl:in-package :asdf)

(defsystem "demo01_action-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "AddintsAction" :depends-on ("_package_AddintsAction"))
    (:file "_package_AddintsAction" :depends-on ("_package"))
    (:file "AddintsActionFeedback" :depends-on ("_package_AddintsActionFeedback"))
    (:file "_package_AddintsActionFeedback" :depends-on ("_package"))
    (:file "AddintsActionGoal" :depends-on ("_package_AddintsActionGoal"))
    (:file "_package_AddintsActionGoal" :depends-on ("_package"))
    (:file "AddintsActionResult" :depends-on ("_package_AddintsActionResult"))
    (:file "_package_AddintsActionResult" :depends-on ("_package"))
    (:file "AddintsFeedback" :depends-on ("_package_AddintsFeedback"))
    (:file "_package_AddintsFeedback" :depends-on ("_package"))
    (:file "AddintsGoal" :depends-on ("_package_AddintsGoal"))
    (:file "_package_AddintsGoal" :depends-on ("_package"))
    (:file "AddintsResult" :depends-on ("_package_AddintsResult"))
    (:file "_package_AddintsResult" :depends-on ("_package"))
  ))