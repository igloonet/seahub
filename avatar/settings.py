from django.conf import settings

try:
    from PIL import Image
    dir(Image) # Placate PyFlakes
except ImportError:
    import Image

### User avatar settings ###
AVATAR_DEFAULT_SIZE = getattr(settings, 'AVATAR_DEFAULT_SIZE', 80)
AVATAR_STORAGE_DIR = getattr(settings, 'AVATAR_STORAGE_DIR', 'avatars')
AVATAR_DEFAULT_URL = getattr(settings, 'AVATAR_DEFAULT_URL', 'avatar/img/default.jpg')
    
### Group avatars ###
GROUP_AVATAR_DEFAULT_SIZE = getattr(settings, 'GROUP_AVATAR_DEFAULT_SIZE', 48)
GROUP_AVATAR_STORAGE_DIR = getattr(settings, 'GROUP_AVATAR_STORAGE_DIR', 'avatars/groups')
GROUP_AVATAR_DEFAULT_URL = getattr(settings, 'GROUP_AVATAR_DEFAULT_URL', 'avatars/groups/default.png')

### Common settings ###
AUTO_GENERATE_AVATAR_SIZES = getattr(settings, 'AUTO_GENERATE_AVATAR_SIZES', (AVATAR_DEFAULT_SIZE,))
AVATAR_RESIZE_METHOD = getattr(settings, 'AVATAR_RESIZE_METHOD', Image.ANTIALIAS)
AVATAR_GRAVATAR_BACKUP = getattr(settings, 'AVATAR_GRAVATAR_BACKUP', True)
AVATAR_GRAVATAR_DEFAULT = getattr(settings, 'AVATAR_GRAVATAR_DEFAULT', None)
AVATAR_MAX_AVATARS_PER_USER = getattr(settings, 'AVATAR_MAX_AVATARS_PER_USER', 42)
AVATAR_MAX_SIZE = getattr(settings, 'AVATAR_MAX_SIZE', 1024 * 1024)
AVATAR_THUMB_FORMAT = getattr(settings, 'AVATAR_THUMB_FORMAT', "png")
AVATAR_THUMB_QUALITY = getattr(settings, 'AVATAR_THUMB_QUALITY', 85)
AVATAR_HASH_FILENAMES = getattr(settings, 'AVATAR_HASH_FILENAMES', False)
AVATAR_HASH_USERDIRNAMES = getattr(settings, 'AVATAR_HASH_USERDIRNAMES', False)
AVATAR_ALLOWED_FILE_EXTS = getattr(settings, 'AVATAR_ALLOWED_FILE_EXTS', None)
AVATAR_CACHE_TIMEOUT = getattr(settings, 'AVATAR_CACHE_TIMEOUT', 60*60)

