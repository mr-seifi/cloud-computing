from celery import shared_task
from .models import Ad


@shared_task
def tag_covers(ad_id):

    from .services import ImageProcessingService, MailService
    ad = Ad.objects.filter(id=ad_id).first()

    img_processing_service = ImageProcessingService()
    tag = img_processing_service.tags(image_url=ad.cover.url.split('?')[0])

    mail_service = MailService()
    if tag == 'car':
        ad.category = 'car'
        ad.approved = True
        ad.save()

        mail_service.send(to=ad.user.email, subject='Ad response', text='Your ad sent successfully!')
        return

    mail_service.send(to=ad.user.email, subject='Ad response', text='Your ad did not send!')


@shared_task
def push_rabbitmq(ad_id):

    from .services import AMPQService, MailService
    ad = Ad.objects.filter(id=ad_id).first()

    ampq_service = AMPQService()
    ampq_service.publish(ad_id)

    mail_service = MailService()
    mail_service.send(to=ad.user.email, subject='Ad submitted', text='Your ad submitted successfully!')
