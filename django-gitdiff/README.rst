To integrate into your application:

Install the requirements.

Include 'gitdiffmatch' in settings.INSTALLED_APPS.

Include gitdiffmatch urls in urls.py

url(r'^gitdiffmatch/', include('gitdiffmatch.urls')),

from utils import find_diffs  //it's takes 2 input files and returns their diffs

Check at  /gitdiffmatch/.
