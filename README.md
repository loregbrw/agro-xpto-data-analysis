# Case Agro XPTO

## Agro XPTO – Data Pipeline Tutorial

This project builds a **data pipeline for Brazilian export data** using official datasets from the Ministry of Development, Industry and Foreign Trade (MDIC).

The pipeline automatically:

1. Downloads the raw datasets
2. Unifies export data
3. Cleans and normalizes the tables
4. Produces structured datasets ready for analysis

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-repository/agro-xpto-data-analysis.git
cd agro-xpto-data-analysis 
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the Data Pipeline

To execute the full data pipeline, run:

```bash
python src/setup.py
```

## Agro XPTO – Data sources
* **Data source:** https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta

### NCM Tables

* **NCM 2025:** https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2025.csv
* **NCM 2024:** https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2024.csv
* **NCM 2023:** https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2023.csv
* **NCM 2022:** https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2022.csv
* **NCM 2021:** https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2021.csv
* **NCM Base:** https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv

### Complementary Tables

* **Paises:** https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv
* **Blocos:** https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS_BLOCO.csv
* **Municipios:** https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv
* **Estados:** https://balanca.economia.gov.br/balanca/bd/tabelas/UF.csv
* **Via:** https://balanca.economia.gov.br/balanca/bd/tabelas/VIA.csv
* **URF:** https://balanca.economia.gov.br/balanca/bd/tabelas/URF.csv
