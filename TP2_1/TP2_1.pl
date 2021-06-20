/*Sistema experto para mantenimiento de sistema de control 
de valvula de seguridad en estacion de reduccion de presion de gas 

Estados Posibles: yes, no, desconocido.
verificar: verifica el estado actual y devulve la accion correspondiente.

Axiomas (invariantes del dominio) */

% Rama Central derecha
verificar(preventable_leakage) :- 
    estado(preventable_leakage, yes), writeln('Set the safety valve according to the intructions');
    estado(preventable_leakage, no), writeln('Replace Sit and Orifice and put the safety valve into circuit');
    (estado(preventable_leakage, desconocido), 
    ((estado(safety_spring_effective, yes), writeln('Verificar preventable_leakage'));
    (estado(safety_spring_effective, no), writeln('Replace the safety spring in the service'));
    verificar(safety_spring_effective))).

verificar(safety_spring_effective) :-
    estado(safety_spring_effective, desconocido),
    ((estado(control_pressuare_sensor_pipes_blocked, yes), writeln('Clean up and fix the faults of the sensing pipes'));
    (estado(control_pressuare_sensor_pipes_blocked, no), writeln('Verificar safety spring'));
    verificar(control_pressuare_sensor_pipes_blocked)).

verificar(control_pressuare_sensor_pipes_blocked) :-
    estado(control_pressuare_sensor_pipes_blocked, desconocido),
    ((estado(line_gas_pressure_appropiate, yes), writeln('Verificar control and pressuare sensor pipes blocked'));
    (estado(line_gas_pressure_appropiate, no), writeln('Adjust the regulator according to the instructions'));
    verificar(line_gas_pressure_appropiate)).

verificar(line_gas_pressure_appropiate) :-
    estado(line_gas_pressure_appropiate, desconocido),
    ((estado(safety_valve_has_continuous_evacuation, yes), writeln('Verificar line gas pressure'));
    (estado(safety_valve_has_continuous_evacuation, no), writeln('Safety valve has not a continuous gas evacuation, Verificar safety valve has continuous evacuation ')); 
    verificar(safety_valve_has_continuous_evacuation)).


% Rama Central Izquierda
verificar(piloto) :- 
    estado(piloto, yes), writeln('Set the safety valve according to the intructions');
    estado(piloto, no), writeln('Pilot full service and reinstall ion');
    (estado(piloto, desconocido), 
    ((estado(leakage_prevention_between_sit_and_orifice, yes), writeln('Verificar Pilot'));
    (estado(leakage_prevention_between_sit_and_orifice, no), writeln('Replace Sit and Orifice and put the safety value into circuit'));
    verificar(leakage_prevention_between_sit_and_orifice))).

verificar(leakage_prevention_between_sit_and_orifice) :- 
    estado(leakage_prevention_between_sit_and_orifice, desconocido), 
    ((estado(safety_valve_spring, yes), writeln('Verificar leakage prevention between sit and orifice'));
    (estado(safety_valve_spring, no), writeln('Putting spring and safety n the service'));
    verificar(safety_valve_spring)).

verificar(safety_valve_spring) :- 
    estado(safety_valve_spring, desconocido), 
    ((estado(control_valve_sensors_blocked, no), writeln('Verificar safety valve spring'));
    (estado(control_valve_sensors_blocked, yes), writeln('Cleaning and troubleshooting of the sensing pipes'));
    verificar(control_valve_sensors_blocked)).

verificar(control_valve_sensors_blocked) :- 
    estado(control_valve_sensors_blocked, desconocido), 
    ((estado(valve_status_closed, no), writeln('Verificar control valve sensors blocked'));
    (estado(valve_status_closed, yes), writeln('Place the safety valve in open position'));
    verificar(valve_status_closed)).
                
verificar(valve_status_closed) :- 
    estado(valve_status_closed, desconocido),
    ((estado(relief_valve_ok_with_10_percent_more_pressure, no), writeln('Verificar valve status "Close"'));
    (estado(relief_valve_ok_with_10_percent_more_pressure, yes), writeln('Safety function is appropiate'));
    verificar(relief_valve_ok_with_10_percent_more_pressure)).
                
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 
    estado(relief_valve_ok_with_10_percent_more_pressure, desconocido),
    ((estado(safety_valve_has_continuous_evacuation, no), writeln('Verificar relief valve works correctly with +10% over regular pressure'));
    (estado(safety_valve_has_continuous_evacuation, yes), writeln('Safety valve has a continuous gas evacuation, Verificar safety valve has continuous evacuation ')); 
    verificar(safety_valve_has_continuous_evacuation)).
            
verificar(safety_valve_has_continuous_evacuation) :- 
    estado(safety_valve_has_continuous_evacuation, desconocido), 
    writeln('Verificar safety valve has continuous evacuation').


% Rama Izquierda tomamos el cero como valor desconocido.
verificar(thickness_less_threshold) :-
    thickness(valve,Esp),threshold(valve,Limit),Esp =\= 0, Limit =\= 0, Esp < Limit, writeln('Report to the Technical Inspection Unit inmediately');
    thickness(valve,Esp),threshold(valve,Limit), Esp =\= 0, Limit =\= 0, Esp >= Limit, writeln('The condition of the equipment is suitable');
    ((thickness(valve,Esp),Esp = 0; threshold(valve,Limit), Limit=0),
    ((estado(valve_body_having_dazzling_rusting,no), writeln('Verificar thickness less than threshold limit'));
    (estado(valve_body_having_dazzling_rusting,yes), writeln('Coordination is required in order to render and color the equipment'));   
    verificar(valve_body_having_dazzling_rusting))).

verificar(valve_body_having_dazzling_rusting) :-
    estado(valve_body_having_dazzling_rusting, desconocido), 
    writeln('Verificar valve body, pipes and joints is having the effecrs of dazzling and rusting').



% Rama Derecha
verificar(leakage_fixed) :-
    estado(leakage_fixed, yes), writeln('Report to the Technical Inspection Unit');
    estado(leakage_fixed, no), writeln('Send to report to the repair department to fix the fault');
    (estado(leakage_fixed, desconocido),
    ((estado(gas_leakage_joint,no), writeln('The safety valve joint are free of gas leakage'));
    (estado(gas_leakage_joint,yes), writeln('Verificar leakage fixed with the wrench al joints'));   
    verificar(gas_leakage_joint))).

verificar(gas_leakage_joint) :-
    estado(gas_leakage_joint, desconocido), 
    writeln('Verificar gas leakage at joint').

/* Ground Facts de instancia variables */

% Rama Central derecha
estado(preventable_leakage, desconocido).
estado(safety_spring_effective, desconocido).
estado(control_pressuare_sensor_pipes_blocked, desconocido).
estado(line_gas_pressure_appropiate, desconocido).
% Rama Central Izquierda
estado(piloto, desconocido).
estado(leakage_prevention_between_sit_and_orifice, desconocido).
estado(safety_valve_spring, desconocido).
estado(control_valve_sensors_blocked, desconocido).
estado(valve_status_closed, desconocido).
estado(relief_valve_ok_with_10_percent_more_pressure, no).
estado(safety_valve_has_continuous_evacuation, no).
% Rama Derecha
estado(leakage_fixed, desconocido).
estado(gas_leakage_joint, desconocido).
% Rama Izquierda
estado(valve_body_having_dazzling_rusting, no).
thickness(valve,Thi):- Thi is 50. %tomamos el cero como valor desconocido
threshold(valve,The):- The is 40.
