from webapp.common.mails import deliver_notification
from flask_apscheduler import APScheduler
scheduler = APScheduler()


SCHEDULER_API_ENABLED = True
JOBS = [
        {
            'id': 'deliver_notification',
            'func': deliver_notification,
            'args': None,
            'trigger': 'cron',
            'hour': 21,
            'minute':1,
            'second':0
        }
    ]
