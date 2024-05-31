import json

# Função para gerar o template CloudFormation
def gerar_template_cloudformation(nome_vpc, cidr_vpc):
    template = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": f"Template para criar a VPC {nome_vpc}",
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
    return json.dumps(template, indent=4)

# Solicitar informações ao usuário
nome_vpc = input("Digite o nome da VPC: ")
cidr_vpc = input("Digite o CIDR da VPC (exemplo: 10.0.0.0/16): ")

# Gerar o template CloudFormation
template = gerar_template_cloudformation(nome_vpc, cidr_vpc)

# Exibir o template gerado
print("\nTemplate CloudFormation gerado:\n")
print(template)

# Opcional: salvar o template em um arquivo
with open(f"{nome_vpc}_cloudformation_template.json", "w") as file:
    file.write(template)

print(f"\nTemplate salvo em {nome_vpc}_cloudformation_template.json")
