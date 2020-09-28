from datetime import time, datetime, timedelta
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


def push_folder(folder_name, current_time, file_type='.jpeg'):

    # Create a unique name for the container
    container_name = folder_name.replace('_', '-') + '-' + current_time

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    images_out_path = os.getcwd() + '/' + folder_name + '/'
    for filename in os.listdir(images_out_path):
        if file_type in filename:
            with open(os.path.join(images_out_path, filename), 'rb') as f:
                print("Uploading: {} to {}".format(filename, container_name ))
                # Create a blob client using the local file name as the name for the blob
                blob_client = blob_service_client.get_blob_client(container=container_name , blob=filename)
                blob_client.upload_blob(f)



current_time = str(datetime.now().isoformat(timespec='minutes')).replace(':','-').lower()
try:
    print("Azure Blob storage v" + __version__ + " - CloudVision Project!")
    # Quick start code goes here
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    push_folder("images_out", current_time)
    push_folder("images", current_time)

except Exception as ex:
    print('Exception:')
    print(ex)
