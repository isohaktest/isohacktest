from webhooks import webhook
from webhooks.sender import targeted

@webhook(sender_callable=targeted.sender)@webhook(sender_callable=targeted.sender)
