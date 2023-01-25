resource "aws_iam_policy" "lambda_ddb_policy" {
  name_prefix = "panda_ddb_policy"
  path        = "/"
  description = "Allow access to DDB table"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "dynamodb:UpdateItem"
        ],
        Effect   = "Allow"
        Sid      = "DDBAccess"
        Resource = "arn:aws:dynamodb:${var.region}:${data.aws_caller_identity.current.account_id}:table/gatewayCounter"
      }
    ]
  })
}

resource "aws_iam_role" "lambda_execution_role" {
  name_prefix = "codecatalyst-demo-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_role_basic_policy_attachment" {
  role       = aws_iam_role.lambda_execution_role.name
  # policy_arn = aws_iam_policy.lambda_logging_policy.arn
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "lambda_role_ddb_policy_attachment" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn = aws_iam_policy.lambda_ddb_policy.arn
}