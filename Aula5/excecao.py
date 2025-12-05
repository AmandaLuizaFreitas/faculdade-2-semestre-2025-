# Tratamento de Exceções e Aplicações com Arquivos

try:
 n1 = int(input("Digite um número: ")) 
 n2 = int(input("Digite outro número: "))
 resultado = n1 / n2 
 print(f"O resultado da divisão é:{resultado}")
except ZeroDivisionError:
 print("Erro: Divisão por zero não é permitida.")
except ValueError:
 print("Erro: Entrada inválida. Por favor, digite números inteiros.")
except Exception as erro:
 print(f"Ocorreu um erro inesperado: {erro}")
else:
 print("Divisão realizada com sucesso.")
finally:
 print("Fim do programa.")