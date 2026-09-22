from src.retriever import crear_retriever


retriever = crear_retriever(k=4)


consulta = "Quiero conocer actividades culturales y gastronómicas en Buenos Aires"

resultados = retriever.invoke(consulta)


print(f"Documentos recuperados: {len(resultados)}")


for i, doc in enumerate(resultados):

    print("\n" + "=" * 60)
    print(f"RESULTADO {i + 1}")
    print("=" * 60)

    print(doc.page_content[:1000])