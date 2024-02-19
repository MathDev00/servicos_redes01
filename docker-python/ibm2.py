def getNumber(binary):
    if not binary:
        return 0
    
    decimal = 0
    current = binary
    
    while current:
        decimal = (decimal << 1) + current.data
        current = current.next
    
    return decimal

# Exemplo de uso:
# Criando a lista ligada: 0 -> 1 -> 0 -> 0 -> 1 -> 1 -> None
binary = SinglyLinkedList()
binary.insert_node(0)
binary.insert_node(1)
binary.insert_node(0)
binary.insert_node(0)
binary.insert_node(1)
binary.insert_node(1)

# Convertendo a lista ligada binária em número decimal
decimal_representation = getNumber(binary.head)
print(decimal_representation)  # Saída: 19
