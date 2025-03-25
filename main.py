def max_min_select(arr, left, right):
    if left == right:  # Caso base: apenas um elemento
        return arr[left], arr[left]
    
    if right - left == 1:  # Caso base: dois elementos
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    mid = (left + right) // 2  # Divide o array ao meio
    min1, max1 = max_min_select(arr, left, mid)  # Resolve o subproblema esquerdo
    min2, max2 = max_min_select(arr, mid + 1, right)  # Resolve o subproblema direito
    
    return min(min1, min2), max(max1, max2)  # Combina os resultados

if __name__ == "__main__":
    arr = [3, 1, 9, 2, 7, 5, 8, 6, 4,99,-2,55,54,-55,-99]
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")
