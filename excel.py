#Cláudia Jacy Barenco Abbas
#21.10.2026

import pandas as pd 
import os

df = pd.read_excel("dados_alunos_1000.xlsx")
colunas_notas = ['disciplina1', 'disciplina2', 'disciplina3', 'IRA']
for col in colunas_notas:
    df[col] = pd.to_numeric(df[col], errors='coerce')
dicionario = df.set_index('nome').to_dict(orient='index')
os.system("pause")

print("\n--- Cadastro de Alunos ---")
print(dicionario)

#Procura aluno pelo nome 
nome_procurado = input("Digite o nome do(a) aluno(a) a ser procurado: ").strip()
aluno = dicionario.get(nome_procurado)
if aluno:
    print(f"\n--- Aluno Encontrado: {nome_procurado} ---")
    print(f"Matrícula:   {aluno['matricula']}")
    print(f"Disciplina1: {aluno['disciplina1']}")
    print(f"Disciplina2: {aluno['disciplina2']}")
    print(f"Disciplina3: {aluno['disciplina3']}")
    print(f"IRA:         {aluno['IRA']}")
else:
    print(f"\nO(A) aluno(a) '{nome_procurado}' não foi encontrado(a) no cadastro.")

#Adiciona novo aluno 
novo_nome = "Claudia Abbas"
nova_matricula = 20241001
d1 = 8.5
d2 = 9.0
d3 = 7.5
novo_ira = round((d1 + d2 + d3)/3,2)
dicionario[novo_nome] = {
    'matricula': nova_matricula,
    'disciplina1': d1,
    'disciplina2': d2,
    'disciplina3': d3,
    'IRA': novo_ira
}

#Apaga aluno existente
nome_para_apagar = input("\nDigite o nome do(a) aluno(a) a ser apagado(a): ").strip()
if nome_para_apagar in dicionario:
    del dicionario[nome_para_apagar]
    print(f"\nO(A) aluno(a) '{nome_para_apagar}' foi apagado(a) do cadastro.")
else:
    print(f"\nO(A) aluno(a) '{nome_para_apagar}' não foi encontrado(a) no cadastro.")

#Lista alunos cadastrados
print("\n--- Lista de Alunos Cadastrados ---")
for nome, info in dicionario.items():
    print(f"Nome: {nome}")
    print(f"Matrícula: {info['matricula']}")
    print(f"Disciplina1: {info['disciplina1']}")
    print(f"Disciplina2: {info['disciplina2']}")
    print(f"Disciplina3: {info['disciplina3']}")
    print(f"IRA: {info['IRA']}")

#Salva o dicionário atualizado no mesmo arquivo Excel
df_atualizado = pd.DataFrame.from_dict(dicionario, orient='index').reset_index().rename(columns={'index': 'nome'})
for col in ['disciplina1', 'disciplina2', 'disciplina3', 'IRA']:
    if col in df_atualizado.columns:
        df_atualizado[col] = df_atualizado[col].astype(float)
df_atualizado.to_excel("Alunos_Cadastro_Teste_1000.xlsx", index=False)  