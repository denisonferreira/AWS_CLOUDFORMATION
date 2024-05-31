import json

# Função para gerar o template CloudFormation em JSON
def gerar_template_cloudformation(nome_vpc, cidr_vpc, subnets):
    template = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": f"Template para criar a VPC {nome_vpc} com subnets",
        "Resources": {
            "MyVPC": {
                "Type": "AWS::EC2::VPC",
                "Properties": {
                    "CidrBlock": cidr_vpc,
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": nome_vpc
                        }
                    ]
                }
            }
        }
    }

    for i, subnet in enumerate(subnets, 1):
        subnet_resource = {
            f"Subnet{i}": {
                "Type": "AWS::EC2::Subnet",
                "Properties": {
                    "VpcId": {"Ref": "MyVPC"},
                    "CidrBlock": subnet['cidr'],
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": subnet['name']
                        }
                    ]
                }
            }
        }
        template['Resources'].update(subnet_resource)

    return json.dumps(template, indent=4)

# Solicitar informações ao usuário
nome_vpc = input("Digite o nome da VPC: ")
cidr_vpc = input("Digite o CIDR da VPC (exemplo: 10.0.0.0/16): ")
num_subnets = int(input("Quantas subnets deseja criar? "))

subnets = []
for i in range(num_subnets):
    subnet_name = input(f"Digite o nome da subnet {i+1}: ")
    subnet_cidr = input(f"Digite o CIDR da subnet {i+1} (exemplo: 10.0.1.0/24): ")
    subnets.append({"name": subnet_name, "cidr": subnet_cidr})

# Gerar o template CloudFormation em JSON
template = gerar_template_cloudformation(nome_vpc, cidr_vpc, subnets)

# Exibir o template gerado
print("\nTemplate CloudFormation gerado:\n")
print(template)

# Opcional: salvar o template em um arquivo
with open(f"{nome_vpc}_cloudformation_template.json", "w") as file:
    file.write(template)

print(f"\nTemplate salvo em {nome_vpc}_cloudformation_template.json")
