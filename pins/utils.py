from google.cloud import storage
from django.conf import settings


def save_image_to_google_cloud_storage(image_file):
    # Set up Google Cloud Storage client
    client = storage.Client(project=settings.GS_PROJECT_ID)

    # Get the bucket
    bucket = client.get_bucket(settings.GS_BUCKET_NAME)

    # Generate a unique filename or use some logic to generate the filename as needed
    filename = generate_unique_filename(image_file.name)

    # Create a Blob object with the desired filename
    blob = bucket.blob(filename)

    # Upload the image file to Google Cloud Storage
    blob.upload_from_string(
        image_file.read(), content_type=image_file.content_type)

    # Get the public URL of the uploaded file
    gs_path = f'https://storage.googleapis.com/{settings.GS_BUCKET_NAME}/{filename}'

    return gs_path


def generate_unique_filename(original_filename):
    # You can implement your logic to generate a unique filename here
    # For example, you can use a combination of timestamp and the original filename
    import uuid
    unique_id = str(uuid.uuid4())
    _, extension = original_filename.split('.')
    return f'{unique_id}.{extension}'
