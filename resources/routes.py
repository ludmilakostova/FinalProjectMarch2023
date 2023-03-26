from resources.auth import RegisterResource, LogInResource
from resources.complaint import ComplaintsResource, ComplaintRejectResource, ComplaintApproveResource

routes = ((RegisterResource, "/register"),
          (LogInResource, "/login"),
          (ComplaintsResource, "/complaints"),
          (ComplaintApproveResource, "/complaints/<int:pk>/approve"),
         (ComplaintRejectResource, "/complaints/<int:pk>/reject")
          )
            # TODO : new URL for single complaint
