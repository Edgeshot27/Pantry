# # firebase_orm/__init__.py
#
# import firebase_admin
# from firebase_admin import credentials
# from django.conf import settings
# from django.core.exceptions import ImproperlyConfigured
#
# # Ensure these settings are correctly pointing to your Firebase setup
# CERTIFICATE = getattr(settings, "FIREBASE_ORM_CERTIFICATE", None)
# BUCKET_NAME = getattr(settings, "FIREBASE_ORM_BUCKET_NAME", None)
#
# if CERTIFICATE is None:
#     raise ImproperlyConfigured("You haven't set the FIREBASE_ORM_CERTIFICATE in your settings.py")
# if BUCKET_NAME is None:
#     raise ImproperlyConfigured("You haven't set the FIREBASE_ORM_BUCKET_NAME in your settings.py")
#
# firebase_admin.initialize_app(
#     credentials.Certificate(CERTIFICATE),
#     {"storageBucket": BUCKET_NAME}
# )
