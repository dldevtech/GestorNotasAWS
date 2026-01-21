import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    note_id = str(uuid.uuid4())
    userId = 11
    content = event.get("content", "Nota vacía")

    table.put_item(
        Item={
            "userId": userId,
            "noteId": note_id,
            "content": content
        }
    )

    return {
        "status": "ok",
        "noteId": note_id
    }
