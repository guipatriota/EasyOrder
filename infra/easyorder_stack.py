"""Configuração da Stack para a infra com AWS CDK."""

from aws_cdk import (
    Stack,
)
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns
from constructs import Construct


class EasyOrderStack(Stack):
    """Stack da aplicação EasyOrder."""

    def __init__(
        self, scope: Construct, construct_id: str, *, image_tag: str, **kwargs
    ):
        """Inicializa a stack da aplicação EasyOrder."""
        super().__init__(scope, construct_id, **kwargs)

        # VPC (2 AZs, suficiente para demo)
        vpc = ec2.Vpc(self, "Vpc", max_azs=2)

        # ec2_teste = ec2.Instance(self, "Ec2Teste",
        #     instance_type=ec2.InstanceType("t2.micro"),
        #     machine_image=ec2.MachineImage.linux_ubuntu2204(),
        #     vpc=vpc
        # )

        # Cluster ECS
        cluster = ecs.Cluster(self, "Cluster", vpc=vpc)

        # ECR repo (assuma que já existe ou deixe o CDK criar)
        repo = ecr.Repository.from_repository_name(
            self, "Repo", repository_name="easyorder"
        )

        # Imagem com tag dinamico (passado pelo GitHub Actions
        # via -c imageTag=...)
        image = ecs.ContainerImage.from_ecr_repository(repo, tag=image_tag)

        # Serviço Fargate com ALB público
        svc = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "Service",
            cluster=cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=1,
            public_load_balancer=True,
            task_image_options=(
                ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                    image=image,
                    container_port=8000,
                    enable_logging=True,
                )
            ),
        )

        # Auto scaling (opcional)
        scalable = svc.service.auto_scale_task_count(
            min_capacity=1, max_capacity=1
        )
        scalable.scale_on_cpu_utilization(
            "CpuScaling", target_utilization_percent=60
        )
