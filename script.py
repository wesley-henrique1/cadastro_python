import datetime 
from datetime import datetime, timedelta


def app():
    hora = datetime.strptime(input("Digite a hora inicial: "), "%H:%M")
    print("--- Seleção de Horário ---")
    intervalo = int(input("1 para 1:30.\n2 para 1:00: \n"))
    atual = datetime.now()
    while True:
        if intervalo == 1:
            tempo = hora + timedelta(hours=1, minutes= 30)
            print(f"hora: {tempo.strftime("%H:%M")}")
            f = tempo - atual
            print(f"falta {f}.")

            break
        elif intervalo == 2:
            tempo = hora + timedelta(hours=1, minutes= 0)
            print(f"hora: {tempo.strftime('%H:%M')}")
            f = tempo - atual
            h = f.seconds // 3600
            m = (f.seconds // 60) % 60
            print(f"falta {h} horas e {m} minutos.")
            break
        else:
            print(f"{intervalo}, tipo de horario não encontrado")
            continue

if __name__ == "__main__":
    app()
    input("aperte enter para finalizar...")