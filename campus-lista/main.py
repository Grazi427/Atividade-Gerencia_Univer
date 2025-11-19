from crud import adicionar_campus
from crud import excluir_campus
from crud import editar_campus
from crud import visualizar_campus
from crud import adicionar_curso
from crud import editar_curso
from crud import excluir_curso
from campus import campus_list
from _init_ import Campus,Curso

def exibir_menu():
    # Exibe o menu de opções
    print("\n" + "="*40)
    print("Sistema de Gestão Universitária da UFC")
    print("="*40)
    print("\n--- Gerenciamento de Campus ---")
    print("1. Adicionar Campus")
    print("2. Visualizar campus")
    print("3. Editar Campus (Endereço)")
    print("4. Excluir Campus")
    print("\n--- Gerenciamento de Cursos ---")
    print("5. Adicionar Curso")
    print("6. Editar Curso (Nome/Duração)")
    print("7. Excluir Curso")
    print("0. Sair")
    print("="*40)

def main():
    # Função principal que executa o menu
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            adicionar_campus()
        elif escolha == '2':
            visualizar_campus()
        elif escolha == '3':
            editar_campus()
        elif escolha == '4':
            excluir_campus()
        elif escolha == '5':
            adicionar_curso()
        elif escolha == '6':
            editar_curso()
        elif escolha == '7':
            excluir_curso()
        elif escolha == '0':
            print("Obrigado por usar o sistema! Encerrando...")
            return exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")
        main()



#  Inicialização com dados de exemplo (opcional)
print("\n" + "="*80)
exemplo=input('Deseja inicializar o sistema com campus e cursos de exemplo já cadastrados? (s/n) \n').lower


if exemplo=='s'.lower:
    print('Exemplos adicionados com sucesso! Os seguintes exemplos foram adicionados:\n',"-"*70,'\n' \
    '- Campus do Pici - Fortaleza, Av. da Universidade, sn\n'
    '- Cursos: Direito e Medicina' \
    '','\n',"-"*70,\
    '\n- Campus do Benfica - Fortaleza, Av. da Universidade, sn' \
    '\n- Cursos: Engenharia de Software e Ciência de Dados\n')
    campus_1 = Campus("Campus do Pici - Fortaleza", "Av. da Universidade, sn")
    campus_2 = Campus("Campus do Benfica - Fortaleza", "Av. da Universidade, sn")

    campus_1.adicionar_curso(Curso("Direito", 10))
    campus_1.adicionar_curso(Curso("Medicina", 12))
    campus_2.adicionar_curso(Curso("Engenharia de Software", 8))
    campus_2.adicionar_curso(Curso("Ciência de Dados", 6))

    campus_list.append(campus_1)
    campus_list.append(campus_2)


elif exemplo=='n'.lower:
    print('\nOk! o sistema iniciará sem nenhum campus ou curso cadastrado\n')

main()
