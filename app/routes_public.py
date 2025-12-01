#como ficaria a questão de representar o entregador também como o usuário? por que no código vai ter que repetir os atributos do usuário na parte do entregador

"""
routes_public.py
Rotas públicas acessíveis a qualquer visitante do site (não requerem autenticação).
Inclui: página inicial, login, escolha de tipo de cadastro e autenticação.
"""

from flask import Blueprint, request, render_template, redirect, url_for
from .dao.RestauranteDAO import RestauranteDAO
from .dao.UsuarioDAO import UsuarioDAO
from .dao.EntregadorDAO import EntregadorDAO

# Cria o blueprint para rotas públicas
# 'public' é o nome do blueprint
public_bp = Blueprint('public', __name__)

# Instancia os DAOs (Data Access Objects) para acesso ao banco de dados
restaurante_dao = RestauranteDAO()
usuario_dao = UsuarioDAO()
entregador_dao = EntregadorDAO()

# ==================== ROTA: FORMULÁRIO DE LOGIN ====================
@public_bp.route("/", methods=['GET'])
def login():
    """
    Rota para exibir o formulário de login.
    Usuário pode escolher entrar como:
    - Restaurante
    - Usuário
    - Entregador
    
    Returns:
        Renderiza o template 'login.html' com formulário de autenticação
    """
    return render_template('login.html')


# ==================== ROTA: PROCESSAR AUTENTICAÇÃO ====================
@public_bp.route("/autenticar", methods=['POST'])
def autenticar():
    """
    Rota para processar a autenticação (POST).
    Recebe credenciais do formulário e verifica no banco de dados.
    Redireciona para a área apropriada baseado no tipo de usuário.
    
    Fluxo:
    1. Recebe username, password e tipo (restaurante, usuario ou entregador) do formulário
    2. Busca no DAO correspondente
    3. Valida a senha
    4. Redireciona para a área correta ou retorna erro
    
    Returns:
        Redirect para área do restaurante/usuário/entregador ou volta ao login com mensagem de erro
    """
    # Captura os dados enviados pelo formulário
    username = request.form['username']
    password = request.form['password']
    tipo = request.form['tipo']  # 'restaurante', 'atendente', 'gerente' ou 'entregador'
    
    # Verifica qual tipo de login está sendo feito

    
    if tipo == 'entregador':
        # Busca entregador no banco de dados
        entregador = entregador_dao.buscar_por_username(username)
        
        # Verifica se o entregador existe e se a senha está correta
        if entregador and entregador.password == password:
            # Autenticação bem-sucedida - redireciona para área do entregador
            return redirect(url_for('entregador.pedidos_disponiveis', username=username))
        else:
            # Credenciais inválidas - volta ao login com mensagem de erro
            return render_template('login.html', 
                                 msg="Entregador ou senha inválidos",
                                 tipo=tipo)
    else:
        # Busca usuário no banco de dados
        usuario = usuario_dao.buscar_por_username(username)
        
        # Verifica se o usuário existe e se a senha está correta
        if usuario and usuario == password:
            # Autenticação bem-sucedida - redireciona para área do usuário
            # Passa o username como parâmetro na URL
            return redirect(url_for('usuario.area_usuario', username=username))
        else:
            # Credenciais inválidas - volta ao login com mensagem de erro
            return render_template('login.html', 
                                 msg="Usuário ou senha inválidos",
                                 tipo=tipo)


# ==================== ROTA: AGUARDANDO APROVAÇÃO ====================
@public_bp.route("/aguardando-aprovacao", methods=['GET'])
def aguardando_aprovacao():
    """
    Rota para exibir mensagem de aguardando aprovação.
    Acessada após cadastro de restaurante ou usuário.
    
    Returns:
        Renderiza o template 'aguardando_aprovacao.html' com mensagem informativa
    """
    return render_template('aguardando_aprovacao.html')


# ==================== ROTA: FORMULÁRIO DE CADASTRO DO ENTREGADOR ====================
@public_bp.route("/cadastro-entregador", methods=['GET'])
def cadastro_entregador():
    """
    Rota para exibir o formulário de cadastro de entregador.
    
    Formulário deve incluir campos como:
    - Nome completo
    - CPF
    - Email
    - Telefone
    - Username (para login)
    - Password (para login)
    - VEÍCULO (dropdown: carro, moto, bicicleta) - OBRIGATÓRIO
    - Placa do veículo
    - CNH (Carteira Nacional de Habilitação)
    
    IMPORTANTE: O status inicial do entregador será 'inativo' ou 'aguardando_aprovacao'
    após o cadastro. Ele precisará ser ativado depois.
    
    Returns:
        Renderiza o template 'form_cadastro_entregador.html'
    """
    return render_template('form_cadastro_entregador.html')


# ==================== ROTA: PROCESSAR CADASTRO DO ENTREGADOR ====================
@public_bp.route("/cadastrar-entregador", methods=['POST'])
def cadastrar_entregador():
    """
    Rota para processar o cadastro do entregador (POST).
    
    Fluxo:
    1. Recebe todos os dados do formulário
    2. Cria um objeto Entregador
    3. Define status inicial como 'inativo' (entregador precisa ativar manualmente depois)
    4. Insere no banco de dados através do DAO
    5. Redireciona para página de "aguardando aprovação"
    
    Campos importantes:
    - veiculo: tipo de veículo usado (carro, moto, bicicleta)
    - status: sempre inicia como 'inativo' - entregador ativa quando quiser trabalhar
    
    Returns:
        Redirect para a rota 'public.aguardando_aprovacao'
    """
    from models.Entregador import Entregador
    
    # Captura todos os dados enviados pelo formulário
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    telefone = request.form['telefone']
    username = request.form['username']
    password = request.form['password']
    
    
    # Cria o objeto Entregador com os dados recebidos
    # Status inicial sempre é 'inativo' - entregador ativa quando quiser trabalhar
    entregador = Entregador(
        nome=nome,
        cpf=cpf,
        email=email,
        telefone=telefone,
        username=username,
        password=password,
        status='inativo'  # Status inicial - entregador não está disponível ainda
    )
    
    # Insere o entregador no banco de dados
    entregador_dao.inserir(entregador)
    
    # Redireciona para a página de aguardando aprovação
    return redirect(url_for('public.aguardando_aprovacao'))