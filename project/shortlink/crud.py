from .models import Links_log , Links , packets_log


def create_link_log( **kwargs):

    return Links_log.objects.create(**kwargs)


def update_count_view(link):
    link.count_view +=1
    link.save()