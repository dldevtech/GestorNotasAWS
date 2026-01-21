import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    
    userId = event.get("userId")
    noteId = event.get("noteId")

    response = table.delete_item(
        Key={
            "userId": userId,
            "noteId": noteId
        },
        ReturnValues="ALL_OLD"
    )

    deleted_item = response.get("Attributes")
    if deleted_item is None:
        print("No se ha encontrado la nota para borrar")
        return {
        "status": "not_found",
        "message": "No existe ninguna nota con ese userId y noteId" 
    }

    print("Nota eliminada correctamente:", deleted_item)
    
    return {
        "status": "ok",
        "deleted": deleted_item
    }