from testimonials.models import Profile
from testimonials.models import Testimonial
from django.contrib import admin

class TestimonialInline(admin.StackedInline):
  model = Testimonial
  extra = 2

class ProfileAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields':['name']}),
  ]
  inlines = [TestimonialInline]
  
admin.site.register(Profile, ProfileAdmin)

