"""Infra com AWS CDK."""

from aws_cdk import (  # Duration,; aws_sqs as sqs,
    Stack,
)
from constructs import Construct


class InfraStack(Stack):
    """Stack da infraestrutura."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """Inicializa a stack da infraestrutura."""
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "InfraQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
