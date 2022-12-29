from background_task import background
from Wappalyzer import Wappalyzer, WebPage
from tags.models import Tag
from scans.models import Scan
import json
from django.db.models import Q

from django_redis import get_redis_connection


@background(schedule=60)
def analyze(scan_id, domain):
    error_msg = None
    scan = None
    publish_event()
    try:
        scan = Scan.objects.get(pk=scan_id)
        scan.phase = "Running"
        scan.save()
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(domain)
        res = wappalyzer.analyze_with_versions_and_categories(webpage)
    except Exception as e:
        res = None
        error_msg = str(e)
        print("Message: ", str(e))

    if res is None:
        scan.phase = "Error"
        scan.errors = error_msg
        scan.save()
    else:
        scan.phase = "Complete"
        scan.errors = None
        scan.save()
        for k, v in res.items():
            technology = k
            versions = v.get('versions', [])
            if versions:
                versions.sort()

            categories = v.get('categories', [])
            if categories:
                categories.sort()

            version_str = json.dumps(versions)
            categories_str = json.dumps(categories).replace('\\"', "\"")

            print(version_str)
            print(categories_str)

            try:
                tags = Tag.objects.filter(Q(name=technology) & Q(categories=categories_str) & Q(versions=version_str))
                if not tags:
                    # create tag
                    tag = Tag.objects.create(name=technology, versions=version_str, categories=categories_str)
                else:
                    tag = tags[0]

                scan.tags.add(tag)
            except Exception as e:
                print("Error Message: ", str(e))


def publish_event():
    print("eventttttttttttttttt")
    event = {
        "name": "Omar",
        "id": 123,
        "message": "This is a dummy message"
    }
    connection = get_redis_connection("default")
    payload = json.dumps(event)
    connection.publish("events", payload)

