from shennonFanoCompression import shennon_fano_compression
from shennonFanoDecompression import shennon_fano_decompression

result = shennon_fano_compression("Тестовая строка для проверки ошибки")
print(result.code)
print(result.dictionary)
print(shennon_fano_decompression(result.code, result.dictionary))
