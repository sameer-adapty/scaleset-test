from lib.flask_mailplus import send_template_message
from snakeeyes.app import create_celery_app
import time

celery = create_celery_app()


@celery.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.

    :param email: E-mail address of the visitor
    :type user_id: str
    :param message: E-mail message
    :type user_id: str
    :return: None
    """

    counter = 50 
    while  counter > 0:
        time.sleep(.5)
        counter = counter -1
        print("Counter :", counter)    
 
    return None
