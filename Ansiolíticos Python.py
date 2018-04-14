
# coding: utf-8

# In[32]:


rivotril = {"Nome Comercial": "rivotril",
            "Composto Principal": "diazepam",
            "Formula Quimica": "C14H10BrN3O"[::1],
            "Meia vida de Eliminacao em Horas": 36.5,
            "Número de Comprimidos por Embalagem": 30, 
            "Preco da Embalagem em Tres Fornecedores":  [13.53, 20.19, 12.94],
            "Quantidade do Composto Principal por Comprimido": 2,
            "Dose Diaria em mg Para um Adulto": 20,
            "As 3 Reacoes Adversas Mais Comuns": ["sonolência", "cefaleia", "infecção de vias aéreas superiores"]}


valium = {"Nome Comercial": "valium",
          "Composto Principal": "diazepam",
          "Formula Quimica": "C16H13ClN2O"[::1],
          "Meia vida de Eliminacao em Horas": 35,
          "Número de Comprimidos por Embalagem": 20, 
          "Preco da Embalagem em Tres Fornecedores":  [6.57, 6.51, 11.36],
          "Quantidade do Composto Principal por Comprimido": 5,
          "Dose Diaria Em mg Para um Adulto": 5,
          "As 3 Reacoes Adversas Mais Comuns": ["ataxia", "disartria", "fala enrolada"]}


frontal = {"Nome Comercial": "frontal",
          "Composto Principal": "alprazolam",
          "Formula Quimica": "C17H13ClN4"[::1],
          "Meia vida de Eliminacao em Horas": 11.2,
          "Número de Comprimidos por Embalagem": 30, 
          "Preco da Embalagem em Tres Fornecedores":  [46.44, 18.93, 27.03],
          "Quantidade do Composto Principal por Comprimido": 0.5,
          "Dose Diaria Em mg Para um Adulto": 1.5,
          "As 3 Reacoes Adversas Mais Comuns": ["depressão", "sedação", "sonolência"]}


ansitec = {"Nome Comercial": "ansitec",
          "Composto Principal": "buspirona",
          "Formula Quimica": "C21H31N5O2"[::1],
          "Meia vida de Eliminacao em Horas": 11,
          "Número de Comprimidos por Embalagem": 20, 
          "Preco da Embalagem em Tres Fornecedores":  [26.22, 20.31, 19.18],
          "Quantidade do Composto Principal por Comprimido": 5,
          "Dose Diaria Em mg Para um Adulto": 15,
          "As 3 Reacoes Adversas Mais Comuns": ["tontura", "cefaleia", "sonolência"]} 


lorax = {"Nome Comercial": "lorax",
          "Composto Principal": "lorazepam",
          "Formula Quimica": "C15H10Cl2N2O2"[::1],
          "Meia vida de Eliminacao em Horas": 16,
          "Número de Comprimidos por Embalagem": 30, 
          "Preco da Embalagem em Tres Fornecedores":  [34.99, 19.20, 20.87],
          "Quantidade do Composto Principal por Comprimido": 2,
          "Dose Diaria Em mg Para um Adulto": 2,
          "As 3 Reacoes AdversasMmais Comuns": ["sedação", "cansaço", "sonolência"]} 


olcadil = {"Nome Comercial": "olcadil",
          "Composto Principal": "cloxazolam",
          "Formula Quimica": "C17H14Cl2N2O2"[::1],
          "Meia vida de Eliminacao em Horas": 80,
          "Número de Comprimidos por Embalagem": 30, 
          "Preco da Embalagem em Tres Fornecedores":  [37.35, 22.59, 22.62],
          "Quantidade do Composto Principal por Comprimido": 1,
          "Dose Diaria Em mg Para um Adulto": 3,
          "As 3 Reacoes Adversas Mais Comuns": ["sonolência", "fadiga", "cefaleia"]} 


tranxilene = {"Nome Comercial": "tranxilene",
          "Composto Principal": "clorazepato dipotássico",
          "Formula Quimica": "C16H11ClK2N2O4"[::1],
          "Meia vida de Eliminacao em Horas": 20,
          "Número de Comprimidos por Embalagem": 20, 
          "Preco da Embalagem em Tres Fornecedores":  [11.18, 10.21, 11.13],
          "Quantidade do Composto Principal por Comprimido": 15,
          "Dose Diaria Em mg Para um Adulto": 30,
          "As 3 Reacoes Adversas Mais Comuns": ["sonolência", "diarréia", "vômitos"]}


somalium = {"Nome Comercial": "somalium",
          "Composto Principal": "bromazepam",
          "Formula Quimica": "C14H10BrN3O"[::1],
          "Meia vida de Eliminacao em Horas": 20,
          "Número de Comprimidos por Embalagem": 20, 
          "Preco da Embalagem em Tres Fornecedores":  [12.84, 15.41, 13.58],
          "Quantidade do Composto Principal por Comprimido": 10,
          "Dose Diaria Em mg Para um Adulto": 9,
          "As 3 Reacoes Adversas Mais Comuns": ["cansaço", "sonolência", "sedação"]} 


urbanil = {"Nome Comercial": "urbanil",
          "Composto Principal": "clobazam",
          "Formula Quimica": "C16H13ClN2O2"[::1],
          "Meia vida de Eliminacao em Horas": 20,
          "Número de Comprimidos por Embalagem": 30, 
          "Preco da Embalagem em Tres Fornecedores":  [22.62, 17.17, 18.57],
          "Quantidade do Composto Principal por Comprimido": 3,
          "Dose Diaria Em mg Para um Adulto": 3,
          "As 3 Reacoes Adversas Mais Comuns": ["sonolência", "tontura", "sedação"]} 


noctal = {"Nome Comercial": "noctal",
          "Composto Principal": "estazolam",
          "Formula Quimica": "C16H11ClN4"[::1],
          "Meia vida de Eliminacao em Horas": 17,
          "Número de Comprimidos por Embalagem": 20, 
          "Preco da Embalagem em Tres Fornecedores":  [19.90, 21.30, 18.73],
          "Quantidade do Composto Principal por Comprimido": 2,
          "Dose Diaria Em mg Para um Adulto": 2,
          "As 3 Reacoes Adversas Mais Comuns": ["cefaléia", "sonolência", "náusea"]} 

