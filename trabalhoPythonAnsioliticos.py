
# coding: utf-8

# In[2]:


#Medicamentos Selecionados: ANSIOLÍTICOS


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#Pesquisa sobre os medicamentos e inclusão em dicionários

rivotril = {"Nome Comercial": "rivotril",
            "Composto Principal": "diazepam",
            "Formula Quimica": "C14H10BrN3O"[::1],
            "Meia vida de Eliminacao em Horas": 36.5,
            "Número de Comprimidos por Embalagem": 30, 
            "Preco da Embalagem em Tres Fornecedores":  [13.53, 20.19, 12.94],
            "Quantidade do Composto Principal por Comprimido": 2,
            "Dose Diaria Em mg Para um Adulto": 20,
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
          "As 3 Reacoes Adversas Mais Comuns": ["sedação", "cansaço", "sonolência"]} 


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


# In[5]:


#Cálculo dos preço médio por comprimido dos medicamentos

#Rivotril
soma = 0
media = 0
for x in range(3):
    soma += rivotril["Preco da Embalagem em Tres Fornecedores"][x]
    mediaRivotril = soma/3
valor_comprimidoRivotril = mediaRivotril/rivotril["Número de Comprimidos por Embalagem"]

#Valium
soma = 0
media = 0
for x in range(3):
    soma += valium["Preco da Embalagem em Tres Fornecedores"][x]
    mediaValium = soma/3
valor_comprimidoValium = mediaValium/valium["Número de Comprimidos por Embalagem"]

#Frontal
soma = 0
media = 0
for x in range(3):
    soma += frontal["Preco da Embalagem em Tres Fornecedores"][x]
    mediaFrontal = soma/3
valor_comprimidoFrontal = mediaFrontal/frontal["Número de Comprimidos por Embalagem"]

#Ansitec
soma = 0
media = 0
for x in range(3):
    soma += ansitec["Preco da Embalagem em Tres Fornecedores"][x]
    mediaAnsitec = soma/3
valor_comprimidoAnsitec = mediaAnsitec/ansitec["Número de Comprimidos por Embalagem"]

#Lorax
soma = 0
media = 0
for x in range(3):
    soma += lorax["Preco da Embalagem em Tres Fornecedores"][x]
    mediaLorax = soma/3
valor_comprimidoLorax = mediaLorax/lorax["Número de Comprimidos por Embalagem"]

#Olcadil
soma = 0
media = 0
for x in range(3):
    soma += olcadil["Preco da Embalagem em Tres Fornecedores"][x]
    mediaOlcadil = soma/3
valor_comprimidoOlcadil = mediaOlcadil/olcadil["Número de Comprimidos por Embalagem"]

#Tranxilene
soma = 0
media = 0
for x in range(3):
    soma += tranxilene["Preco da Embalagem em Tres Fornecedores"][x]
    mediaTranxilene = soma/3
valor_comprimidoTranxilene = mediaTranxilene/tranxilene["Número de Comprimidos por Embalagem"]

#Somalium
soma = 0
media = 0
for x in range(3):
    soma += somalium["Preco da Embalagem em Tres Fornecedores"][x]
    mediaSomalium = soma/3
valor_comprimidoSomalium = mediaSomalium/somalium["Número de Comprimidos por Embalagem"]

#Urbanil
soma = 0
media = 0
for x in range(3):
    soma += urbanil["Preco da Embalagem em Tres Fornecedores"][x]
    mediaUrbanil = soma/3
valor_comprimidoUrbanil = mediaUrbanil/urbanil["Número de Comprimidos por Embalagem"]

#Noctal
soma = 0
media = 0
for x in range(3):
    soma += noctal["Preco da Embalagem em Tres Fornecedores"][x]
    mediaNoctal = soma/3
valor_comprimidoNoctal = mediaNoctal/noctal["Número de Comprimidos por Embalagem"]


# In[6]:


#Gráfico de preço médio por comprimido dos medicamentos

plt.figure(figsize=(12,5))
plt.title('Gráfico de Preço do Comprimido por Medicamento')
plt.xlabel('Medicamento')
plt.ylabel('Preço do Comprimido (R$)')

y = [valor_comprimidoRivotril, valor_comprimidoValium, valor_comprimidoFrontal, valor_comprimidoAnsitec, valor_comprimidoLorax, valor_comprimidoOlcadil, valor_comprimidoTranxilene, valor_comprimidoSomalium, valor_comprimidoUrbanil, valor_comprimidoNoctal]
N = len(y)
x = ["Rivotril","Valium","Frontal","Ansitec","Lorax","Olcadil","Tranxilene","Somalium","Urbanil","Noctal"]
width = 0.5
plt.bar(x, y, width, color="gold")


# In[7]:


#Cálculo do preço médio da mg do componente principal por medicamento

#Rivotril
media_mgRivotril = (mediaRivotril/(rivotril["Número de Comprimidos por Embalagem"]*rivotril["Quantidade do Composto Principal por Comprimido"]))

#Valium
media_mgValium = (mediaValium/(valium["Número de Comprimidos por Embalagem"]*valium["Quantidade do Composto Principal por Comprimido"]))

#Frontal
media_mgFrontal = (mediaFrontal/(frontal["Número de Comprimidos por Embalagem"]*frontal["Quantidade do Composto Principal por Comprimido"]))

#Ansitec
media_mgAnsitec = (mediaAnsitec/(ansitec["Número de Comprimidos por Embalagem"]*ansitec["Quantidade do Composto Principal por Comprimido"]))

#Lorax
media_mgLorax = (mediaLorax/(lorax["Número de Comprimidos por Embalagem"]*lorax["Quantidade do Composto Principal por Comprimido"]))

#Olcadil
media_mgOlcadil = (mediaOlcadil/(olcadil["Número de Comprimidos por Embalagem"]*olcadil["Quantidade do Composto Principal por Comprimido"]))

#Tranxilene
media_mgTranxilene = (mediaTranxilene/(tranxilene["Número de Comprimidos por Embalagem"]*tranxilene["Quantidade do Composto Principal por Comprimido"]))

#Somalium
media_mgSomalium = (mediaSomalium/(somalium["Número de Comprimidos por Embalagem"]*somalium["Quantidade do Composto Principal por Comprimido"]))

#Urbanil
media_mgUrbanil = (mediaUrbanil/(urbanil["Número de Comprimidos por Embalagem"]*urbanil["Quantidade do Composto Principal por Comprimido"]))

#Noctal
media_mgNoctal = (mediaNoctal/(noctal["Número de Comprimidos por Embalagem"]*noctal["Quantidade do Composto Principal por Comprimido"]))


# In[8]:


#Gráfico do preço médio da mg do componente principal por medicamento

plt.figure(figsize=(12,5))
plt.title('Gráfico de Preço Médio da mg do Componente Principal por Medicamento')
plt.xlabel('Medicamento')
plt.ylabel('Preço da mg do Componente Principal (R$)')

y = [media_mgRivotril, media_mgValium, media_mgFrontal, media_mgAnsitec, media_mgLorax, media_mgOlcadil, media_mgTranxilene, media_mgSomalium, media_mgUrbanil, media_mgNoctal]
N = len(y)
x = ["Rivotril","Valium","Frontal","Ansitec","Lorax","Olcadil","Tranxilene","Somalium","Urbanil","Noctal"]
width = 0.5
plt.bar(x, y, width, color="blue")


# In[9]:


#Gráfico de dose diária x meia vida de eliminação

plt.figure(figsize=(20,15))
plt.title("Gráfico Dose Diária x Meia Vida Eliminação")
plt.grid(True)

plt.subplot(5,5,1)
plt.title("Rivotril")
x = [1,rivotril["Meia vida de Eliminacao em Horas"]]
y = [1,rivotril["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,2)
plt.title("Valium")
x = [1,valium["Meia vida de Eliminacao em Horas"]]
y = [1,valium["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,3)
plt.title("Frontal")
x = [1,frontal["Meia vida de Eliminacao em Horas"]]
y = [1,frontal["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,4)
plt.title("Ansitec")
x = [1,ansitec["Meia vida de Eliminacao em Horas"]]
y = [1,ansitec["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,5)
plt.title("Lorax")
x = [1,lorax["Meia vida de Eliminacao em Horas"]]
y = [1,lorax["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,6)
plt.title("Olcadil")
x = [1,olcadil["Meia vida de Eliminacao em Horas"]]
y = [1,olcadil["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,7)
plt.title("Tranxilene")
x = [1,tranxilene["Meia vida de Eliminacao em Horas"]]
y = [1,tranxilene["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,8)
plt.title("Somalium")
x = [1,somalium["Meia vida de Eliminacao em Horas"]]
y = [1,somalium["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,9)
plt.title("Urbanil")
x = [1,urbanil["Meia vida de Eliminacao em Horas"]]
y = [1,urbanil["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)

plt.subplot(5,5,10)
plt.title("Noctal")
x = [1,noctal["Meia vida de Eliminacao em Horas"]]
y = [1,noctal["Dose Diaria Em mg Para um Adulto"]]
plt.plot(x,y)
plt.xlabel('Meia-vida de eliminação(h)')
plt.ylabel('Dose diária para um adulto(mg)')
plt.grid(True)


plt.tight_layout()


# In[10]:


#Cálculo de valor para um tratamento de 7 dias com os medicamentos

trat7DiasRivotril = (7*rivotril["Dose Diaria Em mg Para um Adulto"]*media_mgRivotril)
trat7DiasValium = (7*valium["Dose Diaria Em mg Para um Adulto"]*media_mgValium)
trat7DiasFrontal = (7*frontal["Dose Diaria Em mg Para um Adulto"]*media_mgFrontal)
trat7DiasAnsitec = (7*ansitec["Dose Diaria Em mg Para um Adulto"]*media_mgAnsitec)
trat7DiasLorax = (7*lorax["Dose Diaria Em mg Para um Adulto"]*media_mgLorax)
trat7DiasOlcadil = (7*olcadil["Dose Diaria Em mg Para um Adulto"]*media_mgOlcadil)
trat7DiasTranxilene = (7*tranxilene["Dose Diaria Em mg Para um Adulto"]*media_mgTranxilene)
trat7DiasSomalium = (7*somalium["Dose Diaria Em mg Para um Adulto"]*media_mgSomalium)
trat7DiasUrbanil = (7*urbanil["Dose Diaria Em mg Para um Adulto"]*media_mgUrbanil)
trat7DiasNoctal = (7*noctal["Dose Diaria Em mg Para um Adulto"]*media_mgNoctal)


# In[11]:


#Gráfico de valor para um tratamento de 7 dias com os medicamentos

plt.figure(figsize=(12,5))
plt.title('Gráfico de Valor para Tratamento de 7 Dias')
plt.xlabel('Medicamento')
plt.ylabel('Valor do tratamento (R$)')

y = [trat7DiasRivotril, trat7DiasValium, trat7DiasFrontal, trat7DiasAnsitec, trat7DiasLorax, trat7DiasOlcadil, trat7DiasTranxilene, trat7DiasSomalium, trat7DiasUrbanil, trat7DiasNoctal]
N = len(y)
x = ["Rivotril","Valium","Frontal","Ansitec","Lorax","Olcadil","Tranxilene","Somalium","Urbanil","Noctal"]
width = 0.5
plt.bar(x, y, width, color="red")


# In[19]:


#Resultado dos dados coletados para valor de tratamento
print("O medicamento com tratamento mais caro para um período de 7 dias é o Rivotril, como mostra o gráfico acima")


# In[23]:


ansitec["Dose Criança"] = (6/24)*ansitec["Dose Diaria Em mg Para um Adulto"]
frontal["Dose Criança"] = (6/24)*frontal["Dose Diaria Em mg Para um Adulto"]
lorax["Dose Criança"] = (6/24)*lorax["Dose Diaria Em mg Para um Adulto"]
noctal["Dose Criança"] = (6/24)*noctal["Dose Diaria Em mg Para um Adulto"]
olcadil["Dose Criança"] = (6/24)*olcadil["Dose Diaria Em mg Para um Adulto"]
rivotril["Dose Criança"] = (6/24)*rivotril["Dose Diaria Em mg Para um Adulto"]
somalium["Dose Criança"] = (6/24)*somalium["Dose Diaria Em mg Para um Adulto"]
tranxilene["Dose Criança"] = (6/24)*tranxilene["Dose Diaria Em mg Para um Adulto"]
urbanil["Dose Criança"] = (6/24)*urbanil["Dose Diaria Em mg Para um Adulto"]
valium["Dose Criança"] = (6/24)*valium["Dose Diaria Em mg Para um Adulto"]

