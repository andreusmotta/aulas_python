velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_rada_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('A velocidade do carro era maior quando passou no radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if  carro_passou_radar_1 and vel_carro_pass_radar_1:
    print('O carro foi multado no radar 1')