;; Auto-generated. Do not edit!


(when (boundp 'demo01_action::AddintsResult)
  (if (not (find-package "DEMO01_ACTION"))
    (make-package "DEMO01_ACTION"))
  (shadow 'AddintsResult (find-package "DEMO01_ACTION")))
(unless (find-package "DEMO01_ACTION::ADDINTSRESULT")
  (make-package "DEMO01_ACTION::ADDINTSRESULT"))

(in-package "ROS")
;;//! \htmlinclude AddintsResult.msg.html


(defclass demo01_action::AddintsResult
  :super ros::object
  :slots (_result ))

(defmethod demo01_action::AddintsResult
  (:init
   (&key
    ((:result __result) 0)
    )
   (send-super :init)
   (setq _result (round __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; int32 _result
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _result
       (write-long _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _result
     (setq _result (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get demo01_action::AddintsResult :md5sum-) "034a8e20d6a306665e3a5b340fab3f09")
(setf (get demo01_action::AddintsResult :datatype-) "demo01_action/AddintsResult")
(setf (get demo01_action::AddintsResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#2.最终反馈变量
int32 result

")



(provide :demo01_action/AddintsResult "034a8e20d6a306665e3a5b340fab3f09")


