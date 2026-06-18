from mySettings.models import Topics


def getAllToipcs():
    all_topics = Topics.objects.all()
    return all_topics