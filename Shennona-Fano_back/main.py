from shennonFanoCompression import shennon_fano_compression
from shennonFanoDecompression import shennon_fano_decompression
from max_value import mayor, lengths

print(mayor(lengths))
result = shennon_fano_compression()
print(result.code)
print(result.dictionary)
print(shennon_fano_decompression(result.code, result.dictionary))
