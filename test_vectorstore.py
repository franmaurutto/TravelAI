from src.vectorstore import cargar_vectorstore


print("TEST DEL VECTORSTORE")
print("=" * 50)


vectorstore = cargar_vectorstore()

cantidad = vectorstore._collection.count()


print(f"Cantidad de documentos almacenados: {cantidad}")


assert cantidad > 0


print("=" * 50)
print("✓ El vectorstore contiene documentos.")