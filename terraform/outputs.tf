output "aws_account_id" {
    value = data.aws_caller_identity.current.account_id
}

output "api_gateway_url" {
    value = aws_api_gateway_deployment.apideploy.invoke_url
}
