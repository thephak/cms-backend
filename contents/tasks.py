from .models import Content, DRAFT, PUBLISHED
from celery import shared_task
from datetime import datetime, timezone

@shared_task
def publish_content():
    print(f"Checking draft content...")
    first_draft = Content.objects.filter(status=DRAFT).order_by("id").first()

    if first_draft:
        print(f"Content {first_draft.title} [{first_draft.id}]")
        first_draft.status = PUBLISHED
        first_draft.published_date = datetime.now(timezone.utc)
        first_draft.save()
    return (f"Content {first_draft.title} [{first_draft.id}] has been published.")