import boto3
import time
import logging

logger = logging.getLogger(__name__)

def invalidate_cloudfront_cache(tool_input=None)-> str:

    logger.info("Inside cloudfront cache method...")
    # Create CloudFront client
    client = boto3.client('cloudfront')

    # Your CloudFront distribution ID
    distribution_id = "E2IHQN1MUS8MW8"

    # Generate a unique caller reference (must be unique per request)
    caller_reference = str(time.time())

    # Create invalidation request   §
    try:
        response = client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        '/index.html',   # ✅ path(s) you want to invalidate
                        # You can also use '/*' to invalidate everything
                    ]
                },
                'CallerReference': caller_reference
            }
        )

        logger.info("Invalidation created:")
    except Exception as e:
        logger.error(f"error occured while invalidating the cache..{e}")    

    logger.fatal(f"Status:, {response['Invalidation']['Status']},ID:{response['Invalidation']['Id']}")

    return f"Status:, {response['Invalidation']['Status']},ID:{response['Invalidation']['Id']}"
