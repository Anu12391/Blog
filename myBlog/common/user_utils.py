from login.models import NewUser




def createNewUser(cleaned_data):
    data = cleaned_data.copy()
    data.pop('confirm_password', None)

    return NewUser.objects.create_user(**data)