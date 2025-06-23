class ContainerBase:
    def __init__(self):
        self._size = 0

    def __str__(self):
        if not hasattr(self, 'first'):
            return "None"

        actual = self.first # type: ignore
        if actual is None:
            return "None"

        resultado = ""
        while actual:
            resultado += f"[{actual.value}]->"
            actual = actual.next
        return resultado + "None"
