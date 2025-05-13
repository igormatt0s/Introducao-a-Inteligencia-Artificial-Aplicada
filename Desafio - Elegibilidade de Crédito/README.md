# Desafio de Classificação de Elegibilidade de Crédito

## 📌 Introdução

Este projeto é parte de um desafio para criar um modelo de **classificação de clientes** quanto à sua **elegibilidade para crédito**. A proposta envolve o uso de variáveis financeiras de um cliente para prever se ele é:

- Não elegível
- Requer análise
- Elegível

A solução foi desenvolvida utilizando um **modelo KNN (K-Nearest Neighbors)**, que classifica novas amostras com base na proximidade a clientes anteriores com características semelhantes.

O pipeline envolve:
- Pré-processamento de dados (tratamento de string em score, normalização)
- Treinamento com divisão treino/validação
- Armazenamento do modelo e scaler
- Exemplo de uso com entrada real

---

## 📁 Estrutura de Diretórios

```
├── modelo_classificacao.joblib # Dump do modelo KNN treinado
├── scaler.joblib # Dump do StandardScaler usado na normalização
├── README.md # Documentação
```

---

## 🔍 Modelo Utilizado

- **Tipo**: KNN (K-Nearest Neighbors)
- **K (n_neighbors)**: 3

---

## 📊 Variáveis Utilizadas

A entrada do modelo é composta por **4 variáveis**, na seguinte ordem:

```text
[salário anual, total de dívidas, histórico de pagamento (score), crédito solicitado]
```

> **Observação**: A variável idade está presente no conjunto original, mas não foi utilizada no modelo.