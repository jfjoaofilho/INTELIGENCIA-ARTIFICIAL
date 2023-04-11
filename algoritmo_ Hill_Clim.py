import random

# Funcao que avalia o estado atual
def evaluate(state):
  # Avalia o estado atual
  value = 0

  # Adiciona ou subtrai valor de acordo com o estado
  for i in range(len(state)):
    if state[i] == 0:
      value -= 1
    else:
      value += 1
  return value

# Funcao que gera um estado vizinho
def generate_neighbor(state):
  # Gera um estado vizinho
  neighbor = state[:]
  i = random.randint(0, len(state)-1)

  # Alterna o valor do bit aleatorio
  if neighbor[i] == 0:
    neighbor[i] = 1
  else:
    neighbor[i] = 0
  return neighbor

# Funcao Hill Climbing
def hill_climbing(state):
  while True:
    # Avalia o estado atual
    current_value = evaluate(state)

    # Gera o estado vizinho
    neighbor = generate_neighbor(state)

    # Avalia o estado vizinho
    neighbor_value = evaluate(neighbor)

    # Verifica se o estado vizinho é melhor
    if neighbor_value > current_value:
      state = neighbor
    else:
      break
  return state

# Objeto teste
state = [0, 0, 0, 0, 0, 0, 0, 0]

# Executa o Hill Climbing
best_state = hill_climbing(state)

# Mostra o resultado
print("Estado Final:", best_state)
