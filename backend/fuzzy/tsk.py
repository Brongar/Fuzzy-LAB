"""
fuzzy/tsk.py
============
Sistema de inferência fuzzy TSK (Takagi-Sugeno-Kang).
 
Diferença chave em relação ao Mamdani:
  - Consequentes são FUNÇÕES (lineares ou constantes), não conjuntos fuzzy
  - Não há etapa de defuzzificação — a saída é calculada como média ponderada
 
Tipos de consequente:
  - Ordem zero: y_k = c   (constante)
  - Ordem um:   y_k = a₀ + a₁·x₁ + a₂·x₂ + ...
"""