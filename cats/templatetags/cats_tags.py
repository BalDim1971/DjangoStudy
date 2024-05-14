from cats.models import TagPost
from women.templatetags.women_tags import register


@register.inclusion_tag('cats/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.all()}
