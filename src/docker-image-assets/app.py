from aws_cdk import App
from cdk.api_gateway_stack import ApiGatewayStack
from cdk.ecr_lambda_stack import EcrPublicListStack

app = App()

api_stack = ApiGatewayStack(app, "ApiGatewayStack")

EcrPublicListStack(
    app, "EcrPublicListStack",
    rest_api=api_stack.rest_api,
    images_resource=api_stack.images_resource
)

app.synth()
