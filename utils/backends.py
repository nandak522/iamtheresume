from users.models import User

class EmailAuthBackend(object):
    
    supports_object_permissions = False
    supports_anonymous_user = False
    
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    
    def authenticate(self, email, password):
        try:
            user = User.objects.get(email=email.lower(), is_active=True)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None
