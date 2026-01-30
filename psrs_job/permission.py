from rest_framework.permissions import BasePermission






class  IsRecuiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.role =='RECRUITER'
    

class IsApplicant(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'APPLICANT'
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'