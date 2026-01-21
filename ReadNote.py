import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler (event, context):

    userId = event.get("userId")
    noteId = event.get("noteId")

    response = table.get_item(
        Key={
            "userId": userId,
            "noteId": noteId
        }
    )

    item = response.get("Item")
    if not item:
        return {
            "status": "error",
            "message": "Nota no encontrada"
        }
    
    return {
        "status": "ok",
        "note" : item
    }