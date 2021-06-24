(define (problem capp-pieza)
    (:domain capp)
    (:objects 
        orientacion+x
        orientacion+y
        orientacion+z
        orientacion-x
        orientacion-y
        orientacion-z
        s2
        s4
        s6
     	s8
        s9
        s10
     	h1
     	h3
     	h5
     	h7
     	h9
     	h11
     	h12
        slot
        through-hole
        blind-hole
        fresado
        taladrado
        torneado
    )
    (:init 
        (orientacion orientacion+x)
        (orientacion orientacion+y)
        (orientacion orientacion+z)
        (orientacion orientacion-x)
        (orientacion orientacion-y)
        (orientacion orientacion-z)
        (feature s2)
        (feature s4)
        (feature s6)
     	(feature s8)
        (feature s9)
        (feature s10)
     	(feature h1)
     	(feature h3)
     	(feature h5)
     	(feature h7)
     	(feature h9)
     	(feature h11)
     	(feature h12)
        (tipo slot)
        (tipo through-hole)
        (tipo blind-hole)
        (operacion fresado)
        (operacion taladrado)
        (operacion torneado)
        (feature-tipo s2 slot)
        (feature-tipo s4 slot)
        (feature-tipo s6 slot)
     	(feature-tipo s8 slot)
        (feature-tipo s9 slot)
        (feature-tipo s10 slot)
     	(feature-tipo h1 blind-hole)
     	(feature-tipo h3 through-hole)
     	(feature-tipo h5 through-hole)
     	(feature-tipo h7 through-hole)
     	(feature-tipo h9 through-hole)
     	(feature-tipo h11 through-hole)
     	(feature-tipo h12 through-hole)
        (orientacion-pieza orientacion-x)
        (orientacion-feature s2 orientacion+x)
        (orientacion-feature s4 orientacion-x)
        (orientacion-feature s6 orientacion+x)
     	(orientacion-feature s8 orientacion-x)
        (orientacion-feature s9 orientacion+z)
        (orientacion-feature s10 orientacion+z)
     	(orientacion-feature h1 orientacion+z)
     	(orientacion-feature h3 orientacion+z)
     	(orientacion-feature h5 orientacion+z)
     	(orientacion-feature h7 orientacion+x)
     	(orientacion-feature h9 orientacion+x)
     	(orientacion-feature h11 orientacion+x)
     	(orientacion-feature h12 orientacion+x)
        (fabricable slot fresado)
     	(fabricable through-hole taladrado)
     	(fabricable blind-hole taladrado)
  
    )
    (:goal 
        (and
            (fabricada s2)
            (fabricada s4)
            (fabricada s6)
         	(fabricada s8)
            (fabricada s9)
            (fabricada s10)
         	(fabricada h1)
         	(fabricada h3)
         	(fabricada h5)
         	(fabricada h7)
         	(fabricada h9)
         	(fabricada h11)
         	(fabricada h12)
        )
    )
)