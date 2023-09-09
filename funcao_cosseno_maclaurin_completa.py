def funcao_cosseno_maclaurin(x, precisao_desejada):
    import numpy as np
    import math
    precisao_desejada_alcancada = False
    #Booleana que determina se a estimativa atual está dentro da precisão
    #desejada ou não

    k = 0
    # número de termos da série de Maclaurin considerados até o momento

    f = 0
    #Estimativa da função que queremos calcular, inicializada como 0
    
    r=0
    #Nesse caso r será a função do resto, que será utilizada para avalair a precisão desejada
    while not precisao_desejada_alcancada:
        if k == 0:
            f += 1
        elif k >= 1 and k % 2 == 0 and k % 4 != 0:
            f += (-1) * ((x ** k) / math.factorial(k))
        elif k >= 1 and k % 4 == 0:
            f += (x ** k) / math.factorial(k)
        
        r = (1 / math.factorial(k + 1)) * (np.abs(x) ** (k + 1))
        
        if r <= precisao_desejada:
            precisao_desejada_alcancada = True
        else:
            k += 1

        # Aqui, vocês devem implementar o cálculo da função seno a partir
        # da série de MacLaurin, bem como do resto (para verificar se a
        # precisão desejada foi alcançada)
        
        # Enquanto a precisão desejada não tiver sido alcançada, 
        # incrementamos o valor de k e adicionamos novos termos ao
        # polinômio.
        
        
    return [f,k]

