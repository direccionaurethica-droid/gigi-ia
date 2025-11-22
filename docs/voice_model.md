```md
# Voice Model — Gigi IA

Tono = vector emocional en 5 ejes, rango 0–1.

Pipeline:
1. Inputs: texto libre + elecciones del test
2. Normalización Likert → vector
3. Modelo baseline: regresión sobre embeddings (OpenAI)
4. Modelo futuro: LLM fine-tuned
5. Runtime: el vector alimenta el estilo de respuesta
