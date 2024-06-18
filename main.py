#imports
import random #biblioteca para gerar numeros randomicos

#defs
size=20 #numero de casas no tabuleiro
max_rounds=1000 #maximo de rounds

#==========================Novo paradigma classes

class strategy:
    def __init__(self, name: str) -> bool: #se a estrategia retorna se compra ou nao fiz que retorna booleana...
        self.name=name 
    
    def buy_decision(self):
        ...

class player:
    def __init__(self, strategy: strategy, balance: float, lap: int, position: int ) -> None:
        self.balance = balance
        self.lap = lap
        self.position = position
        self.strategy = strategy

    # def __repr__(self) -> str:
    #     return self.strategy

    @staticmethod
    def generate_players():
        p1 = player("Impulsive", 300, 0, 0)
        p2 = player("Demanding", 300, 0, 0)
        p3 = player("Cautious", 300, 0, 0)
        p4 = player("Random", 300, 0, 0) 
        return [p1,p2,p3,p4]
    
class PlayerQueue: #corrigir nomes das classes para CamelCase
    #este é um constructor que é um metodo de instancia
    def __init__(self) -> queue: #como retornar o valor da função interna?
        self.player_list=player.generate_players() #aqui coloco dentro de uma variavel da classe PlayerQueue o setup padrão dos players
        self.queue=self._generate_queue()
        #self._generate_queue() #nao sei oq era isso

    #metodo de instancia, médoto de classe e metodo estatico
    #aqui precisa dizer que é um metodo estatico pois nao usa nenhum argumento, 
    #e quando nao deixa isso explicito o compilador entende que é um metodo de classe, que no minimo precisa do argumento 'cls'
   
    @staticmethod
    #gera set de 4 numeros randomicos numa ordem desconhecida, mas como tem uma ordem interna será usado para organizar os players
    def _generate_order_set() -> set:
        order_set=set()
        while len(order_set) < 4:
            order_set.add(random.randrange(1,100,1))
        return list(order_set)
 
    def _generate_queue(self):
        order=self._generate_order_set() #set de ordenação instanciado
        lista_ordenada=[]
        queue=[]

        i = 0
        for player in self.player_list:
            dict = {"prioridade": order[i], "player": player}
            lista_ordenada.append(dict) #cria a lista com os pesos de prioridade
            i += 1
        
        def key(e):
            return e["prioridade"]

        lista_ordenada.sort(key=key) #ordena a lista com base nos pesos das prioridades

        for i in lista_ordenada:
            queue.append(i["player"]) #tira da fila a informação da prioridade
        
        self.queue=queue

class property:
    def __init__(self, position: int, value: float , rent: float, owner: player | None) -> None:
        self.position = position
        self.value = value
        self.rent = rent
        self.owner = owner

queue=player_queue() 
print(queue.queue)
#==========================/Novo paradigma classes

# #funções do jogo
# def round(player_order:list[dict[str,str|int]],board): 
#     #cada round é constituido de 3 fases para cada player
#     for player in player_order:

#         #1 - parte que joga o dado e move o jogador pra casa 
#         dice_roll=random.randrange(1,7,1) #tem que ser 7 pq nao inclui o valor de limite, desta forma gera os valores de 1 à 6
#         #random.randint() poderia usar esta para incluir o valor limite tambem
#         if player['Posicao']+dice_roll>(casas-1): #precisa da condição casas-1 pq são 20 casas mas a ultima casa é a 19
#            player['Posicao']+=(dice_roll-casas)
#            player['Volta']+=1
#            player['Saldo']+=100
#         else:
#            player['Posicao']+=dice_roll 
        
#         #2 - parte que checa ação do player na casa de chegada
#         #landing_site=board[player['Posicao']] ## proposta do eiti
#         landing_site_owner=board[player['Posicao']]['Dono']
#         landing_site_rent=board[player['Posicao']]['Aluguel']
#         landing_site_value=board[player['Posicao']]['Preco']

#         if landing_site_owner == 'banco': #se esta numa casa sem dono
#             if player['Estrategia']=='Impulsive':
#                 if player['Saldo']>=landing_site_value: #impulsivo compra sempre que tem dinheiro
#                     #landing_site_owner=player['Estrategia'] #aqui tentei usar a var landing_site_owner, mas daí nao atualizava a lista da board, achei que tratia o p1,p2,p3,p4
#                     #landing_site['Dono']=player['Estrategia']  ## proposta do eiti
#                     board[player['Posicao']]['Dono']=player['Estrategia'] 
#                     player['Saldo']-=landing_site_value
#             elif player['Estrategia']=='Demanding':     
#                 if (player['Saldo']>=landing_site_value) and (landing_site_rent>50): #demanding compra sempre que aluguel >50 e tenha saldo
#                     #landing_site_owner=player['Estrategia'] #aqui tentei usar a var landing_site_owner, mas daí nao atualizava a lista da board, achei que tratia o p1,p2,p3,p4
#                     board[player['Posicao']]['Dono']=player['Estrategia']
#                     player['Saldo']-=landing_site_value
#             elif player['Estrategia']=='Cautious':
#                 if player['Saldo']>=(80+landing_site_value): #cauteloso compra sempre que sobre +80 caso compre
#                     #landing_site_owner=player['Estrategia'] #aqui tentei usar a var landing_site_owner, mas daí nao atualizava a lista da board, achei que tratia o p1,p2,p3,p4
#                     board[player['Posicao']]['Dono']=player['Estrategia']
#                     player['Saldo']-=landing_site_value
#             else:
#                 if (player['Saldo']>=landing_site_value) and (random.randrange(1,3,1)==1): #randomico compra sempre que tenha dinheiro e considerando teste randomico
#                     #landing_site_owner=player['Estrategia'] #aqui tentei usar a var landing_site_owner, mas daí nao atualizava a lista da board, achei que tratia o p1,p2,p3,p4
#                     board[player['Posicao']]['Dono']=player['Estrategia']
#                     player['Saldo']-=landing_site_value
#         else:  #se está numa casa com dono, paga aluguel
#             player['Saldo']-=landing_site_rent
#             for owner in player_order:
#                 if owner['Estrategia']==landing_site_owner:
#                     owner['Saldo']+=landing_site_rent
#             #player_order[landing_site_owner]['Saldo']+=landing_site_rent
#             #codigo desse jeito deu erro, tem a ver com o landing_site_owner acabar trazendo o dict inteiro, mudei para o nome da estratégia agora para testar


#         #3 - Parte que checa condições de derrota no final de turno do player
#         if player['Saldo']<0:
#             player_order.remove(player)
            
#             #eliminar o player como dono de todas suas propriedades
#             for x in board:
#                 if x['Dono']==player['Estrategia']:
#                     x['Dono']='banco'
#     return True       

# def play_game(player_order,board):
#     game_round=0 #round atual
    
#     while game_round < max_rounds:
#         round(player_order,board)
#         if len(player_order)==1:#se o jogo acabou por restar apenas um jogador
#             game_winner_strat=player_order[0]['Estrategia']
#             game_data={'Winner':game_winner_strat,'Rounds':game_round}
#             return game_data
#         game_round+=1
    
#     #se saiu do loop do while é pq deu os 1000 turnos e o vencedor será o que tem mais dinheiro
#     def saldo_vencedor(e):
#         return e['Saldo']

#     player_order.sort(reverse=True, key=saldo_vencedor) #ordenaa a lista dos players ativos por saldo do maior para menor
#     game_winner_strat=player_order[0]['Estrategia'] #pega o primeiro player e chama de vencedor do jogo
#     game_data={'Winner':game_winner_strat,'Rounds':game_round}

#     return game_data

    
# def run_simulations(simulations):
#     simulations_data=[] #lista com as estatiscas das simulações rodadas
#     for _ in range(simulations):
#         #antes chamava estas funções antes das definições das funções de jogo, mas ai nao resetava entre simulações, por isso botei aqui pra gerar entre cada simulação
#         player_order=order_players()
#         board=gera_board(casas)
#         simulations_data.append(play_game(player_order,board))
    
#     timeouts=0
#     total_rounds=0
#     win_count={'Impulsive':0,'Demanding':0,'Cautious':0,'Random':0}

#     for x in simulations_data:
#         if x['Rounds']==1000:
#             timeouts+=1

#         total_rounds+=x['Rounds']

#         for a in win_count:
#             if x['Winner']==a:
#                 win_count[a]+=1

#     #i
#     # best_strat=max(zip(win_count.values(), win_count.keys()))[1] #nao entendi o uso dessa função, copiei da net
#     #troquei pelo codigo de noob abaixo
#         # a=('a','b'=2,'c','d')
#         # b=(1,2,3,4)
    
#         # c = (('a', 1), ('b', 1), ('c', 3)) #mais ou menos oq o zip faz

#     max=0
#     best_strat=''
#     for x in win_count: 
#         if max<win_count[x]:
#             max=win_count[x]
#             best_strat=x   

#     #outra forma ainda de fazer
#     # max=0
#     # best_strat=''
#     # for x,y in win_count.items(): 
#     #     if max<y:
#     #         max=y
#     #         best_strat=x 

#     print(f"Jogos com timeout: {timeouts}")
#     print(f"Média de turnos por jogo: {total_rounds/simulations}")
#     for chave, valor in win_count.items():
#         print(f"A taxa de sucesso da estratégia {chave} foi de {100*valor/simulations}%")
#     print(f"A melhor estratégia de jogo foi: {best_strat}")

# run_simulations(1000)

