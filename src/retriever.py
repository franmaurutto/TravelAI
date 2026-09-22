from .vectorstore import cargar_vectorstore


def crear_retriever(k=4):

    vectorstore = cargar_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever