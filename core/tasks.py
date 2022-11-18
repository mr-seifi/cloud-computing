from celery import shared_task
from .models import Ad


@shared_task
def tag_covers(ad_id):

    from .services import ImageProcessingService
    ad = Ad.objects.filter(id=ad_id).first()

    img_processing_service = ImageProcessingService()
    tag = img_processing_service.tags(image_url=ad.cover.url.split('?')[0])

    if tag == 'car':
        ad.category = 'car'
        ad.approved = True
        ad.save()

    # TODO: Send mail
