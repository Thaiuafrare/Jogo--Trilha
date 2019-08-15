##Aqui esta o tabuleiro usado como mapa das posições na hora de mover as peças.
posi2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','w','x']
def tabuleiro_inicial(posi2):
    print('Pra lembrar as posições :)')
    print((' %s ---------------- %s --------------- %s\n')%(posi2[0],posi2[1],posi2[2]),
    ('|                  |                 |\n'),
    ('|     %s ---------  %s --------- %s     |\n')%(posi2[3],posi2[4],posi2[5]),
    ('|     !            !           !     |\n'),   
    ('|     !   %s ...... %s ..... %s   !     |\n')%(posi2[6],posi2[7],posi2[8]),
    ('|     !   !                !   !     |\n'),
    ('%s --- %s - %s                %s - %s --- %s\n')%(posi2[9],posi2[10],posi2[11],posi2[12],posi2[13],posi2[14]),
    ('|     !   !                !   !     |\n'),
    ('|     !   %s ...... %s ..... %s   !     |\n')%(posi2[15],posi2[16],posi2[17]),
    ('|     !            !           !     |\n'),
    ('|     %s ---------- %s --------- %s     |\n')%(posi2[18],posi2[19],posi2[20]),   
    ('|                  !                 |\n'),
    ('%s ---------------- %s --------------- %s')%(posi2[21],posi2[22],posi2[23]))


posi = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','w','x']
## Aqui esta o tabuleiro do jogo.
def tabuleiro(posi):
    print((' %s ---------------- %s --------------- %s\n')%(posi[0],posi[1],posi[2]),
    ('|                  |                 |\n'),
    ('|     %s ---------  %s --------- %s     |\n')%(posi[3],posi[4],posi[5]),
    ('|     !            !           !     |\n'),
    ('|     !   %s ...... %s ..... %s   !     |\n')%(posi[6],posi[7],posi[8]),
    ('|     !   !                !   !     |\n'),
    ('%s --- %s - %s                %s - %s --- %s\n')%(posi[9],posi[10],posi[11],posi[12],posi[13],posi[14]),
    ('|     !   !                !   !     |\n'),
    ('|     !   %s ...... %s ..... %s   !     |\n')%(posi[15],posi[16],posi[17]),
    ('|     !            !           !     |\n'),
    ('|     %s ---------- %s --------- %s     |\n')%(posi[18],posi[19],posi[20]),   
    ('|                  !                 |\n'),
    ('%s ---------------- %s --------------- %s')%(posi[21],posi[22],posi[23]))


import sys    
global qtd_pecas_jogador1 
global qtd_pecas_jogador2
global ja_foi1
global ja_foi2
## O contador de peças que já foram colocadas
qtd_pecas_colocadas1 = 0
qtd_pecas_colocadas2 = 0

print()          
tabuleiro(posi)
## Quantidades de peças dos jogadores(as)
qtd_pecas_jogador1 = 9
qtd_pecas_jogador2 = 9
## Armazenador de trilhas que tem como objetivo de guardar as trilhas que já foram feitas para que não sejam reconhecidas novamente a não ser quer que esta trilha seja desfeita e momentos depois seja refeita.
ja_foi1 = []
ja_foi2 = []

## Aqui identifica as trilhas, o jagador(a) tem direito de retirar uma peça do adversario se completar uma trilha.
def ponto1(posi):
    global dele1
    global ja_foi1
    global qtd_pecas_jogador2
    for x in ja_foi1:
        if x == False:
            del(ja_foi1[x])
    lista_das_trilhas = [[posi[0] == posi[1]== posi[2] == '#'] , [posi[3] == posi[4] == posi[5] == '#'] , [posi[6] == posi[7] == posi[8] == '#'] , \
      [posi[0] == posi[9] == posi[21] == '#'] or [posi[21] == posi[22] == posi[23] == '#'] , [posi[23] == posi[14] == posi[2] == '#'] , \
       [posi[3] == posi[10] == posi[18] == '#'] or [posi[18] == posi[19] == posi[20] == '#'] , [posi[20] == posi[13] == posi[5] == '#'] , \
       [posi[9] == posi[10] == posi[11] == '#'] or [posi[12] == posi[13] == posi[14] == '#'] , [posi[16] == posi[19] == posi[22] == '#'] , \
       [posi[16] == posi[19] == posi[22] == '#'] or [posi[1] == posi[4] == posi[7] == '#'] , [posi[6] == posi[11] == posi[15] == '#'] , \
       [posi[8] == posi[12] == posi[17] == '#'] or [posi[15]== posi[16] == posi[17] == '#'] , [posi[17] == posi[12] == posi[8] == '#']]
    for g in lista_das_trilhas:
        if g[0] == True:
            if g in ja_foi1:
                print()
            else:
                tabuleiro(posi)
                print()
                print(80*'-')
                print('(Jogador # )Você fez uma trilha!!')
                print(50*'+')
                print()
                tabuleiro_inicial(posi2)
                print()
                print(50*'+')
                dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
               
                if dele1 == 'a' or dele1 == 'A':
                    if posi[0] == 'A' or posi[0] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[0] = 'A'
                elif dele1 == 'b' or dele1 == 'B':
                    if posi[1] ==  'B' or posi[1] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[1] = 'B'
                elif dele1 == 'c' or dele1 == 'C':
                    if posi[2] == 'C' or posi[2] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[2] = 'C'
                elif dele1 == 'd' or dele1 == 'D':
                    if posi[3] == 'D' or posi[3] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[3] = 'D'
                elif dele1 == 'e' or dele1 == 'E':
                    if posi[4] == 'E' or posi[4] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[4] = 'E'
                elif dele1 == 'f' or dele1 == 'F':
                    if posi[5] == 'F' or posi[5] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[5] = 'F'
                elif dele1 == 'g' or dele1 == 'G':
                    if posi[6] == 'G' or posi[6] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[6] = 'G'
                elif dele1 == 'h' or dele1 == 'H':
                    if posi[7] == 'H' or posi[7] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[7] = 'H'
                elif dele1 == 'i' or dele1 == 'I':
                    if posi[8] == 'I' or posi[8] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                       posi[8] = 'I'
                elif dele1 == 'j' or dele1 == 'J':
                    if posi[9] == 'J' or posi[9] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[9] = 'J'
                elif dele1 == 'k' or dele1 == 'K':
                    if posi[10] == 'K' or posi[10] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[10] = 'K'
               
                elif dele1 == 'l' or dele1 == 'L':
                    if posi[11] == 'L' or posi[11] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[11] = 'L'
                elif dele1 == 'm' or dele1 == 'M':
                    if posi[12] == 'M' or posi[12] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[12] = 'M'
                elif dele1 == 'n' or dele1 == 'N':
                    if posi[13] == 'N' or posi[13] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[13] = 'N'
                elif dele1 == 'o' or dele1 == 'O':
                    if posi[14] == 'O' or posi[14] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[14] = 'O'
                elif dele1 == 'p' or dele1 == 'P':
                    if posi[15] == 'P' or posi[15] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[15] = 'P'
               
                elif dele1 == 'q' or dele1 == 'Q':
                    if posi[16] == 'Q' or posi[16] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    posi[16] = 'Q'
                elif dele1 == 'r' or dele1 == 'R':
                    if posi[17] == 'R' or posi[17] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[17] = 'R'
                elif dele1 == 's' or dele1 == 'S':
                    if posi[18] == 'S' or posi[18] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[18] = 'S'
                elif dele1 == 't' or dele1 == 'T':
                    if posi[19] == 'T' or posi[19] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[19] = 'T'
                elif dele1 == 'u' or dele1 == 'U':
                    if posi[20] == 'U' or posi[20] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[20] = 'U'
                elif dele1 == 'v' or dele1 == 'V':
                    if posi[21] == 'V' or posi[21] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[21] = 'V'

                elif dele1 == 'w' or dele1 == 'W':
                    if posi[22] == 'W' or posi[22] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[22] = 'W'
                elif dele1 == 'x' or dele1 == 'X':
                    if posi[23] == 'X' or posi[23] == '#':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele1 = str(input('(Jogador # )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[23] = 'X'
                        
               
                qtd_pecas_jogador2 = qtd_pecas_jogador2 - 1
                print(80*'-')
                print()
            ja_foi1.append(g)    
## Aqui identifica as trilhas, o jagador(a) tem direito de retirar uma peça do adversario se completar uma trilha.
def ponto2(posi):
     global dele2
     global ja_foi2
     global qtd_pecas_jogador1
     for x in ja_foi2:
        if x == False:
            del(ja_foi2[x])
     lista_das_trilhas2 = [[posi[0] == posi[1]== posi[2] == '#'] , [posi[3] == posi[4] == posi[5] == '#'] , [posi[6] == posi[7] == posi[8] == '#'] , \
     [posi[0] == posi[9] == posi[21] == '#'] or [posi[21] == posi[22] == posi[23] == '#'] , [posi[23] == posi[14] == posi[2] == '#'] , \
    [posi[3] == posi[10] == posi[18] == '#'] or [posi[18] == posi[19] == posi[20] == '#'] , [posi[20] == posi[13] == posi[5] == '#'] , \
    [posi[9] == posi[10] == posi[11] == '#'] or [posi[12] == posi[13] == posi[14] == '#'] , [posi[16] == posi[19] == posi[22] == '#'] , \
    [posi[16] == posi[19] == posi[22] == '#'] or [posi[1] == posi[4] == posi[7] == '#'] , [posi[6] == posi[11] == posi[15] == '#'] , \
    [posi[8] == posi[12] == posi[17] == '#'] or [posi[15]== posi[16] == posi[17] == '#'] , [posi[17] == posi[12] == posi[8] == '#']]
     for g in lista_das_trilhas2:
         if g[0] == True:
             if g in ja_foi2:
                 print()
             else:
                 print()
                 tabuleiro(posi)
                 print()
                 print(80*'-')
                 print()
                 print('(Jogador @)Você fez uma trilha!!')
                 print(50*'+')
                 print()
                 tabuleiro_inicial(posi2)
                 print()
                 print(50*'+')
                
                 dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                 if dele2 == 'a' or dele2 == 'A':
                    if posi[0] == 'A' or posi[0] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                        print()
                    else:
                        posi[0] = 'A'
                 elif dele2 == 'b' or dele2 == 'B':
                    if posi[1] ==  'B' or posi[1] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                        print()
                    else:
                        posi[1] = 'B'
                 if dele2 == 'c' or dele2 == 'C':
                    if posi[2] == 'C' or posi[2] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[2] = 'C'
                 elif dele2 == 'd' or dele2 == 'D':
                    if posi[3] == 'D' or posi[3] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                        print()
                    else:
                        posi[3] = 'D'
                 elif dele2 == 'e' or dele2 == 'E':
                    if posi[4] == 'E' or posi[4] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                        print()
                    else:
                        posi[4] = 'E'
                 elif dele2 == 'f' or dele2 == 'F':
                    if posi[5] == 'F' or posi[5] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                        print()
                    else:
                        posi[5] = 'F'
                 elif dele2 == 'g' or dele2 == 'G':
                    if posi[6] == 'G' or posi[6] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[6] = 'G'
                 elif dele2 == 'a' or dele2 == 'H':
                    if posi[7] == 'H' or posi[7] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))

                        print()
                    else:
                        posi[7] = 'H'
                 elif dele2 == 'i' or dele2 == 'I':
                    if posi[8] == 'I' or posi[8] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[8] = 'I'
                 elif dele2 == 'j' or dele2 == 'J':
                    if posi[9] == 'J' or posi[9] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[9] = 'J'
                 elif dele2 == 'k' or dele2 == 'K':
                    if posi[10] == 'K' or posi[10] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[10] = 'K'
               
                 elif dele2 == 'l' or dele2 == 'L':
                    if posi[11] == 'L' or posi[11] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[11] = 'L'
                 elif dele2 == 'm' or dele2 == 'M':
                    if posi[12] == 'M' or posi[12] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[12] = 'M'
                 elif dele2 == 'n' or dele2 == 'N':
                    if posi[13] == 'N' or posi[13] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[13] = 'N'
                 elif dele2 == 'o' or dele2 == 'O':
                    if posi[14] == 'O' or posi[14] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[14] = 'O'
                 elif dele2 == 'p' or dele2 == 'P':
                    if posi[15] == 'P' or posi[15] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[15] = 'P'
               
                 elif dele2 == 'q' or dele2 == 'Q':
                    if posi[16] == 'Q' or posi[16] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[16] = 'Q'
                 elif dele2 == 'r' or dele2 == 'R':
                    if posi[17] == 'R' or posi[17] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[17] = 'R'
                 elif dele2 == 's' or dele2 == 'S':
                    if posi[18] == 'S' or posi[18] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[18] = 'S'
                 elif dele2 == 't' or dele2 == 'T':
                     if posi[19] == 'T' or posi[19] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                     else:
                        posi[19] = 'T'
                 elif dele2 == 'u' or dele2 == 'U':
                    if posi[20] == 'U' or posi[20] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[20] = 'U'
                 elif dele2 == 'v' or dele2 == 'V':
                    if posi[21] == 'V' or posi[21] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[21] = 'V'

                 elif dele2 == 'w' or dele2 == 'W':
                    if posi[22] == 'W' or posi[22] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[22] = 'W'
                 elif dele2 == 'x' or dele2 == 'X':
                    if posi[23] == 'X' or posi[23] == '@':
                        print()
                        print('movimento inválido!')
                        print()
                        print()
                        dele2 = str(input('(Jogador @ )Escolha uma peça para retirar do seu adversário : '))
                        print()
                    else:
                        posi[23] = 'X'

                
                 qtd_pecas_jogador1 = qtd_pecas_jogador1 - 1
                 print(80*'-')
                 print()
             ja_foi2.append(g)
## O jogo roda até um dos jogadores perderem, ou melhor, quando um deles(as) tiverem somente duas peças.
while qtd_pecas_jogador1 > 2 and qtd_pecas_jogador2 > 2:
    print()
    print(80*'-')
    if qtd_pecas_colocadas1 == 9:
        print()
        tabuleiro(posi)
        print()
        print()
        tabuleiro_inicial(posi2)
        print()
        ## Depois do jogador(a) 1 ter colocados suas 9 peças no tabuleiro, ele tem somente o direito de mover as peças entre as linhas localizadas ao lado das mesmas, a não ser que este jogador tem 3 peças, ai ele podera mover flutuando(Obs: Ele podera fazer qualquer movimento a qualquer hora, porém se não seguir as regras estará roubando).
        ## Aqui é onde ele escolhe de onde ele quer tirar a peça.
        tira1 = str(input('(Jogador #)Digite qual das suas peças você quer mover?: '))
        tabuleiro(posi)
        

        if tira1 == 'a' or tira1 == 'A':
            posi[0] = 'A'
        elif tira1 == 'b' or tira1 == 'B':
            posi[1] = 'B'
        elif tira1 == 'c' or tira1 == 'C':
            posi[2] = 'C'
        elif tira1 == 'd' or tira1 == 'D':
            posi[3] = 'D'
        elif tira1 == 'e' or tira1 == 'E':
            posi[4] = 'E'
        elif tira1 == 'f' or tira1 == 'F':
            posi[5] = 'F'
        elif tira1 == 'g' or tira1 == 'G':
            posi[6] = 'G'
        elif tira1 == 'h' or tira1 == 'H':
            posi[7] = 'H'
        elif tira1 == 'i' or tira1 == 'I':
            posi[8] = 'I'
        elif tira1 == 'j' or tira1 == 'J':
            posi[9] = 'J'
        elif tira1 == 'k' or tira1 == 'K':
            posi[10] = 'K'
        elif tira1 == 'l' or tira1 == 'L':
            posi[11] = 'L'
        elif tira1 == 'm' or tira1 == 'M':
            posi[12] = 'M'
        elif tira1 == 'n' or tira1 == 'N':
            posi[13] = 'N'
        elif tira1 == 'o' or tira1 == 'O':
            posi[14] = 'O'
        elif tira1 == 'p' or tira1 == 'P':
            posi[15] = 'P'
        elif tira1 == 'q' or tira1 == 'Q':
            posi[16] = 'Q'
        elif tira1 == 'r' or tira1 == 'R':
            posi[17] = 'R'
        elif tira1 == 's' or tira1 == 'S':
            posi[18] = 'S'
        elif tira1 == 't' or tira1 == 'T':
            posi[19] = 'T'
        elif tira1 == 'u' or tira1 == 'U':
            posi[20] = 'U'
        elif tira1 == 'v' or tira1 == 'V':
            posi[21] = 'V'
        elif tira1 == 'w' or tira1 == 'W':
            posi[22] = 'W'
        elif tira1 == 'x' or tira1 == 'X':
            posi[23] = 'X'
        ## Aqui ele descide onde vai coloca-la.  
        print()
        tabuleiro_inicial(posi2)
        print()
        coloca1 = str(input('(Jogador #)Digite aonde você quer colocar: '))
        print()
        print(20*' ! ')
        print()
        print('ATENÇÃO:  Você só pode mover a peça em linha, ou seja não pode pular de uma linha para outra a não ser que esta outra linha esteja ligada na sua atual posição!!!')
        print('')
        print()
        print(20*' ! ')
        print()
        tabuleiro(posi)
        print()
        if coloca1 == 'a' or coloca1 == 'A':
            posi[0] = '#'
        elif coloca1 == 'b' or coloca1 == 'B':
            posi[1] = '#'
        elif coloca1 == 'c' or coloca1 == 'C':
            posi[2] = '#'
        elif coloca1 == 'd' or coloca1 == 'D':
            posi[3] = '#'
        elif coloca1 == 'e' or coloca1 == 'E':
            posi[4] = '#'
        elif coloca1 == 'f' or coloca1 == 'F':
            posi[5] = '#'
        elif coloca1 == 'g' or coloca1 == 'G':
            posi[6] = '#'
        elif coloca1 == 'h' or coloca1 == 'H':
            posi[7] = '#'
        elif coloca1 == 'i' or coloca1 == 'I':
            posi[8] = '#'
        elif coloca1 == 'j' or coloca1 == 'J':
            posi[9] = '#'
        elif coloca1 == 'k' or coloca1 == 'K':
            posi[10] = '#'
        elif coloca1 == 'l' or coloca1 == 'L':
            posi[11] = '#'
        elif coloca1 == 'm' or coloca1 == 'M':
            posi[12] = '#'
        elif coloca1 == 'n' or coloca1 == 'N':
            posi[13] = '#'
        elif coloca1 == 'o' or coloca1 == 'O':
            posi[14] = '#'
        elif coloca1 == 'p' or coloca1 == 'P':
            posi[15] = '#'
        elif coloca1 == 'q' or coloca1 == 'Q':
            posi[16] = '#'
        elif coloca1 == 'r' or coloca1 == 'R':
            posi[17] = '#'
        elif coloca1 == 's' or coloca1 == 'S':
            posi[18] = '#'
        elif coloca1 == 't' or coloca1 == 'T':
            posi[19] = '#'
        elif coloca1 == 'u' or coloca1 == 'U':
            posi[20] = '#'
        elif coloca1 == 'v' or coloca1 == 'V':
            posi[21] = '#'
        elif coloca1 == 'w' or coloca1 == 'W':
            posi[22] = '#'
        elif coloca1 == 'x' or coloca1 == 'X':
            posi[23] = '#'

    ## Esta parte funciona até o jogador(a) colocar todas as peças no tabuleiro.       
    else:
        dig =str(input('Primeiro jogador(#) digite uma posição: '))
        print()
        if dig == 'A' or dig == 'a':
            posi[0] = '#'
        elif dig == 'B' or dig == 'b':
            posi[1] = '#'
        elif dig == 'C' or dig == 'c':
            posi[2] = '#'
        elif dig == 'D' or dig == 'd':
            posi[3] = '#'
        elif dig == 'E' or dig == 'e':
            posi[4] = '#'
        elif dig == 'F' or dig == 'f':
            posi[5] = '#'
        elif dig == 'G' or dig == 'g':
            posi[6] = '#'
        elif dig == 'H' or dig == 'h':
            posi[7] = '#'
        elif dig == 'I' or dig == 'i':
            posi[8] = '#'
        elif dig == 'J' or dig == 'j':
            posi[9] = '#'
        elif dig == 'K' or dig == 'k':
            posi[10] = '#'
        elif dig == 'L' or dig == 'l':
            posi[11] = '#'
        elif dig == 'M' or dig == 'm':
            posi[12] = '#'
        elif dig == 'N' or dig == 'n':
            posi[13] = '#'
        elif dig == 'O' or dig == 'o':
            posi[14] = '#'
        elif dig == 'P' or dig == 'p':
            posi[15] = '#'
        elif dig == 'Q' or dig == 'q':
            posi[16] = '#'
        elif dig == 'R' or dig == 'r':
            posi[17] = '#'
        elif dig == 'S' or dig == 's':
            posi[18] = '#'
        elif dig == 'T' or dig == 't':
            posi[19] = '#'
        elif dig == 'U' or dig == 'u':
            posi[20] = '#'
        elif dig == 'V' or dig == 'v':
            posi[21] = '#'
        elif dig == 'W' or dig == 'w':
            posi[22] = '#'
        elif dig == 'X' or dig == 'x':
            posi[23] = '#'
        qtd_pecas_colocadas1 += 1
           
            


    ponto1(posi)
    ## Aqui se por um acaso um dos jogadores(as) tiver vencido o jogo para.
    if qtd_pecas_jogador2 < 3:
        print('Jogador(a) # venceu!!')
        sys.exit()
    
    
    
    tabuleiro(posi)
    ## Aqui mostra a quantidade de peças dos jogadores(as).
    print('Jogador(a) um tem %d peças!'%qtd_pecas_jogador1)
    print('Jogador(a) dois tem %d peças!'%qtd_pecas_jogador2)
    
    print()
    ## Depois do jogador(a) 2 ter colocados suas 9 peças no tabuleiro, ele tem somente o direito de mover as peças entre as linhas localizadas ao lado das mesmas, a não ser que este jogador tem 3 peças, ai ele podera mover flutuando(Obs: Ele podera fazer qualquer movimento a qualquer hora, porém se não seguir as regras estará roubando).
    ## Aqui é onde ele escolhe de onde ele quer tirar a peça.
    if qtd_pecas_colocadas2 == 9:
        print()
        print()
        tabuleiro_inicial(posi2)
        print()
        tira2 = str(input('(Jogador @)Digite qual das suas peças você quer mover?: '))
        tabuleiro(posi)
        
        
        if tira2 == 'a' or tira2 == 'A':
            posi[0] = 'A'
        elif tira2 == 'b' or tira2 == 'B':
            posi[1] = 'B'
        elif tira2 == 'c' or tira2 == 'C':
            posi[2] = 'C'
        elif tira2 == 'd' or tira2 == 'D':
            posi[3] = 'D'
        elif tira2 == 'e' or tira2 == 'E':
            posi[4] = 'E'
        elif tira2 == 'f' or tira2 == 'F':
            posi[5] = 'F'
        elif tira2 == 'g' or tira2 == 'G':
            posi[6] = 'G'
        elif tira2 == 'h' or tira2 == 'H':
            posi[7] = 'H'
        elif tira2 == 'i' or tira2 == 'I':
            posi[8] = 'I'
        elif tira2 == 'j' or tira2 == 'J':
            posi[9] = 'J'
        elif tira2 == 'k' or tira2 == 'K':
            posi[10] = 'K'
        elif tira2 == 'l' or tira2 == 'L':
            posi[11] = 'L'
        elif tira2 == 'm' or tira2 == 'M':
            posi[12] = 'M'
        elif tira2 == 'n' or tira2 == 'N':
            posi[13] = 'N'
        elif tira2 == 'o' or tira2 == 'O':
            posi[14] = 'O'
        elif tira2 == 'p' or tira2 == 'P':
            posi[15] = 'P'
        elif tira2 == 'q' or tira2 == 'Q':
            posi[16] = 'Q'
        elif tira2 == 'r' or tira2 == 'R':
            posi[17] = 'R'
        elif tira2 == 's' or tira2 == 'S':
            posi[18] = 'S'
        elif tira2 == 't' or tira2 == 'T':
            posi[19] = 'T'
        elif tira2 == 'u' or tira2 == 'U':
            posi[20] = 'U'
        elif tira2 == 'v' or tira2 == 'V':
            posi[21] = 'V'
        elif tira2 == 'w' or tira2 == 'W':
            posi[22] = 'W'
        elif tira2 == 'x' or tira2 == 'X':
            posi[23] = 'X'
        ## Aqui ele descide onde irá colocar a peças.
        print()
        tabuleiro_inicial(posi2)
        print()
        coloca2 = str(input('(Jogador @)Digite aonde você quer colocar: '))
        print()
        print(20*' ! ')
        print()
        print('ATENÇÃO:  Você só pode mover a peça em linha, ou seja não pode pular de uma linha para outra a não ser que esta outra linha esteja ligada na sua atual posição!!!')
        print('')
        print()
        print(20*' ! ')
        print()
        tabuleiro_inicial
        print()

        if coloca2 == 'a' or coloca2 == 'A':
            posi[0] = '@'
        elif coloca2 == 'b' or coloca2 == 'B':
            posi[1] = '@'
        elif coloca2 == 'c' or coloca2 == 'C':
            posi[2] = '@'
        elif coloca2 == 'd' or coloca2 == 'D':
            posi[3] = '@'
        elif coloca2 == 'e' or coloca2 == 'E':
            posi[4] = '@'
        elif coloca2 == 'f' or coloca2 == 'F':
            posi[5] = '@'
        elif coloca2 == 'g' or coloca2 == 'G':
            posi[6] = '@'
        elif coloca2 == 'h' or coloca2 == 'H':
            posi[7] = '@'
        elif coloca2 == 'i' or coloca2 == 'I':
            posi[8] = '@'
        elif coloca2 == 'j' or coloca2 == 'J':
            posi[9] = '@'
        elif coloca2 == 'k' or coloca2 == 'K':
            posi[10] = '@'
        elif coloca2 == 'l' or coloca2 == 'L':
            posi[11] = '@'
        elif coloca2 == 'm' or coloca2 == 'M':
            posi[12] = '@'
        elif coloca2 == 'n' or coloca2 == 'N':
            posi[13] = '@'
        elif coloca2 == 'o' or coloca2 == 'O':
            posi[14] = '@'
        elif coloca2 == 'p' or coloca2 == 'P':
            posi[15] = '@'
        elif coloca2 == 'q' or coloca2 == 'Q':
            posi[16] = '@'
        elif coloca2 == 'r' or coloca2 == 'R':
            posi[17] = '@'
        elif coloca2 == 's' or coloca2 == 'S':
            posi[18] = '@'
        elif coloca2 == 't' or coloca2 == 'T':
            posi[19] = '@'
        elif coloca2 == 'u' or coloca2 == 'U':
            posi[20] = '@'
        elif coloca2 == 'v' or coloca2 == 'V':
            posi[21] = '@'
        elif coloca2 == 'w' or coloca2 == 'W':
            posi[22] = '@'
        elif coloca2 == 'x' or coloca2 == 'X':
            posi[23] = '@'
        
        
    ## Esta parte funciona até o jogador(a) colocar todas as peças no tabuleiro.   
    else:
        dig2= str(input('Segundo jogador(@) digite uma posição: '))
        print()
        while dig2 == dig:
            print()
            print('Não é possivel colocar no mesmo lugar!')
            print(80*'-')
            dig2= str(input('Segundo jogador(@) digite uma posição: '))
            print()
        else:
            if dig2 == 'A' or dig2 == 'a':
                posi[0] = '@'
            elif dig2 == 'B' or dig2 == 'b':
                posi[1] = '@'
            elif dig2 == 'C' or dig2 == 'c':
                posi[2] = '@'
            elif dig2 == 'D' or dig2 == 'd':
                posi[3] = '@'
            elif dig2 == 'E' or dig2 == 'e':
                posi[4] = '@'
            elif dig2 == 'F' or dig2 == 'f':
                posi[5] = '@'
            elif dig2 == 'G' or dig2 == 'g':
                posi[6] = '@'
            elif dig2 == 'H' or dig2 == 'h':
                posi[7] = '@'
            elif dig2 == 'I' or dig2 == 'i':
                posi[8] = '@'
            elif dig2 == 'J' or dig2 == 'j':
                posi[9] = '@'
            elif dig2 == 'K' or dig2 == 'k':
                posi[10] = '@'
            elif dig2 == 'L' or dig2 == 'l':
                posi[11] = '@'
            elif dig2 == 'M' or dig2 == 'm':
                posi[12] = '@'
            elif dig2 == 'N' or dig2 == 'n':
                posi[13] = '@'
            elif dig2 == 'O' or dig2 == 'o':
                posi[14] = '@'
            elif dig2 == 'P' or dig2 == 'p':
                posi[15] = '@'
            elif dig2 == 'Q' or dig2 == 'q':
                posi[16] = '@'
            elif dig2 == 'R' or dig2 == 'r':
                posi[17] = '@'
            elif dig2 == 'S' or dig2 == 's':
                posi[18] = '@'
            elif dig2 == 'T' or dig2 == 't':
                posi[19] = '@'
            elif dig2 == 'U' or dig2 == 'u':
                posi[20] = '@'
            elif dig2 == 'V' or dig2 == 'v':
                posi[21] = '@'
            elif dig2 == 'W' or dig2 == 'w':
                posi[22] = '@'
            elif dig2 == 'X' or dig2 == 'x':
                posi[23] = '@'
                
            qtd_pecas_colocadas2 += 1
            
            
        

        ponto2(posi)
        
        if qtd_pecas_jogador1 < 3:
            print()
            print('Jogador(a) @ venceu!!')
            print()
            sys.exit()
               
        
    
        
        tabuleiro(posi)
        print('Jogador(a) # tem %d peças!'%qtd_pecas_jogador1)
        print('Jogador(a) @ tem %d peças!'%qtd_pecas_jogador2)

        

    
