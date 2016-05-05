from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]


'''
Add a slug field to your Blog model.

from django.template.defaultfilters import slugify

Class Blog(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(_('slug'), max_length=60, blank=True)

    #Then override models save method:
    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title)
            #Or whatever you want the slug to use
        super(Blog, self).save(*args, **kwargs)
In your urls.py

(r'^blog/view/(?P<slug>[-\w]+)/$', 'app.views.blog_view'),
In views.py

def blog_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    #Then do whatever you want
'''
