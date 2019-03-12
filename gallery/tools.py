from azure.storage.blob.blockblobservice import BlockBlobService
from azure.storage.blob import ContentSettings
from gallery import app
import os


bbs = BlockBlobService(
    account_name=app.config['AZURE_STORAGE_ACCOUNT_NAME'],
    account_key=app.config['AZURE_STORAGE_ACCOUNT_KEY']
)


def upload_file_to_azure(file):

    try:

        dir_path = os.path.dirname(os.path.realpath(__file__))
        temp_dir = dir_path + '/' + file.filename
        file.save(dst=temp_dir)

        bbs.create_blob_from_path(
            container_name=app.config['AZURE_STORAGE_CONTAINER_NAME'],
            blob_name=file.filename,
            file_path=temp_dir,
            content_settings=ContentSettings(content_type=file.content_type)
        )

        os.remove(temp_dir)

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(app.config["AZURE_STORAGE_CONTAINER_LOCATION"], file.filename)


def list_files_in_azure():
    try:
        objects = bbs.list_blobs(app.config['AZURE_STORAGE_CONTAINER_NAME'])

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return objects


def delete_file_from_azure(name):
    try:
        response = bbs.delete_blob(
            container_name=app.config['AZURE_STORAGE_CONTAINER_NAME'],
            blob_name=name,
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return response
