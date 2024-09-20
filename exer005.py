luzes = {"lampada1": False, "lampada2": False, "lampada3": False}
interruptores = {"interruptor1": "lampada1", "interruptor2": "lampada2", "interruptor3": "lampada3"}

luzes["lampada1"] = True
tempo_primeiro_interruptor_ligado = 5

luzes["lampada1"] = False
luzes["lampada2"] = True

estado_lampadas = {
    "lampada1": {"acesa": luzes["lampada1"], "quente": tempo_primeiro_interruptor_ligado > 0},
    "lampada2": {"acesa": luzes["lampada2"], "quente": False},
    "lampada3": {"acesa": luzes["lampada3"], "quente": False}
}

for lampada, estado in estado_lampadas.items():
    if estado["acesa"]:
        print(f"O interruptor que controla a {lampada} é o interruptor2")
    elif estado["quente"]:
        print(f"O interruptor que controla a {lampada} é o interruptor1")
    else:
        print(f"O interruptor que controla a {lampada} é o interruptor3")