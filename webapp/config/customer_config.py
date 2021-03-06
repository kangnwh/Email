# -*- coding: utf-8 -*-
import webapp
import os

# upload folder
base_dir = webapp.__file__
PROD_UPLOAD_PATH = "{base_dir}{sep}static{sep}img{sep}products{sep}".format(base_dir=os.path.dirname(base_dir), sep=os.sep)
USER_LOGO_UPLOAD_PATH = "{base_dir}{sep}static{sep}img{sep}user_logos{sep}".format(base_dir=os.path.dirname(base_dir), sep=os.sep)

PROD_NUM_PER_PAGE = 9
USER_NUM_PER_PAGE = 20
FEEDBACK_NUM_PER_PAGE = 10
USER_ORDER_PER_PAGE = 20
USER_QUOTE_PER_PAGE = 20
AD_LIST_PER_PAGE = 10

ALLOWED_EXTENSIONS=set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','TXT', 'PDF', 'PNG', 'JPG', 'JPEG', 'GIF'])


# MAIL_SERVER = 'smtp.tom.com'# 'smtp.163.com'
# MAIL_PORT = 25
# MAIL_USE_SSL = False
# MAIL_USE_TLS = False
# MAIL_USERNAME = 'emalltest'
# MAIL_DEFAULT_SENDER = 'emalltest@tom.com'
# MAIL_PASSWORD = 'passw0rd'

#qq mail : 1131725367@qq.com passw0rd
MAIL_SERVER = 'smtp.qq.com'# 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = '1412796539'
MAIL_DEFAULT_SENDER = '1412796539@qq.com'
MAIL_PASSWORD = 'frglisxtrsuegjeb'

# MAIL_SERVER = 'smtp.163.com'# 'smtp.163.com'
# MAIL_PORT = 465
# MAIL_USE_SSL = True
# MAIL_USE_TLS = False
# MAIL_USERNAME = 'emalltest'
# MAIL_DEFAULT_SENDER = 'emalltest@163.com'
# MAIL_PASSWORD = 'emalltest2'

ADMIN_EMAIL = ["792564101@qq.com","1412796539@qq.com"]

USER_POINT_DISCOUNT_RATE=1



REMINDER_PRE_DAYS=2



ORDER_STATUS_MAP={
    #0:'default',
    1:'User Submitted',
    2:'Supplier Checked',
    3:'Product On The Way',
    4:'User Feedback Submitted',
    5:'Finished',
    6:'User Canceled',
    7:'Supplier Canceled',
    8:'Admin Canceled'
}

QUOTE_STATUS_MAP={
    0:'User Submitted',
    1:'Supplier Replied'
}

APPROVAL_STATUS_MAP={
    -1:["Rejected","danger"],
    0:["Approval Pending","info"],
    1:["Approved","success"]
}

VALID_INFO_MAP={
    #valid_flg:[valid_info,valid_class]
    0:["UnShelve","danger"],
    1:["On Show","success"]
}
#1 submitted by supplier,2 approved by armin, 3 ad sent out
AD_STATUS_MAP={
    1:["Submitted","info"],
    2:["Approved","info"],
    3:["Sent Out","success"],
    -1:["Rejected","danger"]
}

RATE_NOTIFICATION="There will be an add-up rate when users buy this product."