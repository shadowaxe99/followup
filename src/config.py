```python
# src/config.py

# Gmail API credentials
GMAIL_API_CREDENTIALS = {
    'client_id': 'your_client_id',
    'client_secret': 'your_client_secret',
    'redirect_uris': ['your_redirect_uris'],
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token'
}

# OpenAI GPT-3 API Key
OPENAI_API_KEY = 'your_openai_api_key'

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'password',
    'database': 'email_followup'
}

# Email follow-up trigger conditions
TRIGGER_CONDITIONS = {
    'business_owner': {
        'days_after': 2
    },
    'job_seeker': {
        'days_after': 7
    }
}

# Performance metrics
PERFORMANCE_METRICS = {
    'open_rate': 0,
    'click_through_rate': 0
}

# DOM Element IDs
DOM_ELEMENT_IDS = {
    'login_form': 'loginForm',
    'dashboard': 'dashboard',
    'trigger_form': 'triggerForm',
    'follow_up_form': 'followUpForm',
    'metrics_display': 'metricsDisplay'
}

# Message Names
MESSAGE_NAMES = {
    'login_success': 'Login successful!',
    'trigger_set_success': 'Trigger set successfully!',
    'follow_up_set_success': 'Follow-up email set successfully!',
    'metrics_update': 'Performance metrics updated!'
}
```