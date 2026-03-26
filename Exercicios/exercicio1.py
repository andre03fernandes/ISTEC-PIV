"""
Exercicio 1 - Programação IV ISTEC
Estruturas de Dados Compostas

Este programa demonstra como trabalhar com estruturas de dados compostas em Python:
- Lista de Listas (Matrizes)
- Dicionário de Listas
- Lista de Dicionários
"""

print("=" * 50)
print("ESTRUTURAS DE DADOS COMPOSTAS")
print("=" * 50)

# ========== 1. LISTA DE LISTAS (MATRIZ) ==========
print("\n1. LISTA DE LISTAS (Matriz 3x3):")
print("-" * 50)

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matriz: {lista_de_listas}")

# Exemplos de acesso
print(f"Primeiro elemento [0][0]: {lista_de_listas[0][0]}")
print(f"Elemento [1][2]: {lista_de_listas[1][2]}")
print(f"Última linha: {lista_de_listas[-1]}")

# Iteração pela matriz
print("\nTodos os elementos:")
for linha in lista_de_listas:
    print(f"  {linha}")

# ========== 2. DICIONÁRIO DE LISTAS ==========
print("\n2. DICIONÁRIO DE LISTAS:")
print("-" * 50)

dict_de_listas = {
    "frutas": ["Maçã", "Banana", "Laranja"],
    "legumes": ["Cenoura", "Brócolos", "Alface"]
}
print(f"Dicionário: {dict_de_listas}")

# Exemplos de acesso
print(f"\nFrutas: {dict_de_listas['frutas']}")
print(f"Primeira fruta: {dict_de_listas['frutas'][0]}")
print(f"Última legume: {dict_de_listas['legumes'][-1]}")

# Iteração
print("\nCategorias:")
for categoria, items in dict_de_listas.items():
    print(f"  {categoria.upper()}: {items}")

# ========== 3. LISTA DE DICIONÁRIOS ==========
print("\n3. LISTA DE DICIONÁRIOS (Alunos):")
print("-" * 50)

lista_de_dicts = [
    {"nome": "André", "nota": 18, "turma": "A"},
    {"nome": "Miguel", "nota": 20, "turma": "B"},
    {"nome": "Sofia", "nota": 19, "turma": "A"}
]

# Exemplos de acesso
print(f"Primeiro aluno: {lista_de_dicts[0]}")
print(f"Nome do segundo aluno: {lista_de_dicts[1]['nome']}")
print(f"Nota do primeiro aluno: {lista_de_dicts[0]['nota']}")

# Iteração e processamento
print("\nLista de Alunos:")
for aluno in lista_de_dicts:
    status = "Aprovado" if aluno['nota'] >= 10 else "Reprovado"
    print(f"  {aluno['nome']} - Nota: {aluno['nota']} ({status}) - Turma: {aluno['turma']}")

# Cálculo da média
media = sum(aluno['nota'] for aluno in lista_de_dicts) / len(lista_de_dicts)
print(f"\nMédia da turma: {media:.1f}")

print("\n" + "=" * 50)
print("Estruturas criadas e demonstradas com sucesso!")
print("=" * 50)
