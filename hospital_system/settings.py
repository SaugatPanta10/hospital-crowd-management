import os
from pathlib import Path

# ==============================================================================
# 1. CORE PATHS & ENVIRONMENT CONFIGURATION
# ==============================================================================

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 🛠️ UPGRADED NATIVE .ENV PARSER (Loads configuration data offline without dependencies)
env_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_path):
    with open(env_path, 'r', encoding = 'utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                # Clean off trailing whitespace and any surrounding single/double quotes
                clean_value = value.strip().strip("'").strip('"')
                os.environ[key.strip()] = clean_value

# 🔒 SECURE DECOUPLING: Extracted out of system memory
SECRET_KEY = os.getenv('SECRET_KEY')

# Bulletproof boolean check: evaluates cleanly against string parameters
DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1']

# Accessible hosts deployment array
ALLOWED_HOSTS = ['*']


# ==============================================================================
# 2. APPLICATION DEFINITIONS
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # Active Messaging Framework
    'django.contrib.staticfiles',
    
    # Your core application
    'records', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Processes message alerts
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospital_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Templates are stored inside app subdirectories
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',  # Makes messages accessible in HTML
            ],
        },
    },
]

WSGI_APPLICATION = 'hospital_system.wsgi.application'


# ==============================================================================
# 3. DATABASE CONFIGURATION
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================================================================
# 4. AUTHENTICATION & ACCESS ROUTING
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Automated Login / Logout Navigation Anchors
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'doctor_dashboard'
LOGOUT_REDIRECT_URL = 'home'


# ==============================================================================
# 5. INTERNATIONALIZATION & LOCALIZATION
# ==============================================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ==============================================================================
# 6. STATIC FILES & STORAGE MECHANICS
# ==============================================================================

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'