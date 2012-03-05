Django Resumes by Juan C. Yunis
=================================

Django Resume provides a easy way to create and generate Resumes/CV.

Installation
************

1. Add ``"resumes"`` to ``INSTALLED_APPS`` settings.
2. Run syncdb or migrate resumes, if you have installed south.
3. Add (r'^resumes/', include('resumes.urls')) to your main urls.py
