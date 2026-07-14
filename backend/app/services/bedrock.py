import boto3
from botocore.exceptions import ClientError

from simpleText.backend.app.config import settings


class BedrockService:
    
    def __init__(self):
        
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=settings.AWS_REGION
        )
        
        self.model_id = settings.BEDROCK_MODEL_ID
    
    
    def generate_response(self, user_message: str) -> str:
        
        conversation = [
            {
                "role": "user",
                "content": [{"text": user_message}],
            }
        ]
        
        try:
            response = self.client.converse(
                modelId=self.model_id,
                messages=conversation,
                inferenceConfig={
                    "maxTokens": 512,
                    "temperature": 0.5,
                    "topP": 0.9
                }
            )
            
            return response["output"]["message"]["content"][0]["text"]
        
        except (ClientError, Exception) as e:
            raise RuntimeError(f"Bedrock API call failed: {str(e)}")

bedrock_service = BedrockService()