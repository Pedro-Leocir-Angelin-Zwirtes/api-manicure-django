💅 Projeto: API para Agendamento de Manicure — Daniela's Nails
🧾 Cenário do Cliente
Você foi contratado por Daniela, dona do salão Daniela's Nails, um espaço de estética especializado em manicure, pedicure e unhas em gel. Ela está expandindo o negócio e deseja modernizar o atendimento com um sistema de agendamentos 100% digital. Ela ainda não tem site nem app, mas contratou uma equipe futura que cuidará disso. Por enquanto, ela só quer a API pronta e bem documentada.

# 💅 API para Agendamento de Manicure — Daniela's Nails

Esta é uma API RESTful desenvolvida para modernizar o sistema de agendamentos do salão **Daniela's Nails**, especializado em manicure, pedicure e unhas em gel.

## 🧾 Cenário do Cliente

Daniela está expandindo seu salão e deseja automatizar os agendamentos com uma API robusta. A interface (site ou app) será feita no futuro por outra equipe. Seu pedido é uma API funcional, segura e bem documentada.

## 🎯 Objetivo da API

Desenvolver uma API para gerenciar:

- Clientes
- Profissionais
- Serviços
- Agendamentos
- Autenticação

Com regras específicas como horários disponíveis, conflitos de agenda e controle de acesso via token.

## ✅ Checklist de Implementação

### 🧍 Clientes

- [x]  Modelo: nome, telefone, e-mail, data de nascimento
- [x]  CRUD completo
- [x]  Busca por nome ou telefone

### 🧑‍🎨 Profissionais

- [x]  Modelo: nome, especialidades, dias e horários de trabalho
- [x]  Associação com serviços oferecidos
- [x]  CRUD completo

### 💅 Serviços

- [x]  Modelo: nome, duração (min), preço
- [x]  CRUD completo

### 📆 Agendamentos

- [x]  Modelo: cliente, profissional, serviço, data, horário
- [x]  Verificação de conflito de horários
- [x]  Respeitar agenda do profissional
- [x]  CRUD completo
- [x]  Cancelar e remarcar

---

## 🛠️ Tecnologias Utilizadas

- Django 4+
- Django REST Framework
- SQLite (ou PostgreSQL)
- SimpleJWT (para autenticação)

---

## 🚀 Como Rodar o Projeto

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/api-danielas-nails.git
cd api-danielas-nails

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Realize as migrações
python manage.py migrate

# 5. Crie um superusuário
python manage.py createsuperuser

# 6. Rode o servidor
python manage.py runserver
```


🎯 Objetivo da API
Criar uma API RESTful para o sistema de agendamento do salão Daniela's Nails, com controle de profissionais, serviços, horários disponíveis, clientes e agendamentos.

🗂️ Recursos da API

1. Clientes - OK
   Cadastro (nome, telefone, e-mail, data de nascimento)

CRUD completo

Consulta por nome ou telefone

2. Profissionais - OK
   Nome, especialidades (Ex: manicure, unhas em gel), dias e horários de trabalho

Ex: Daniela trabalha de segunda a sexta, das 13h às 20h

Cada profissional pode oferecer vários serviços

3. Serviços - OK
   Nome (Ex: Manicure simples, Unhas em Gel, Spa dos Pés)

Duração estimada em minutos (Ex: 30, 60, 90 min)

Preço

4. Agendamentos
   Cliente, Profissional, Serviço, Data e Horário

Não pode haver dois agendamentos no mesmo horário para o mesmo profissional

Apenas horários dentro da agenda do profissional

CRUD completo

Possibilidade de cancelar ou remarcar

5. Autenticação
   Autenticação por token (Django Token Auth ou JWT)

Somente usuários autenticados podem criar, editar ou cancelar agendamentos

✨ Funcionalidades Extras (se quiser avançar)
Disponibilidade automática: endpoint que retorna horários livres de um profissional em uma data

Histórico de agendamentos de um cliente

Painel/admin de relatórios: número de atendimentos por serviço ou profissional

Webhooks para integração futura com sistemas de pagamento ou WhatsApp

📂 Organização Sugerida
Você pode estruturar como:

bash
Copiar
Editar
/clientes/
/profissionais/
/servicos/
/agendamentos/
/disponibilidade/
🛠️ Tecnologias sugeridas
Django 4+

Django REST Framework

Autenticação via JWT (com djangorestframework-simplejwt)

SQLite (ou PostgreSQL, se quiser treinar)

[opcional] Django Admin customizado

📄 Documentação
Inclua no README do GitHub:

Explicação dos endpoints

Como rodar localmente

Como gerar tokens de autenticação

Como testar os agendamentos (ex: com curl ou Postman)

Se quiser, posso te enviar uma lista com os endpoints esperados em detalhes, ou você pode primeiro tentar montar os modelos e me mandar pra revisar. Posso agir como cliente e pedir alterações também, caso queira deixar mais desafiador. 😄

Você topa começar por esse desafio? Se sim, posso criar o primeiro "briefing oficial do cliente" com mais detalhes.
