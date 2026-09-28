from src.retriever import crear_retriever


print("TEST DEL RETRIEVER")
print("=" * 50)


retriever = crear_retriever(k=4)


consulta = (
    "Quiero conocer actividades culturales "
    "y gastronómicas en Buenos Aires"
)


resultados = retriever.invoke(consulta)


print(f"Documentos recuperados: {len(resultados)}")


assert len(resultados) > 0
assert len(resultados) <= 4


for i, doc in enumerate(resultados):

    print("\n" + "-" * 50)
    print(f"RESULTADO {i + 1}")
    print("-" * 50)

    print(doc.page_content[:500])


print("\n" + "=" * 50)
print("✓ El retriever recuperó documentos correctamente.")