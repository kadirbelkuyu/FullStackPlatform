provider "aws" {
  region = "<AWS_REGION>"
  access_key = "<AWS_ACCESS_KEY>"
  secret_key = "<AWS_SECRET_KEY>"
}

module "eks" {
  source       = "terraform-aws-modules/eks/aws"
  cluster_name = "my-cluster"
  subnets      = ["subnet-abcde012", "subnet-bcde012a", "subnet-fghi345a"]
  vpc_id       = "vpc-abcde012"
  
  node_groups = {
    eks_nodes = {
      desired_capacity = 3
      max_capacity     = 5
      min_capacity     = 1
    }
  }
}
