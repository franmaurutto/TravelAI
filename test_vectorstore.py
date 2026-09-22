from src.vectorstore import cargar_vectorstore


vectorstore = cargar_vectorstore()

print("Cantidad de documentos en Chroma:")
print(vectorstore._collection.count())