(define (problem carga-aerea)
    (:domain aviones)
    (:objects 
        LA01
        LA02
        LA03
     	LA04
        AA01
        AA02
        AA03
     	AA04
        FB01
        FB02
        FB03
     	FB04
        MDZ
        AEP
        COR
        SFN
     	EZE
     	CARNES
        FERTILIZANTE
        TELA-GRANIZO
        COSECHADORA
        AUTOPARTES
     	MAQUINAS-HERR    	
    )
    (:init 
        (avion LA01)
        (avion LA02)
        (avion LA03)
     	(avion LA04)
        (avion AA01)
        (avion AA02)
        (avion AA03)
        (avion AA04)
        (avion FB01)
        (avion FB02)
        (avion FB03)
     	(avion FB04)
        (aeropuerto MDZ)
        (aeropuerto AEP)
        (aeropuerto COR)
        (aeropuerto SFN)
     	(aeropuerto EZE)
        (carga FERTILIZANTE)
        (carga TELA-GRANIZO)
        (carga COSECHADORA)
        (carga AUTOPARTES)
     	(carga CARNES)
     	(carga MAQUINAS-HERR)
        (en LA01 MDZ)
        (en LA02 AEP)
        (en LA03 COR)
     	(en LA04 SNF)
        (en AA01 SFN)
        (en AA02 MDZ)
        (en AA03 EZE)
     	(en AA04 COR)
        (en FB01 EZE)
        (en FB02 AEP)
        (en FB03 COR)
     	(en FB04 MDZ)
        (en FERTILIZANTE EZE)
        (en TELA-GRANIZO AEP)
        (en COSECHADORA SFN)
        (en AUTOPARTES COR)
     	(en CARNES MDZ)
     	(en MAQUINAS-HERR MDZ)
    )
    (:goal 
        (and
            (en FERTILIZANTE SFN)
            (en TELA-GRANIZO MDZ)
            (en COSECHADORA COR)
            (en AUTOPARTES EZE)
         	(en CARNES AEP)
         	(en MAQUINAS-HERR EZE)
        )
    )
)