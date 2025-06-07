from models import user, seller


us = user.User()
ve = seller.Seller()

if __name__ == "__main__":
    while True:
        print("Seja bem-vindo(a), escolha uma opção abaixo")

        choice = input(
            "[1] Usuário\n"
            "[2] Vendedor\n"
            "[3] Produto\n"
            "[4] Compra\n"
            "[5] Sair\n"
        )

        match choice:
            case "1":
                while True:
                    choice = input(
                        "O que deseja fazer?\n"
                        "[1] Inserir\n"
                        "[2] Atualizar\n"
                        "[3] Voltar\n"
                    )

                    match choice:
                        case "1":
                            name = input("Digite o nome do usuário: ")
                            email = input("Digite o email do usuário: ")
                            cpf = input("Digite o CPF do usuário: ")
                            password = input("Digite a senha do usuário: ")

                            addresses = []

                            add_address = input(
                                "Deseja adicionar endereços? s/n: "
                            )
                            while add_address.lower() == "s":
                                street = input("Digite a rua: ")
                                neighborhood = input("Digite o bairro: ")
                                city = input("Digite a cidade: ")
                                state = input("Digite o estado: ")
                                cep = input("Digite o cep: ")
                                number = input("Digite o número: ")

                                addresses.append({
                                    "rua": street,
                                    "bairro": neighborhood,
                                    "cidade": city,
                                    "estado": state,
                                    "cep": cep,
                                    "numero": number
                                })

                                stop = input(
                                    "Deseja adicionar mais um endereço? s/n: "
                                )

                                if stop.lower() != "s":
                                    break

                            us.insert(
                                name,
                                email,
                                cpf,
                                addresses,
                                password
                            )
                        case "2":
                            user_id = input(
                                "Digite o ID do usuário que deseja atualizar: "
                            )

                            print(
                                "Deixe o campo vazio se não quiser atualizar."
                            )

                            name = input("Novo nome: ") or None
                            email = input("Novo email: ") or None
                            cpf = input("Novo CPF: ") or None
                            password = input("Nova senha: ") or None

                            addresses = []
                            change_address = input(
                                "Deseja atualizar os endereços? (s/n): "
                            )
                            if change_address.lower() == "s":
                                while True:
                                    street = input("Digite a rua: ")
                                    neighborhood = input("Digite o bairro: ")
                                    city = input("Digite a cidade: ")
                                    state = input("Digite o estado: ")
                                    cep = input("Digite o CEP: ")
                                    number = input("Digite o número: ")

                                    addresses.append({
                                        "rua": street,
                                        "bairro": neighborhood,
                                        "cidade": city,
                                        "estado": state,
                                        "cep": cep,
                                        "numero": number
                                    })

                                    stop = input(
                                        "Deseja adicionar mais um endereço? "
                                        "(s/n): "
                                    )
                                    if stop.lower() != "s":
                                        break
                            else:
                                addresses = None

                            us.update(
                                user_id,
                                name,
                                email,
                                cpf,
                                password,
                                addresses
                            )
                        case "3":
                            break
                        case _:
                            print("Selecione somente as opções listadas.")
            case "2":
                while True:
                    choice = input(
                        "O que deseja fazer?\n"
                        "[1] Inserir\n"
                        "[2] Voltar\n"
                    )

                    match choice:
                        case "1":
                            name = input("Digite o nome do vendedor: ")
                            email = input("Digite o email do vendedor: ")
                            cpf = input("Digite o CPF do vendedor: ")
                            cnpj = input("Digite o CNPJ do vendedor: ")
                            password = input("Digite a senha do vendedor: ")

                            addresses = []

                            add_address = input(
                                "Deseja adicionar endereços? s/n: "
                            )

                            while add_address.lower() == "s":
                                street = input("Digite a rua: ")
                                neighborhood = input("Digite o bairro: ")
                                city = input("Digite a cidade: ")
                                state = input("Digite o estado: ")
                                cep = input("Digite o cep: ")
                                number = input("Digite o número: ")

                                addresses.append({
                                    "rua": street,
                                    "bairro": neighborhood,
                                    "cidade": city,
                                    "estado": state,
                                    "cep": cep,
                                    "numero": number
                                })

                                stop = input(
                                    "Deseja adicionar mais um endereço? s/n: "
                                )

                                if stop.lower() != "s":
                                    break

                            ve.insert(
                                name,
                                email,
                                cpf,
                                cnpj,
                                password,
                                addresses
                            )
                        case "2":
                            break
                        case _:
                            print("Selecione somente as opções listadas.")
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Por favor, selecione apenas as opções listadas.")
