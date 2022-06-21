def importe_total_carro(request):
    total=0
    session = request.session
    carro = session.get("carro")
    if not carro:
        carro = session["carro"] = {}
    else:
        carro = carro

        carro = carro.items()
        for key, value in carro:

            total = total + value["precio"]

    return {"importe_total_carro": total}