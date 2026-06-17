from common.Constants.ApplicationNames import AppNames as APP


class AuthUrls:

    class Dashboard:
        dashboard_subUrl = ""
        dashboard_reverseName = 'home'
        dashboard_redirectName = f"{APP.DashBoardApp.app_name}:{dashboard_reverseName}"

    class Register:
        register_subUrl="register/"
        register_reverseName='register_new_user'
        register_redirectName = f"{APP.AuthApp.app_name}:{register_reverseName}"

    class Login:
        login_subUrl="login/"
        login_reverseName="login_user"
        login_redirectName=f"{APP.AuthApp.app_name}:{login_reverseName}"

    class Logout:
        logout_subUrl = "logout/"
        logout_reverseName = "logout_user"
        logout_redirectName = f"{APP.AuthApp.app_name}:{logout_reverseName}"

    class UserActivation:
        activate_subUrl = "'activate/<str:uidb64>/<str:token>/'"
        activate_reverseName = 'activate'

    class ForgotPassword:
        forgot_password_subUrl = 'forgot_password/'
        forgot_password_reverseName = 'forgot_password'
        forgot_password_redirectName = f"{APP.AuthApp.app_name}:{forgot_password_reverseName}"

    class PasswordReset:
        reset_password_subUrl = 'reset_password/<str:uidb64>/<str:token>/'
        reset_password_reverseName = 'reset_password'
        reset_password_redirectName = f"{APP.AuthApp.app_name}:{reset_password_reverseName}"


    class MyProfile:
        myProfile_subUrl = "profile/"
        myProfile_reverseName = 'myprofile'
        myProfile_redirectName = f"{APP.MyProfile.app_name}:{myProfile_reverseName}"

    class MyTopics:
        myTopics_subUrl = "my-topics/"
        myTopics_reverseName = 'myTopics'
        myTopics_redirectName = f"{APP.MySettings.app_name}:{myTopics_reverseName}"










