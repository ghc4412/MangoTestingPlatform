from .env import env, env_bool, env_int

# ************************ Data source ************************ #

IS_SQLITE = env_bool('IS_SQLITE', False)

# ************************ MySQL ************************ #

MYSQL_IP = env('MYSQL_IP', 'db')
MYSQL_PORT = env_int('MYSQL_PORT', 3306)
MYSQL_DB_NAME = env('MYSQL_DB_NAME', 'mango_server', aliases=('MYSQL_DATABASE',))
MYSQL_USER = env('MYSQL_USER', 'root')
MYSQL_PASSWORD = env('MYSQL_PASSWORD', '')

# ************************ Debug ************************ #

DEBUG = env_bool('DJANGO_DEBUG', False)
IS_DEBUG_LOG = env_bool('DJANGO_DEBUG_LOG', False)

# ************************ Redis ************************ #

REDIS = env_bool('REDIS', False)

# ************************ MinIO ************************ #

IS_MINIO = env_bool('IS_MINIO', True)
MINIO_STORAGE_ENDPOINT = env('MINIO_STORAGE_ENDPOINT', 'minio:9000', aliases=('MINIO_ENDPOINT',))
MINIO_STORAGE_ACCESS_KEY = env(
    'MINIO_STORAGE_ACCESS_KEY',
    '',
    aliases=('MINIO_ACCESS_KEY', 'MINIO_ROOT_USER'),
)
MINIO_STORAGE_SECRET_KEY = env(
    'MINIO_STORAGE_SECRET_KEY',
    '',
    aliases=('MINIO_SECRET_KEY', 'MINIO_ROOT_PASSWORD'),
)
MINIO_STORAGE_USE_HTTPS = env_bool('MINIO_STORAGE_USE_HTTPS', False, aliases=('MINIO_USE_HTTPS',))
MINIO_STORAGE_MEDIA_BUCKET_NAME = env('MINIO_STORAGE_MEDIA_BUCKET_NAME', 'mango-file', aliases=('MINIO_BUCKET',))
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = env_bool('MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET', True)

# ************************ Runtime switches ************************ #

IS_DELETE = env_bool('IS_DELETE', True)
IS_SEND_MAIL = env_bool('IS_SEND_MAIL', True)
