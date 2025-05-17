# 💅 Projeto: API para Agendamento de Manicure — Daniela's Nails
## 🧾 Cenário do Cliente
Você foi contratado por Daniela, dona do salão Daniela's Nails, um espaço de estética especializado em manicure, pedicure e unhas em gel. Ela está expandindo o negócio e deseja modernizar o atendimento com um sistema de agendamentos 100% digital. Ela ainda não tem site nem app, mas contratou uma equipe futura que cuidará disso. Por enquanto, ela só quer a API pronta e bem documentada.

## 🎯 Objetivo da API

Desenvolver uma API para gerenciar:

- Clientes
- Profissionais
- Serviços
- Agendamentos

Com regras específicas como horários disponíveis, conflitos de agenda.

---

## 🛠️ Tecnologias Utilizadas

- Django 4+
- Django REST Framework
- SQLite

---

## 🚀 Como Rodar o Projeto

```bash
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/api-danielas-nails.git](https://github.com/Pedro-Leocir-Angelin-Zwirtes/api-manicure-django.git)
cd api-danielas-nails

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Realize as migrações
python manage.py migrate

# 6. Rode o servidor
python manage.py runserver
```
## 🗂️ Recursos da API

### 1. Clientes
  - Cadastro (nome, telefone, e-mail, data de nascimento)
  - CRUD completo
  - Consulta por nome ou telefone

### 2. Profissionais
  - Nome, especialidades (Ex: manicure, unhas em gel), dias e horários de trabalho
  - Ex: Daniela trabalha de segunda a sexta, das 13h às 20h
  - Cada profissional pode oferecer vários serviços

### 3. Serviços
  - Nome (Ex: Manicure simples, Unhas em Gel, Spa dos Pés)
  - Duração estimada em minutos (Ex: 30, 60, 90 min)
  - Preço

### 4. Agendamentos
  - Cliente, Profissional, Serviço, Data e Horário
  - Não pode haver dois agendamentos no mesmo horário para o mesmo profissional
  - Apenas horários dentro da agenda do profissional
  - CRUD completo

  Obs: (Como a API foi desenvolvida somente com back-end tratamentos como na etapa de agendamento listar todos os serviços ao invés de somente os serviços do profissional não foram resolvidos. Recomendações da documentação Django )

  ## Endpoints da API

- **/api/clientes/** : Crud Clientes
- **/api/servicos/** : Crud Servicos
- **/api/profissionais/** : Crud Profissionais
- **/api/agendamentos/** : Crud Agendamentos

## Autor

Pedro Leocir Angelin Zwirtes  
📧 Contato: pedroangelinzwirtes@gmail.com
