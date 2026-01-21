import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler (event, context):

    userId = event.get("userId")
    noteId = event.get("noteId")
    content = event.get("content")

    response = table.update_item(
        Key={
            "userId": userId,
            "noteId": noteId
        },
        UpdateExpression="SET content = :newContent",
        ExpressionAttributeValues={
            ":newContent": content
        },
        ReturnValues="ALL_NEW"
    )

    updated_item = response.get("Attributes")

    print("nota actualizada:", updated_item)

    return{
        "status": "ok",
        "updated": updated_item
    }