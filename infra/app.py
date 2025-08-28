"""Infra com AWS CDK."""

import os

from aws_cdk import App, Environment, LegacyStackSynthesizer
from easyorder_stack import EasyOrderStack

app = App()
image_tag = app.node.try_get_context("imageTag") or "latest"
env = Environment(
    account=os.environ.get("CDK_DEFAULT_ACCOUNT"),  # Uso do OIDC
    region=os.environ.get("CDK_DEFAULT_REGION"),
)

EasyOrderStack(
    app,
    "EasyOrderStack",  # O mesmo configurado em github secrets CDK_STACK_NAME
    image_tag=image_tag,
    env=env,
    synthesizer=LegacyStackSynthesizer(),
)

app.synth()
