class AuthUrls:

    class Register:
        register_subUrl="register/"
        register_reverseName='register_new_user'

    class Login:
        login_subUrl="login/"
        login_reverseName="login_user"

    class Logout:
        logout_subUrl = "logout/"
        logout_reverseName = "logout_user"

    class UserActivation:
        activate_subUrl = "'activate/<str:uidb64>/<str:token>/'"
        activate_reverseName = 'activate'

    class ForgotPassword:
        forgot_password_subUrl = 'forgot_password/'
        forgot_password_reverseName = 'forgot_password'

    class PasswordReset:
        reset_password_subUrl = 'reset_password/<str:uidb64>/<str:token>/'
        reset_password_reverseName = 'reset_password'










