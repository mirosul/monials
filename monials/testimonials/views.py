from testimonials.models import Profile, Testimonial
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

def embed(request, profile_id):
  # profil = Profile.objects.get(pk = profile_id)
  profil = get_object_or_404(Profile, pk = profile_id)
  testimonials = get_list_or_404(Testimonial, profile = profil)
  return render_to_response('embed.html', {'profil': profil, 'testimonials': testimonials})
