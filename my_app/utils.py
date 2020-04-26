from my_app.models import User


def update_user(data, id):
    author_ = User.objects.get(id=id)
    for key in data:
        author_[key] = data[key]
    author_.save()
